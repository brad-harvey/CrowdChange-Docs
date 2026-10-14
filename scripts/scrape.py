# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Mirror CrowdChange's documentation into LLM-friendly Markdown.

Two collections:

  help-center  https://ch.crowdchange.help/cnak   (K15t Scroll Sites)  -> docs/help-center/
      /cnak/__pagetree.json (left-nav hierarchy), /llms.txt + sitemap (completeness),
      /cnak/<slug>.md (page Markdown), /cnak/<slug> HTML (last-modified + description meta tags)

  api          https://apidoc.crowdchange.dev     (Mintlify)           -> docs/api/
      /llms.txt (nav groups + descriptions), sitemap (completeness), /<path>.md (page MDX),
      overview HTML (method + path of every endpoint). MDX components are converted to plain Markdown.

Shared outputs: llms.txt (repo entry point) and docs/TAGS.md (topic index across both collections).

Usage (from the repo root):  uv run scripts/scrape.py [all|help-center|api]      (default: all)
"""

from __future__ import annotations

import concurrent.futures as cf
import datetime as dt
import html
import json
import posixpath
import re
import sys
import textwrap
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path.cwd()  # run from the repo root
DOCS = ROOT / "docs"
UA = "CrowdChange-Docs-mirror/1.0 (offline reference copy)"
RETRIEVED = dt.date.today().isoformat()

HC_BASE = "https://ch.crowdchange.help"
HC_SPACE = "/cnak"
HC_DIR = DOCS / "help-center"

API_BASE = "https://apidoc.crowdchange.dev"
API_DIR = DOCS / "api"

# Topic tags shared by both collections: tag -> keywords. Help-center pages match on title, or on >=4 body hits;
# API pages match on title, description and URL path only (their bodies are field lists that mention everything).
TAG_RULES: dict[str, list[str]] = {
    "fundraiser-setup": ["start a fundraiser", "create fundraiser", "duplicate a fundraiser", "close or reopen", "archive",
                         "date and time", "fundraising goal", "hide a fundraiser", "fundraiser approval"],
    "page-design": ["block", "cover", "image", "gallery", "avatar", "ui & design", "design", "photo", "banner",
                    "meta description", "fundraiser cards", "image editor"],
    "donations": ["donation", "donor", "pledg", "tribute", "matching", "installment", "encouragement"],
    "recurring-donations": ["recurring"],
    "offline-donations": ["offline donation", "offline transaction"],
    "ticketing": ["ticket"],
    "registration": ["registration", "register", "participant"],
    "merchandise": ["merchandise", "ecards"],
    "sponsorship": ["sponsorship"],
    "auctions": ["auction"],
    "purchase-options": ["purchase option", "promo code", "access code", "per-transaction", "ticket", "merchandise",
                         "sponsorship", "registration"],
    "peer-to-peer": ["personal page", "personal fundraising", "p2p", "peer to peer", "team", "co-captain",
                     "leaderboard", "participant center"],
    "teams": ["team"],
    "activity-tracking": ["activity", "strava"],
    "communications": ["email", "mailing list", "notification", "sharing", "share", "instagram", "social", "community feed"],
    "reporting-and-data": ["report", "export", "data included", "csv", "mass upload", "upload a list", "donations list"],
    "payments-and-receipts": ["refund", "failed transaction", "receipt", "tax", "payment", "installment"],
    "custom-questions": ["custom question"],
    "account-and-access": ["password", "profile", "multi-factor", "2fa", "access manager", "admin access", "opt out"],
    "troubleshooting": ["did not receive", "failed", "not found", "error", "browser"],
}
API_TAG_RULES: dict[str, list[str]] = {
    "webhooks": ["webhook"],
    "authentication": ["sign in", "sign out", "login", "logout", "how to authenticate", "authentication", "api key"],
    "transactions": ["transaction"],
    "search": ["search", "find "],
    "widgets": ["widget"],
    "analytics-tracking": ["analytics", "pixel", "tag manager", "conversions api", "events api"],
    "leaderboards": ["leaderboard", "top daily"],
}

# Help-center pages most likely to matter when integrating CrowdChange data with a CRM.
CRM_KEYWORDS = ["report", "export", "csv", "data included", "offline donation", "recurring", "refund", "receipt",
                "tax", "custom question", "registration", "mailing list", "opt out", "matching", "pledg",
                "installment", "tribute", "upload", "failed transaction", "tickets report", "access manager",
                "donor"]


# ----------------------------------------------------------------------------------------------- shared helpers

def fetch(url: str, binary: bool = False, retries: int = 3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                return data if binary else data.decode("utf-8")
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def download_all(images: dict[str, Path]):
    def dl(item):
        url, dest = item
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(fetch(url, binary=True))
    with cf.ThreadPoolExecutor(6) as ex:
        list(ex.map(dl, images.items()))


def front_matter(fm: dict) -> str:
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n\n"


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.replace("\\&", "&").lower()).strip()


def short(d: str | None, n: int = 160) -> str:
    d = (d or "").replace("\n", " ").strip()
    return d if len(d) <= n else d[: n - 1].rsplit(" ", 1)[0] + "…"


def match_tags(strong: str, body: str = "", rules: dict[str, list[str]] = TAG_RULES) -> set[str]:
    s = strong.lower()
    b = re.sub(r"!?\[[^\]]*\]\([^)]*\)", " ", body).lower()  # ignore image names and link targets
    return {tag for tag, kws in rules.items() if any(k in s for k in kws) or (b and sum(b.count(k) for k in kws) >= 4)}


def word_count(body: str) -> int:
    return len(re.findall(r"\w+", re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)))


def write_full_text(path: Path, heading: str, intro: str, files: list[str]):
    full = [f"# {heading}\n\n{intro} Pages are separated by '=====' lines and begin with YAML front matter.\n"]
    for f in files:
        full.append("\n" + "=" * 80 + "\n" + (ROOT / f).read_text(encoding="utf-8"))
    write(path, "".join(full))


def write_manifest(path: Path, source: str, pages: list[dict]):
    write(path, json.dumps({"source": source, "retrieved": RETRIEVED, "page_count": len(pages), "pages": pages},
                           indent=2, ensure_ascii=False))


# ------------------------------------------------------------------------------------------------- help center

def hc_slug(path_or_url: str) -> str | None:
    p = urllib.parse.urlparse(path_or_url).path
    m = re.fullmatch(rf"{HC_SPACE}/([^/]+?)(?:\.md)?/?", p)
    return m.group(1) if m else None


def hc_walk(nodes, parents, parent_slug, out, order):
    for n in nodes:
        slug = hc_slug(n["path"])
        order[0] += 1
        out[slug] = {"title": n["title"], "nav_path": parents + [n["title"]], "nav_order": order[0],
                     "parent": parent_slug, "children": [hc_slug(c["path"]) for c in n.get("children", [])]}
        hc_walk(n.get("children", []), parents + [n["title"]], slug, out, order)


def hc_discover() -> dict[str, dict]:
    pages: dict[str, dict] = {}
    hc_walk(json.loads(fetch(f"{HC_BASE}{HC_SPACE}/__pagetree.json")), [], None, pages, [0])
    extra: dict[str, str | None] = {}
    for title, url in re.findall(r"\* \[(.+?)\]\((https://[^)]+)\)", fetch(f"{HC_BASE}/llms.txt")):
        extra[hc_slug(url)] = title
    for sm in re.findall(r"<loc>(.*?)</loc>", fetch(f"{HC_BASE}/sitemap.xml")):
        for loc in re.findall(r"<loc>(.*?)</loc>", fetch(sm)):
            extra.setdefault(hc_slug(loc), None)
    for slug, title in extra.items():
        if slug and slug not in pages:
            pages[slug] = {"title": title, "nav_path": None, "nav_order": None, "parent": None, "children": []}
    pages.setdefault("help-center-home", {"title": "Help Center", "nav_path": None, "nav_order": 0,
                                          "parent": None, "children": [], "_src": f"{HC_BASE}{HC_SPACE}"})
    return pages


def hc_meta(html_text: str, name: str) -> str | None:
    m = re.search(rf'<meta (?:name|property)="{re.escape(name)}" content="([^"]*)"', html_text)
    return html.unescape(html.unescape(m.group(1))) if m else None  # site double-encodes entities


def hc_page_type(title: str) -> str:
    t = title.lower()
    if re.search(r"did not receive|failed|not found|error|recommended web browsers", t):
        return "troubleshooting"
    if t.startswith("how ") and " works" in t or t.startswith("importance"):
        return "concept"
    if t.startswith("how to") or " - how to" in t or "setup" in t or "setting up" in t:
        return "how-to"
    if t in {"featured", "help center", "what's new section"}:
        return "navigation"
    return "reference"


def scrape_help_center() -> list[dict]:
    pages_dir, assets_dir = HC_DIR / "pages", HC_DIR / "assets"
    pages = hc_discover()
    print(f"[help-center] discovered {len(pages)} pages")

    def get(slug):
        src = pages[slug].get("_src", f"{HC_BASE}{HC_SPACE}/{slug}")
        return slug, fetch(src + ".md"), fetch(src)

    raw = {}
    with cf.ThreadPoolExecutor(4) as ex:
        for slug, md, page_html in ex.map(get, pages):
            raw[slug] = (md, page_html)

    title_to_slug = {}
    for slug, (md, page_html) in raw.items():
        h1 = re.search(r"^# (.+)$", md, re.M)
        p = pages[slug]
        p["title"] = p["title"] or (h1.group(1).replace("\\&", "&") if h1 else slug)
        p["last_modified"] = hc_meta(page_html, "page-last-modified")
        p["description"] = hc_meta(page_html, "description")
        title_to_slug[norm(p["title"])] = slug
        if h1:
            title_to_slug.setdefault(norm(h1.group(1)), slug)

    images: dict[str, Path] = {}
    manifest = []
    for slug, (md, _) in sorted(raw.items()):
        p = pages[slug]
        body = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S).strip()

        # Images -> local files under assets/<slug>/
        def img(m):
            alt, url = m.group(1), m.group(2)
            fname = re.sub(r"[^\w.\-]", "_", urllib.parse.unquote(urllib.parse.urlparse(url).path.rsplit("/", 1)[-1]))
            images[url] = assets_dir / slug / fname
            return f"![{alt}](../assets/{slug}/{fname})"
        body = re.sub(r"!\[([^\]]*)\]\((https://ch\.crowdchange\.help/__attachments/[^)\s]+)\)", img, body)

        # Internal links -> relative .md files; unknown ones -> live URL
        def link(m):
            text, url = m.group(1), m.group(2)
            full = urllib.parse.urljoin(HC_BASE, url)
            u = urllib.parse.urlparse(full)
            if u.netloc != urllib.parse.urlparse(HC_BASE).netloc:
                return m.group(0)
            s = hc_slug(full)
            frag = f"#{u.fragment}" if u.fragment else ""
            if u.path.rstrip("/") == HC_SPACE or u.path == f"{HC_SPACE}.md":
                s = "help-center-home"
            if s not in pages:  # legacy Confluence export links: /cnak/Page-Title.123456.html
                legacy = re.sub(r"\.\d+\.html$", "", urllib.parse.unquote(u.path.rsplit("/", 1)[-1]))
                s = title_to_slug.get(norm(legacy.replace("-", " ")), s)
            if s in pages:
                return f"[{text}]({s}.md{frag})"
            return f"[{text}]({full.replace('.md', '')})"
        body = re.sub(r"(?<!!)\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)", link, body)
        body = re.sub(r"\+\+(.+?)\+\+", r"\1", body)  # Confluence underline markup

        # "Related tutorials" are plain bold titles on the site; link them when they match a page title.
        def bold(m):
            s = title_to_slug.get(norm(m.group(2)))
            return f"{m.group(1)}[{m.group(2)}]({s}.md)" if s and s != slug else m.group(0)
        body = re.sub(r"^(\s*[*-] +)\*\*(.+?)\*\*\s*$", bold, body, flags=re.M)

        text = re.sub(r"!?\[[^\]]*\]\([^)]*\)", " ", body).lower()
        crm = (any(k in p["title"].lower() for k in CRM_KEYWORDS)
               or sum(text.count(k) for k in CRM_KEYWORDS) >= 6)
        file = f"docs/help-center/pages/{slug}.md"
        fm = {
            "title": p["title"],
            "slug": slug,
            "collection": "help-center",
            "source_url": p.get("_src", f"{HC_BASE}{HC_SPACE}/{slug}"),
            "nav_path": p["nav_path"] or [p["title"]],
            "nav_order": p["nav_order"],
            "parent": p["parent"],
            "children": p["children"] or [],
            "page_type": hc_page_type(p["title"]),
            "tags": sorted(match_tags(p["title"], body)),
            "crm_relevant": crm,
            "description": p["description"],
            "last_modified": p["last_modified"],
            "retrieved": RETRIEVED,
            "audience": "Charities Non-Admin (CrowdChange help center space CNAK)",
            "word_count": word_count(body),
        }
        p.update(fm)
        nav = " > ".join(fm["nav_path"])
        write(ROOT / file, front_matter(fm)
              + f"<!-- Source: {fm['source_url']} | Nav: {nav} | Mirrored {RETRIEVED} -->\n\n" + body + "\n")
        manifest.append({k: fm[k] for k in ("slug", "collection", "title", "source_url", "nav_path", "parent",
                                             "children", "page_type", "tags", "crm_relevant", "description",
                                             "last_modified", "word_count")} | {"file": file})

    download_all(images)
    print(f"[help-center] wrote {len(manifest)} pages, {len(images)} images")
    hc_indexes(pages, manifest)
    return manifest


def hc_indexes(pages, manifest):
    by_slug = {m["slug"]: m for m in manifest}
    tree = sorted((s for s in by_slug if pages[s].get("nav_order") and pages[s]["nav_path"]
                   and s != "help-center-home"), key=lambda s: pages[s]["nav_order"])
    orphans = sorted(s for s in by_slug if s not in tree)
    ordered = [by_slug[s] for s in tree + orphans]
    for i, m in enumerate(ordered):
        m["order"] = i

    lines = ["# CrowdChange Help Center - Index", "",
             f"Mirrored from {HC_BASE}{HC_SPACE} on {RETRIEVED}. Order and nesting match the site's left navigation.",
             "Each entry: title - page type - one-line summary. Topic index across both collections: "
             "[../TAGS.md](../TAGS.md).", ""]
    for s in tree:
        m = by_slug[s]
        depth = len(pages[s]["nav_path"]) - 1
        lines.append(f"{'  ' * depth}- [{m['title']}](pages/{s}.md) - *{m['page_type']}* - {short(m['description'])}")
    if orphans:
        lines += ["", "## Pages not in the left navigation", "",
                  "Found via the site's llms.txt / sitemap (e.g. linked from the home page or Featured).", ""]
        lines += [f"- [{by_slug[s]['title']}](pages/{s}.md) - *{by_slug[s]['page_type']}* - "
                  f"{short(by_slug[s]['description'])}" for s in orphans]
    write(HC_DIR / "INDEX.md", "\n".join(lines) + "\n")

    write_manifest(HC_DIR / "manifest.json", f"{HC_BASE}{HC_SPACE}", ordered)
    write_full_text(HC_DIR / "llms-full.txt", "CrowdChange Help Center - full text",
                    f"All {len(ordered)} pages from {HC_BASE}{HC_SPACE}, retrieved {RETRIEVED}.",
                    [m["file"] for m in ordered])


# ---------------------------------------------------------------------------------------------- API reference

MDX_TAG = re.compile(
    r"^\s*<(/?)(ParamField|ResponseField|Expandable|ResponseExample|RequestExample|Note|Tip|Warning|Info|Check|"
    r"Frame|CodeGroup|Accordion|AccordionGroup|Steps|Step|Tabs|Tab|Card|CardGroup)"
    r"((?:\s+[\w-]+(?:=(?:\"[^\"]*\"|\{[^}]*\}))?)*)\s*(/?)>\s*$")
MDX_ATTR = re.compile(r"([\w-]+)(?:=(?:\"([^\"]*)\"|\{([^}]*)\}))?")
FIELD_LINE = re.compile(r"^\s*- `")


def mdx_parse(lines: list[str]) -> dict:
    """Build a tree of MDX component nodes; text lines (and anything inside code fences) stay as strings."""
    root = {"kind": "root", "attrs": {}, "children": []}
    stack, fence = [root], False
    for line in lines:
        s = line.strip()
        if not fence:
            m = MDX_TAG.match(line)
            if m:
                closing, kind, attrs, selfclose = m.groups()
                if closing:
                    while len(stack) > 1 and stack.pop()["kind"] != kind:
                        pass
                else:
                    node = {"kind": kind, "children": [],
                            "attrs": {k: (v if v is not None else e) for k, v, e in MDX_ATTR.findall(attrs)}}
                    stack[-1]["children"].append(node)
                    if not selfclose:
                        stack.append(node)
                continue
        if s.startswith("```"):
            fence = not fence if (not fence or s.strip("`") == "") else fence
        stack[-1]["children"].append(line)
    return root


def mdx_render(node: dict) -> list[str]:
    out, buf = [], []

    def flush():
        if buf:
            out.extend(textwrap.dedent("\n".join(buf)).split("\n"))
            buf.clear()
    for c in node["children"]:
        if isinstance(c, str):
            buf.append(c)
        else:
            flush()
            out.extend(mdx_node(c))
    flush()
    return out


def trim(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def mdx_node(node: dict) -> list[str]:
    kind, a = node["kind"], node["attrs"]
    inner = trim(mdx_render(node))
    if kind in ("ParamField", "ResponseField"):
        loc = next((k for k in ("path", "query", "body", "header", "cookie") if k in a), None)
        name = a.get(loc) if loc else a.get("name", "?")
        meta = [a["type"]] if a.get("type") else []
        meta += [loc] if loc else []
        meta += ["**required**"] if "required" in a else []
        meta += [f"default: `{a['default']}`"] if a.get("default") else []
        desc = []
        while inner and inner[0].strip() and not re.match(r"\s*(```|[-*] |\||>|!|<|\d+\. )", inner[0]):
            desc.append(inner.pop(0).strip())
        head = f"- `{name}`" + (f" ({', '.join(meta)})" if meta else "") + (f" — {' '.join(desc)}" if desc else "")
        return [head] + ["  " + l if l.strip() else "" for l in trim(inner)]
    if kind == "Expandable":
        title = a.get("title", "")
        return ([f"*{title}:*"] if title and title.lower() not in ("properties", "property") else []) + inner
    if kind in ("ResponseExample", "RequestExample"):
        return ["", f"**{'Response' if kind == 'ResponseExample' else 'Request'} example:**", ""] + inner + [""]
    if kind in ("Note", "Tip", "Warning", "Info", "Check"):
        if not inner:
            return []
        return ["", f"> **{kind}:** {inner[0]}"] + [f"> {l}" if l.strip() else ">" for l in inner[1:]] + [""]
    if kind in ("Accordion", "Step", "Tab", "Card") and a.get("title"):
        return ["", f"**{a['title']}**", ""] + inner + [""]
    return inner  # Frame, CodeGroup, Steps, Tabs, CardGroup, AccordionGroup: transparent wrappers


def mdx_to_markdown(md: str) -> str:
    lines = mdx_render(mdx_parse(md.split("\n")))
    out, fence = [], False
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("```"):
            if not fence:
                line = re.sub(r"\s+theme=\{[^}]*\}", "", line)
                m = re.match(r"^(\s*)```(\S+)\s+(.+)$", line)  # CodeGroup tab title: ```json Full refund
                if m:
                    out += [f"{m.group(1)}**{m.group(3)}**", ""]
                    line = f"{m.group(1)}```{m.group(2)}"
            fence = not fence if (not fence or s.strip("`") == "") else fence
        elif not fence and not s:
            # drop blank lines between consecutive field bullets to keep long schemas compact
            prev = next((l for l in reversed(out) if l.strip()), "")
            nxt = next((l for l in lines[i + 1:] if l.strip()), "")
            if FIELD_LINE.match(prev) and FIELD_LINE.match(nxt) or (out and not out[-1].strip()):
                continue
        out.append(line)
    return "\n".join(out)


def api_discover() -> dict[str, dict]:
    pages: dict[str, dict] = {}
    heads: dict[int, str | None] = {2: None, 3: None, 4: None}
    for line in fetch(f"{API_BASE}/llms.txt").splitlines():
        if m := re.match(r"^(#{2,4}) (.+)$", line):
            lvl = len(m.group(1))
            heads[lvl] = m.group(2).strip()
            for k in range(lvl + 1, 5):
                heads[k] = None
        elif m := re.match(rf"^- \[(.+?)\]\({re.escape(API_BASE)}/(.+?)\.md\)(?::\s*(.*))?$", line):
            pages[m.group(2)] = {"title": m.group(1), "description": m.group(3),
                                 "nav_path": [h for h in heads.values() if h] + [m.group(1)],
                                 "nav_order": len(pages) + 1}
    for loc in re.findall(r"<loc>(.*?)</loc>", fetch(f"{API_BASE}/sitemap.xml")):
        path = urllib.parse.urlparse(loc).path.strip("/")
        if path and not re.match(r"fr(-ca)?(/|$)", path, re.I) and path not in pages:
            pages[path] = {"title": None, "description": None, "nav_path": None, "nav_order": None}
    return pages


def api_surface(path: str) -> str | None:
    return next((s for s in ("server-side", "client-side") if f"api-reference/{s}/" in path), None)


def api_page_type(path: str, endpoint: str | None) -> str:
    if endpoint:
        return "endpoint"
    if path.startswith("api-reference/"):
        return "reference"
    return "guide"


def api_auth(endpoint_path: str | None) -> str | None:
    if not endpoint_path:
        return None
    if endpoint_path.startswith("/v2/private/user/") and not endpoint_path.endswith("/login"):
        return "API key + user token"
    return "API key"


def scrape_api() -> list[dict]:
    pages_dir, assets_dir = API_DIR / "pages", API_DIR / "assets"
    pages = api_discover()
    print(f"[api] discovered {len(pages)} pages")

    with cf.ThreadPoolExecutor(4) as ex:
        raw = dict(zip(pages, ex.map(lambda p: fetch(f"{API_BASE}/{p}.md"), pages)))

    # Every page's HTML embeds the sidebar data, including "api":"GET /v2/..." for each endpoint page.
    overview_html = fetch(f"{API_BASE}/api-reference/overview").replace('\\"', '"')
    endpoints = {href: (method, path) for method, path, href
                 in re.findall(r'"api":"([A-Z]+) ([^"]+)","href":"/([^"]+)"', overview_html)}
    base_urls = re.findall(r"^\|\s*([^|]+?)\s*\|\s*`(https://api\.[^`]+)`\s*\|", raw.get("api-reference/overview", ""),
                           re.M)

    def rel(target: str, frm: str) -> str:
        return posixpath.relpath(f"pages/{target}.md", posixpath.dirname(f"pages/{frm}.md"))

    images: dict[str, Path] = {}
    manifest = []
    for path, md in raw.items():
        p = pages[path]
        md = re.sub(r"\A> ## Documentation Index\n(?:>.*\n)*\s*", "", md.replace("\r\n", "\n"))
        md = re.sub(r"\n*This documentation is built and hosted on \[Mintlify\].*\s*\Z", "\n", md)
        h1 = re.search(r"^# (.+)$", md, re.M)
        p["title"] = p["title"] or (h1.group(1) if h1 else path)
        if not p["description"] and (d := re.search(r"^# .+\n+> (.+)$", md, re.M)):
            p["description"] = d.group(1)

        body = mdx_to_markdown(md)

        def img(m):
            src = html.unescape(m.group(0))
            url = re.search(r'src="([^"]+)"', src).group(1)
            alt = (re.search(r'alt="([^"]*)"', src) or [None, ""])[1]
            name = (re.search(r'data-path="([^"]+)"', src) or [None, urllib.parse.urlparse(url).path.lstrip("/")])[1]
            name = re.sub(r"[^\w./\-]", "_", name.replace("images/", "", 1))
            images[url] = assets_dir / name
            return f"![{alt}]({posixpath.relpath(f'assets/{name}', posixpath.dirname(f'pages/{path}.md'))})"
        body = re.sub(r"<img\s[^>]*?/?>", img, body)

        def md_img(m):
            url = m.group(2)
            name = re.sub(r"[^\w.\-]", "_", urllib.parse.urlparse(url).path.rsplit("/", 1)[-1])
            images[url] = assets_dir / name
            return f"![{m.group(1)}]({posixpath.relpath(f'assets/{name}', posixpath.dirname(f'pages/{path}.md'))})"
        body = re.sub(r"!\[([^\]]*)\]\((https://[^)\s]+)\)", md_img, body)

        def link(m):
            text, url = m.group(1), m.group(2)
            u = urllib.parse.urlparse(urllib.parse.urljoin(API_BASE + "/", url))
            if u.netloc != urllib.parse.urlparse(API_BASE).netloc:
                return m.group(0)
            target = re.sub(r"\.md$", "", u.path.strip("/"))
            frag = f"#{u.fragment}" if u.fragment else ""
            if target in pages:
                return f"[{text}]({rel(target, path)}{frag})"
            return f"[{text}]({API_BASE}/{target}{frag})"
        body = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", link, body)

        method, ep_path = endpoints.get(path, (None, None))
        endpoint = f"{method} {ep_path}" if method else None
        surface = api_surface(path)
        auth = api_auth(ep_path)
        if endpoint:
            info = [f"**Endpoint:** `{endpoint}`  ",
                    f"**Surface:** {surface.replace('-', ' ').title()} API"
                    + (" (server-to-server only; never call from a browser)" if surface == "server-side" else "")
                    + f" · **Auth:** {auth} — `Authorization: Bearer {{api-key}}` header"
                    + (", plus the user token in the `auth-token` header or `token` param" if "user token" in auth else "")
                    + "  ",
                    "**Base URLs:** " + " · ".join(f"{n} `{u}`" for n, u in base_urls)
                    + f" (see [Overview]({rel('api-reference/overview', path)}))"]
            body = re.sub(r"(^# .+\n+(?:> .+\n)*)", lambda m: m.group(1) + "\n" + "\n".join(info) + "\n",
                          body, count=1, flags=re.M)

        tags = match_tags(f"{p['title']} {p['description'] or ''} {path.replace('-', ' ').replace('_', ' ')}")
        tags |= match_tags(f"{p['title']} {p['description'] or ''} {path.replace('-', ' ')}", rules=API_TAG_RULES)
        file = f"docs/api/pages/{path}.md"
        fm = {
            "title": p["title"],
            "slug": path,
            "collection": "api",
            "source_url": f"{API_BASE}/{path}",
            "nav_path": p["nav_path"] or [p["title"]],
            "nav_order": p["nav_order"],
            "page_type": api_page_type(path, endpoint),
            "endpoint": endpoint,
            "http_method": method,
            "endpoint_path": ep_path,
            "api_surface": surface,
            "auth": auth,
            "tags": sorted(tags),
            "crm_relevant": surface == "server-side" or path == "api-reference/overview",
            "description": p["description"],
            "retrieved": RETRIEVED,
            "word_count": word_count(body),
        }
        nav = " > ".join(fm["nav_path"])
        write(ROOT / file, front_matter(fm)
              + f"<!-- Source: {fm['source_url']} | Nav: {nav} | Mirrored {RETRIEVED} -->\n\n" + body.strip() + "\n")
        manifest.append({k: v for k, v in fm.items() if k != "retrieved"} | {"file": file})

    missing = [p for p in raw if re.search(r"/(get|post|put|patch|delete)_v2", p) and p not in endpoints]
    if missing:
        print(f"[api] WARNING no method/path found for: {missing}")
    download_all(images)
    manifest.sort(key=lambda m: (m["nav_order"] is None, m["nav_order"] or 0, m["slug"]))
    for i, m in enumerate(manifest):
        m["order"] = i
    print(f"[api] wrote {len(manifest)} pages ({sum(1 for m in manifest if m['endpoint'])} endpoints), "
          f"{len(images)} images")
    api_indexes(manifest)
    return manifest


def api_indexes(manifest):
    lines = ["# CrowdChange API & Developer Docs - Index", "",
             f"Mirrored from {API_BASE} on {RETRIEVED}. Sections and order match the site's sidebar.",
             "Endpoint entries show `METHOD /path`. Start with [Overview](pages/api-reference/overview.md) for base URLs, "
             "authentication, status codes and error formats. Topic index across both collections: "
             "[../TAGS.md](../TAGS.md).", ""]
    current: list[str] = []
    for m in manifest:
        groups = m["nav_path"][:-1] if m["nav_order"] else ["Pages not in the sidebar"]
        for depth, g in enumerate(groups):
            if current[: depth + 1] != groups[: depth + 1]:
                lines += ["", f"{'#' * (depth + 2)} {g}", ""]
        current = groups
        ep = f" — `{m['endpoint']}`" if m["endpoint"] else ""
        lines.append(f"- [{m['title']}](pages/{m['slug']}.md){ep} — {short(m['description'])}")
    lines += ["", "## Endpoint quick reference", "",
              "| Method | Path | Surface | Auth | Page |", "| :- | :- | :- | :- | :- |"]
    for m in sorted((m for m in manifest if m["endpoint"]), key=lambda m: (m["endpoint_path"], m["http_method"])):
        lines.append(f"| {m['http_method']} | `{m['endpoint_path']}` | {m['api_surface']} | {m['auth']} | "
                     f"[{m['title']}](pages/{m['slug']}.md) |")
    write(API_DIR / "INDEX.md", re.sub(r"\n{3,}", "\n\n", "\n".join(lines)) + "\n")

    write_manifest(API_DIR / "manifest.json", API_BASE, manifest)
    write_full_text(API_DIR / "llms-full.txt", "CrowdChange API & Developer Docs - full text",
                    f"All {len(manifest)} pages from {API_BASE}, retrieved {RETRIEVED}.",
                    [m["file"] for m in manifest])


# ----------------------------------------------------------------------------------------------- shared indexes

def load_manifest(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))["pages"] if path.exists() else []


def shared_indexes(hc: list[dict], api: list[dict]):
    hc, api = sorted(hc, key=lambda m: m["order"]), sorted(api, key=lambda m: m["order"])

    def link(m, base=""):
        ep = f" — `{m['endpoint']}`" if m.get("endpoint") else ""
        return f"- [{m['title']}]({base}{m['file'].removeprefix('docs/')}){ep}"

    # docs/TAGS.md: one topic index across both collections
    tags: dict[str, dict[str, list]] = {}
    for m in hc + api:
        for t in m["tags"]:
            tags.setdefault(t, {"help-center": [], "api": []})[m["collection"]].append(m)
    tl = ["# Topic Tags", "",
          "Pages from both collections grouped by topic, so a help-center article and the API endpoints for the same "
          "feature sit side by side. Tags are keyword-derived; use them to narrow a search, not as ground truth.", "",
          "## Contents", ""]
    tl += [f"- [{t}](#{t}) ({len(v['help-center'])} help, {len(v['api'])} API)" for t, v in sorted(tags.items())]
    tl += ["- [crm-relevant](#crm-relevant)", ""]
    for t, v in sorted(tags.items()):
        tl += [f"## {t}", ""]
        for coll, label in (("help-center", "Help Center"), ("api", "API")):
            if v[coll]:
                tl += [f"**{label}**", ""] + [link(m) for m in v[coll]] + [""]
    tl += ["## crm-relevant", "",
           "Likely to matter for a CRM integration. Help-center pages: keyword match on data, reporting, donations, "
           "receipts, registrations, etc. API pages: every server-side endpoint, plus the overview.", ""]
    for coll, items in (("Help Center", hc), ("API", api)):
        tl += [f"**{coll}**", ""] + [link(m) for m in items if m["crm_relevant"]] + [""]
    write(DOCS / "TAGS.md", "\n".join(tl))

    # llms.txt (llmstxt.org format): the repo's entry point
    lt = ["# CrowdChange Docs (offline mirror)", "",
          "> Offline Markdown mirror of CrowdChange's two documentation sites: the charity Help Center "
          f"({HC_BASE}{HC_SPACE}), which covers using the platform UI, and the API & developer docs ({API_BASE}): "
          "REST endpoints, webhooks, widgets and analytics integrations. Built as reference material for a "
          f"CrowdChange-to-CRM integration. Retrieved {RETRIEVED}.", "",
          "Navigation: docs/help-center/INDEX.md and docs/api/INDEX.md (trees, plus an endpoint table for the API), "
          "docs/TAGS.md (topics across both). Each collection has a manifest.json with every page's metadata. "
          "Every page starts with YAML front matter.", "",
          f"## Help Center ({len(hc)} pages)", ""]
    lt += [f"- [{m['title']}]({m['file']}): {short(m['description'], 140)}" for m in hc]
    lt += ["", f"## API & Developer Docs ({len(api)} pages)", ""]
    lt += [f"- [{m['title']}]({m['file']}): " + (f"`{m['endpoint']}` — " if m.get("endpoint") else "")
           + short(m["description"], 140) for m in api]
    lt += ["", "## Optional", "",
           "- [Help Center full text](docs/help-center/llms-full.txt): every help-center page in one file",
           "- [API full text](docs/api/llms-full.txt): every API page in one file",
           "- [Help Center manifest](docs/help-center/manifest.json): page metadata as JSON",
           "- [API manifest](docs/api/manifest.json): page metadata as JSON, including method/path per endpoint"]
    write(ROOT / "llms.txt", "\n".join(lt) + "\n")


def main():
    mode = (sys.argv[1:] or ["all"])[0]
    if mode not in ("all", "help-center", "api"):
        sys.exit(f"unknown mode {mode!r}; use all, help-center or api")
    hc = scrape_help_center() if mode in ("all", "help-center") else load_manifest(HC_DIR / "manifest.json")
    api = scrape_api() if mode in ("all", "api") else load_manifest(API_DIR / "manifest.json")
    shared_indexes(hc, api)
    print("Shared indexes written: llms.txt, docs/TAGS.md")


if __name__ == "__main__":
    main()
