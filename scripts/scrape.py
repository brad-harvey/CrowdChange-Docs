# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Mirror the CrowdChange Help Center (https://ch.crowdchange.help/cnak) into LLM-friendly Markdown.

Sources used (all published by the K15t Scroll Sites platform hosting the help center):
  * /cnak/__pagetree.json  - left-nav hierarchy and ordering
  * /llms.txt + sitemap     - catch any page not shown in the nav
  * /cnak/<slug>.md         - clean Markdown rendering of each page
  * /cnak/<slug> (HTML)     - metadata (last modified, description)

Usage:  uv run scripts/scrape.py        (from the repo root)
"""

from __future__ import annotations

import concurrent.futures as cf
import datetime as dt
import html
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

BASE = "https://ch.crowdchange.help"
SPACE = "/cnak"
ROOT = Path.cwd()  # run from the repo root
PAGES_DIR = ROOT / "docs" / "pages"
ASSETS_DIR = ROOT / "docs" / "assets"
UA = "CrowdChange-Docs-mirror/1.0 (offline reference copy)"

# Tag rules: tag -> keywords matched against the title (strong) and body (weak, needs >=2 hits).
TAG_RULES: dict[str, list[str]] = {
    "fundraiser-setup": ["start a fundraiser", "create fundraiser", "duplicate a fundraiser", "close or reopen", "archive",
                         "date and time", "fundraising goal", "hide a fundraiser", "fundraiser approval"],
    "page-design": ["block", "cover", "image", "gallery", "avatar", "ui & design", "design", "photo", "banner",
                    "meta description", "fundraiser cards", "image editor"],
    "donations": ["donation", "donor", "pledg", "tribute", "matching", "installment", "encouragement"],
    "recurring-donations": ["recurring"],
    "offline-donations": ["offline donation"],
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

# Pages most likely to matter when integrating CrowdChange data with a CRM.
CRM_KEYWORDS = ["report", "export", "csv", "data included", "offline donation", "recurring", "refund", "receipt",
                "tax", "custom question", "registration", "mailing list", "opt out", "matching", "pledg",
                "installment", "tribute", "upload", "failed transaction", "tickets report", "access manager",
                "donor"]


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


def slug_of(path_or_url: str) -> str | None:
    p = urllib.parse.urlparse(path_or_url).path
    m = re.fullmatch(rf"{SPACE}/([^/]+?)(?:\.md)?/?", p)
    return m.group(1) if m else None


def walk_tree(nodes, parents, parent_slug, out, order):
    for n in nodes:
        slug = slug_of(n["path"])
        order[0] += 1
        out[slug] = {"title": n["title"], "nav_path": parents + [n["title"]], "nav_order": order[0],
                     "parent": parent_slug, "children": [slug_of(c["path"]) for c in n.get("children", [])]}
        walk_tree(n.get("children", []), parents + [n["title"]], slug, out, order)


def discover() -> dict[str, dict]:
    tree = json.loads(fetch(f"{BASE}{SPACE}/__pagetree.json"))
    pages: dict[str, dict] = {}
    walk_tree(tree, [], None, pages, [0])
    extra: dict[str, str] = {}
    for title, url in re.findall(r"\* \[(.+?)\]\((https://[^)]+)\)", fetch(f"{BASE}/llms.txt")):
        extra[slug_of(url)] = title
    index = fetch(f"{BASE}/sitemap.xml")
    for sm in re.findall(r"<loc>(.*?)</loc>", index):
        for loc in re.findall(r"<loc>(.*?)</loc>", fetch(sm)):
            extra.setdefault(slug_of(loc), None)
    for slug, title in extra.items():
        if slug and slug not in pages:
            pages[slug] = {"title": title, "nav_path": None, "nav_order": None, "parent": None, "children": []}
    return pages


def meta(html_text: str, name: str) -> str | None:
    m = re.search(rf'<meta (?:name|property)="{re.escape(name)}" content="([^"]*)"', html_text)
    return html.unescape(html.unescape(m.group(1))) if m else None  # site double-encodes entities


def page_type(title: str) -> str:
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


def tags_for(title: str, body: str) -> list[str]:
    t = title.lower()
    b = re.sub(r"!?\[[^\]]*\]\([^)]*\)", " ", body).lower()  # ignore image names and link targets
    tags = [tag for tag, kws in TAG_RULES.items()
            if any(k in t for k in kws) or sum(b.count(k) for k in kws) >= 4]
    return sorted(set(tags))


def main():
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    pages = discover()
    pages.setdefault("help-center-home", {"title": "Help Center", "nav_path": None, "nav_order": 0,
                                          "parent": None, "children": [], "_src": f"{BASE}{SPACE}"})
    print(f"Discovered {len(pages)} pages")

    def get(slug):
        src = pages[slug].get("_src", f"{BASE}{SPACE}/{slug}")
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
        p["last_modified"] = meta(page_html, "page-last-modified")
        p["description"] = meta(page_html, "description")
        title_to_slug[norm(p["title"])] = slug
        if h1:
            title_to_slug.setdefault(norm(h1.group(1)), slug)

    images: dict[str, tuple[str, Path]] = {}
    retrieved = dt.date.today().isoformat()
    manifest = []
    for slug, (md, _) in sorted(raw.items()):
        p = pages[slug]
        body = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S).strip()

        # Images -> local files under docs/assets/<slug>/
        def img(m):
            alt, url = m.group(1), m.group(2)
            fname = re.sub(r"[^\w.\-]", "_", urllib.parse.unquote(urllib.parse.urlparse(url).path.rsplit("/", 1)[-1]))
            dest = ASSETS_DIR / slug / fname
            images[url] = (url, dest)
            return f"![{alt}](../assets/{slug}/{fname})"
        body = re.sub(r"!\[([^\]]*)\]\((https://ch\.crowdchange\.help/__attachments/[^)\s]+)\)", img, body)

        # Internal links -> relative .md files; unknown ones -> live URL
        def link(m):
            text, url = m.group(1), m.group(2)
            full = urllib.parse.urljoin(BASE, url)
            u = urllib.parse.urlparse(full)
            if u.netloc != urllib.parse.urlparse(BASE).netloc:
                return m.group(0)
            s = slug_of(full)
            frag = f"#{u.fragment}" if u.fragment else ""
            if u.path.rstrip("/") == SPACE or u.path == f"{SPACE}.md":
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

        tags = tags_for(p["title"], body)
        text = re.sub(r"!?\[[^\]]*\]\([^)]*\)", " ", body).lower()
        crm = (any(k in p["title"].lower() for k in CRM_KEYWORDS)
               or sum(text.count(k) for k in CRM_KEYWORDS) >= 6)
        fm = {
            "title": p["title"],
            "slug": slug,
            "source_url": pages[slug].get("_src", f"{BASE}{SPACE}/{slug}"),
            "nav_path": p["nav_path"] or [p["title"]],
            "nav_order": p["nav_order"],
            "parent": p["parent"],
            "children": p["children"] or [],
            "page_type": page_type(p["title"]),
            "tags": tags,
            "crm_relevant": crm,
            "description": p["description"],
            "last_modified": p["last_modified"],
            "retrieved": retrieved,
            "audience": "Charities Non-Admin (CrowdChange help center space CNAK)",
            "word_count": len(re.findall(r"\w+", re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body))),
        }
        p.update(fm)
        nav = " > ".join(fm["nav_path"])
        out = ("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n\n"
               f"<!-- Source: {fm['source_url']} | Nav: {nav} | Mirrored {retrieved} -->\n\n" + body + "\n")
        (PAGES_DIR / f"{slug}.md").write_text(out, encoding="utf-8", newline="\n")
        manifest.append({k: fm[k] for k in ("slug", "title", "source_url", "nav_path", "parent", "children",
                                             "page_type", "tags", "crm_relevant", "description",
                                             "last_modified", "word_count")}
                        | {"file": f"docs/pages/{slug}.md"})

    def dl(item):
        url, dest = item
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(fetch(url, binary=True))
    with cf.ThreadPoolExecutor(6) as ex:
        list(ex.map(dl, images.values()))
    print(f"Wrote {len(manifest)} pages, {len(images)} images")

    write_indexes(pages, manifest, retrieved)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.replace("\\&", "&").lower()).strip()


def write_indexes(pages, manifest, retrieved):
    by_slug = {m["slug"]: m for m in manifest}
    (ROOT / "manifest.json").write_text(json.dumps({"source": f"{BASE}{SPACE}", "retrieved": retrieved,
                                                    "page_count": len(manifest), "pages": manifest},
                                                   indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")

    # Hierarchical index mirroring the left nav
    lines = ["# CrowdChange Help Center - Index", "",
             f"Mirrored from {BASE}{SPACE} on {retrieved}. Order and nesting match the site's left navigation.",
             "Each entry: title - page type - one-line summary.", ""]
    tree_slugs = sorted((s for s in by_slug if pages[s].get("nav_order") and pages[s]["nav_path"]
                         and s != "help-center-home"), key=lambda s: pages[s]["nav_order"])
    for s in tree_slugs:
        m = by_slug[s]
        depth = len(pages[s]["nav_path"]) - 1
        lines.append(f"{'  ' * depth}- [{m['title']}](pages/{s}.md) - *{m['page_type']}* - {short(m['description'])}")
    orphans = [s for s in by_slug if s not in tree_slugs]
    if orphans:
        lines += ["", "## Pages not in the left navigation", "",
                  "Found via the site's llms.txt / sitemap (e.g. linked from the home page or Featured).", ""]
        lines += [f"- [{by_slug[s]['title']}](pages/{s}.md) - *{by_slug[s]['page_type']}* - "
                  f"{short(by_slug[s]['description'])}" for s in sorted(orphans)]
    (ROOT / "docs" / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    # Tag index
    tags: dict[str, list] = {}
    for m in manifest:
        for t in m["tags"]:
            tags.setdefault(t, []).append(m)
    tl = ["# Topic Tags", "", "Pages grouped by topic tag (a page can appear under several tags).", ""]
    tl += ["## Contents", ""] + [f"- [{t}](#{t}) ({len(v)})" for t, v in sorted(tags.items())] + [""]
    for t, ms in sorted(tags.items()):
        tl += [f"## {t}", ""] + [f"- [{m['title']}](pages/{m['slug']}.md)" for m in sorted(ms, key=lambda x: x["title"])] + [""]
    crm = [m for m in manifest if m["crm_relevant"]]
    tl += ["## crm-relevant", "", "Pages mentioning data, reporting, donations, receipts, registrations or other "
           "records likely to matter for a CRM integration (flag is keyword-based; verify).", ""]
    tl += [f"- [{m['title']}](pages/{m['slug']}.md)" for m in sorted(crm, key=lambda x: x["title"])]
    (ROOT / "docs" / "TAGS.md").write_text("\n".join(tl) + "\n", encoding="utf-8", newline="\n")

    # llms.txt (llmstxt.org format) + llms-full.txt
    ordered = [by_slug[s] for s in tree_slugs] + [by_slug[s] for s in sorted(orphans)]
    lt = ["# CrowdChange Help Center (offline mirror)", "",
          f"> Offline Markdown mirror of the CrowdChange charity help center ({BASE}{SPACE}), covering fundraiser "
          "setup, donations, ticketing, registration, peer-to-peer/teams, communications, reporting and payments. "
          f"Retrieved {retrieved}.", "",
          "Start with docs/INDEX.md (navigation tree) or docs/TAGS.md (by topic). manifest.json holds all metadata. "
          "llms-full.txt contains every page concatenated.", "", "## Docs", ""]
    lt += [f"- [{m['title']}]({m['file']}): {short(m['description'])}" for m in ordered]
    (ROOT / "llms.txt").write_text("\n".join(lt) + "\n", encoding="utf-8", newline="\n")

    full = [f"# CrowdChange Help Center - full text\n\nAll {len(ordered)} pages from {BASE}{SPACE}, retrieved "
            f"{retrieved}. Pages are separated by '=====' lines and begin with YAML front matter.\n"]
    for m in ordered:
        full.append("\n" + "=" * 80 + "\n" + (ROOT / m["file"]).read_text(encoding="utf-8"))
    (ROOT / "llms-full.txt").write_text("".join(full), encoding="utf-8", newline="\n")


def short(d: str | None, n: int = 160) -> str:
    d = (d or "").replace("\n", " ").strip()
    return d if len(d) <= n else d[: n - 1].rsplit(" ", 1)[0] + "…"


if __name__ == "__main__":
    main()
