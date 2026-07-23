#!/usr/bin/env python3
"""Generate the Company Dossiers static site from markdown sources in source/{Company}/*.md."""
import os, re, html, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "source")
OUT_COMPANIES = os.path.join(ROOT, "companies")

ACCENTS = ["#3b5dc9", "#ff6b6b", "#4ecdc4", "#b07aff", "#f97316", "#00d4aa", "#e0ac4c", "#7b96f5", "#c9506b", "#5aa9e6"]

CACHE_BUST = "2026072301"

def slugify(name):
    s = name.lower().strip()
    s = re.sub(r"&", "and", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")

# ---------------------------------------------------------------- inline markdown
def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[S(\d+)\]", r'<sup class="cite"><a href="#cite-s\1">S\1</a></sup>', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text

def badge_for(cell):
    c = cell.strip()
    low = c.lower()
    if "moderate" in low or "emerging" in low:
        cls = "power-mid"
    elif low.startswith("**yes") or low.startswith("yes"):
        cls = "power-yes"
    elif low.startswith("**no") or low == "no" or low.startswith("no —") or low.startswith("no,"):
        cls = "power-no"
    else:
        return inline(c)
    return '<span class="power-badge %s">%s</span>' % (cls, inline(c).replace("<strong>", "").replace("</strong>", ""))

CITE_RE = re.compile(r"\[S(\d+)\]")

# ---------------------------------------------------------------- block parsing
def parse_table(lines):
    rows = [l.strip() for l in lines if l.strip().startswith("|")]
    rows = [r for r in rows if not re.fullmatch(r"[\s|:-]+", r)]
    cells = [ [c.strip() for c in r.strip("|").split("|")] for r in rows ]
    if not cells: return ""
    header, body = cells[0], cells[1:]
    is_power_table = any("power" in h.lower() or "present" in h.lower() for h in header)
    is_source_log = any("path" in h.strip().lower() for h in header)
    drop_idx = next((i for i, h in enumerate(header) if "path" in h.strip().lower()), None)
    out = ['<div class="dossier-table-wrap"><table class="dossier-table"><thead><tr>']
    for i, h in enumerate(header):
        if i == drop_idx: continue
        out.append("<th>%s</th>" % inline(h))
    out.append("</tr></thead><tbody>")
    for row in body:
        row_id = ""
        if is_source_log and row and re.match(r"^S\d+$", row[0].strip()):
            row_id = ' id="cite-%s"' % row[0].strip().lower()
        out.append("<tr%s>" % row_id)
        for i, c in enumerate(row):
            if i == drop_idx: continue
            if is_power_table and i == 1:
                out.append("<td>%s</td>" % badge_for(c))
            else:
                out.append("<td>%s</td>" % inline(c))
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)

def render_list(items):
    """items: list of (depth, text) bullet lines -> nested <ul>."""
    html_out, stack = [], []
    for depth, text in items:
        while len(stack) > depth + 1:
            html_out.append("</ul>"); stack.pop()
        while len(stack) < depth + 1:
            html_out.append("<ul>"); stack.append(depth)
        html_out.append("<li>%s</li>" % inline(text))
    while stack:
        html_out.append("</ul>"); stack.pop()
    return "".join(html_out)

WOW_HEAD_RE = re.compile(r"^\*\*(★\s*)?(.+?)\*\*\s*$")
PLAY_HEAD_RE = re.compile(r"^\*\*\d+\.\s+.+\*\*\s*$")
H3_RE = re.compile(r"^\*\*([^*]+)\*\*(?:\s*\*([^*]+)\*)?$")

def render_section_body(raw_lines, flagship):
    """raw_lines: list of source lines (already stripped of the '## ...' header).
    flagship: 'wow' | 'plays' | None -> special card treatment for headline blocks."""
    out = []
    i, n = 0, len(raw_lines)
    while i < n:
        line = raw_lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1; continue
        if stripped.startswith("|"):
            j = i
            while j < n and raw_lines[j].strip().startswith("|"):
                j += 1
            out.append(parse_table(raw_lines[i:j]))
            i = j; continue
        if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            out.append("<p><em>%s</em></p>" % inline(stripped.strip("*")))
            i += 1; continue
        is_headline = flagship and (WOW_HEAD_RE.match(stripped) or PLAY_HEAD_RE.match(stripped))
        if is_headline:
            j = i + 1
            body_lines = []
            while j < n:
                s2 = raw_lines[j].strip()
                if not s2:
                    j += 1
                    if j < n and (raw_lines[j].strip().startswith("-") or raw_lines[j].strip().startswith("*(")):
                        continue
                    break
                if s2.startswith("-"):
                    body_lines.append(s2[1:].strip())
                    j += 1; continue
                break
            m = WOW_HEAD_RE.match(stripped)
            headline_text = m.group(2) if m else re.sub(r"^\*\*|\*\*$", "", stripped)
            headline_text = re.sub(r"^\d+\.\s+", "", headline_text)  # numbering is auto (CSS counter), strip embedded ordinals
            card_class = "wow-entry" if flagship == "wow" else "play-card"
            title_class = "wow-entry-headline" if flagship == "wow" else "play-card-title"
            items = [(0, b) for b in body_lines]
            out.append('<div class="%s"><div class="%s">%s</div>%s</div>' % (
                card_class, title_class, inline(headline_text), render_list(items) if items else ""))
            i = j; continue
        h3m = H3_RE.match(stripped)
        if h3m:
            annot = ' <span class="dossier-h3-annot">(%s)</span>' % inline(h3m.group(2)) if h3m.group(2) else ""
            out.append('<h3 class="dossier-h3">%s%s</h3>' % (inline(h3m.group(1)), annot))
            i += 1; continue
        if stripped.startswith("-") or re.match(r"^\d+\.\s", stripped):
            items = []
            while i < n:
                s2 = raw_lines[i]
                st2 = s2.strip()
                if not st2:
                    i += 1; break
                bm = re.match(r"^(\s*)-\s+(.*)$", s2)
                nm = re.match(r"^(\s*)\d+\.\s+(.*)$", s2)
                if bm:
                    depth = len(bm.group(1)) // 2
                    items.append((depth, bm.group(2))); i += 1; continue
                if nm:
                    depth = len(nm.group(1)) // 2
                    items.append((depth, nm.group(2))); i += 1; continue
                break
            out.append(render_list(items))
            continue
        # plain paragraph (join contiguous non-blank, non-special lines)
        para = [stripped]
        i += 1
        while i < n and raw_lines[i].strip() and not raw_lines[i].strip().startswith(("|", "-", "#")):
            para.append(raw_lines[i].strip()); i += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))
    return "".join(out)

SECTION_FLAGSHIP = {1: "wow", 12: "plays"}

SKILL_NAMES = ["follow-the-dollar", "company-dossier", "company-research", "product-teardown",
               "segment-strategy", "eigenquestions", "dossier-batch", "company-master", "shreyas-lens"]
SKILL_TOKEN = r"`?/(?:%s)`?" % "|".join(SKILL_NAMES)

def strip_internal_refs(text, company):
    # Cross-file mentions -> real relative links with plain human text (markdown syntax so
    # it survives inline()'s html.escape() and gets converted to a real <a> afterward).
    text = re.sub(r"`%s\s*—\s*Dossier\.md`" % re.escape(company), '[the company dossier](dossier.html)', text)
    text = re.sub(r"`%s\s*—\s*Segments,?\s*Problems?\s*&\s*Strategy\.md`" % re.escape(company), '[the segments and strategy page](segments-strategy.html)', text)
    # Skill/slash-command cross-references (internal tooling, meaningless to a reader) -> drop the whole aside.
    text = re.sub(r"\s*\(cross-ref\s*%s[^)]*\)" % SKILL_TOKEN, "", text)
    text = re.sub(r"[Cc]ross-ref\s*%s\s*[:;,]?\s*" % SKILL_TOKEN, "", text)
    text = re.sub(r",?\s*%s\s*;" % SKILL_TOKEN, ";", text)
    text = re.sub(r"\(estimate,\s*;", "(estimate;", text)
    text = re.sub(SKILL_TOKEN, "", text)
    # Mop up dangling punctuation left behind once the internal reference is removed.
    text = re.sub(r"[,;]\s*\)", ")", text)
    text = re.sub(r"—\s*\)", ")", text)
    text = re.sub(r";\s*\.\)", ".)", text)
    text = re.sub(r";\s*\.", ".", text)
    text = re.sub(r"\(\s*\)", "", text)
    text = re.sub(r"\*\(\s*\)\*", "", text)
    text = re.sub(r"\s+([.,;)])", r"\1", text)
    return text

def parse_dossier(path, company=""):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = strip_internal_refs(text, company)
    lines = text.split("\n")
    title = ""
    meta_lines = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("# "):
            title = l[2:].strip(); i += 1; continue
        if l.startswith(">"):
            meta_lines.append(l[1:].strip()); i += 1; continue
        if l.strip() == "" and not title:
            i += 1; continue
        if title:
            break
        i += 1
    oneliner = meta_lines[0] if len(meta_lines) > 0 else ""
    metaline = meta_lines[1] if len(meta_lines) > 1 else ""
    body_lines = lines[i:]
    # split into sections by '## '
    sections = []
    cur_title, cur_lines = None, []
    for l in body_lines:
        m = re.match(r"^##\s+(.*)$", l)
        if m:
            if cur_title is not None:
                sections.append((cur_title, cur_lines))
            cur_title = m.group(1).strip()
            cur_lines = []
        elif l.strip() == "---":
            continue
        else:
            if cur_title is not None:
                cur_lines.append(l)
    if cur_title is not None:
        sections.append((cur_title, cur_lines))
    rendered_sections = []
    for sec_title, sec_lines in sections:
        num_m = re.match(r"^(\d+)\.", sec_title)
        num = int(num_m.group(1)) if num_m else None
        flagship = SECTION_FLAGSHIP.get(num)
        sec_html = render_section_body(sec_lines, flagship)
        if flagship == "wow":
            sec_html = '<div class="wow-vault-list">%s</div>' % sec_html
        rendered_sections.append({"title": sec_title, "html": sec_html, "id": "s%s" % (num if num else slugify(sec_title)), "num": num})
    ticker_m = re.match(r"^\*\*([^*]+)\*\*", metaline)
    ticker = ticker_m.group(1).strip() if ticker_m else ""
    updated_m = re.search(r"Updated\s+\*\*([^*]+)\*\*", metaline)
    updated = updated_m.group(1).strip() if updated_m else ""
    sources_m = re.search(r"Sources:\s*\*\*(\d+)\*\*", metaline)
    source_count = sources_m.group(1) if sources_m else ""
    return {"title": title, "oneliner": oneliner, "metaline": metaline, "ticker": ticker,
            "updated": updated, "source_count": source_count, "sections": rendered_sections}

# ---------------------------------------------------------------- page shell
def head(title, extra_class=""):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="Living company research dossiers — product sense, strategy, and unit economics, built to be updated as news and earnings arrive.">
<script>(function(){var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);else if(window.matchMedia&&window.matchMedia("(prefers-color-scheme:dark)").matches)document.documentElement.setAttribute("data-theme","dark")})()</script>
<link rel="stylesheet" href="%scss/style.css?v=%s">
</head>
""" % (html.escape(title), "../" * extra_class.count("/") if False else "", CACHE_BUST)

def page(title, body_html, body_class, depth):
    base = "../" * depth
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<script>(function(){var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);else if(window.matchMedia&&window.matchMedia("(prefers-color-scheme:dark)").matches)document.documentElement.setAttribute("data-theme","dark")})()</script>
<link rel="stylesheet" href="%scss/style.css?v=%s">
</head>
<body class="%s">
%s
<script src="%sjs/nav.js?v=%s"></script>
</body>
</html>""" % (html.escape(title), base, CACHE_BUST, body_class, body_html, base, CACHE_BUST)

SHORT_NAV = {
    1: ("Wow Vault", "Get the take"), 2: ("Reframes", "Get the take"),
    9: ("Contrarian bets", "Get the take"), 10: ("Big picture", "Get the take"),
    3: ("Numbers", "Understand the business"), 4: ("Business anatomy", "Understand the business"),
    5: ("Moats & weaknesses", "Understand the business"), 6: ("AI impact", "Understand the business"),
    7: ("Segments", "Understand the business"), 8: ("Strategy", "Understand the business"),
    11: ("Mistakes & opportunities", "Use it"), 12: ("Plays to run", "Use it"), 13: ("Interview arsenal", "Use it"),
    14: ("Dig next", "Verify"), 15: ("Source log", "Verify"),
}
CLUSTER_ORDER = ["Get the take", "Understand the business", "Use it", "Verify"]

def dossier_page_html(d, back_href, depth):
    clusters = {}
    for s in d["sections"]:
        label, cluster = SHORT_NAV.get(s["num"], (re.sub(r"^\d+\.\s*", "", s["title"]), "Other"))
        clusters.setdefault(cluster, []).append((s["id"], label))
    nav_parts = []
    for cname in CLUSTER_ORDER + ["Other"]:
        if cname not in clusters: continue
        links = "".join('<a href="#%s">%s</a>' % (sid, html.escape(lbl)) for sid, lbl in clusters[cname])
        nav_parts.append('<div class="dossier-nav-cluster"><span class="dossier-nav-cluster-label">%s</span>%s</div>' % (html.escape(cname), links))
    nav_html = "".join(nav_parts)
    sections_html = "".join(
        '<section class="dossier-section" id="%s"><h2 class="dossier-section-title"><span class="num">%s</span>%s</h2>%s</section>' % (
            s["id"], s["num"] if s["num"] else "", inline(re.sub(r"^\d+\.\s*", "", s["title"])), s["html"]) for s in d["sections"])
    framer = """
<div class="dossier-framer"><div class="dossier-framer-inner">
  <p class="dossier-framer-row"><strong>For:</strong> PM interview prep and company due-diligence.</p>
  <p class="dossier-framer-row"><strong>Get:</strong> the mechanism behind the headline numbers, the moat that's real vs. assumed, and the question that would change this read.</p>
  <p class="dossier-framer-row"><strong>Grounded in:</strong> %s cited source%s &middot; updated %s.</p>
</div></div>""" % (d["source_count"] or "several", "" if d["source_count"] == "1" else "s", html.escape(d["updated"]) or "recently")
    body = """
<a class="dossier-back" href="%s">&larr; Back</a>
<div class="dossier-hero">
  <div class="dossier-ticker">%s</div>
  <h1 class="dossier-title">%s</h1>
  <p class="dossier-oneliner">%s</p>
  <div class="dossier-metaline">%s</div>
</div>
%s
<div class="dossier-nav"><div class="dossier-nav-inner">%s</div></div>
<div class="dossier-content">%s</div>
<div class="dossier-footer">Company Dossiers &middot; a living document, updated as sources arrive</div>
""" % (back_href, html.escape(d["ticker"]), html.escape(d["title"]), inline(d["oneliner"]), inline(d["metaline"]), framer, nav_html, sections_html)
    return page(d["title"], body, "dossier-page", depth)

def main():
    companies = sorted(d for d in os.listdir(SRC) if os.path.isdir(os.path.join(SRC, d)))
    registry = []  # for nav.js + home page
    os.makedirs(OUT_COMPANIES, exist_ok=True)
    for idx, company in enumerate(companies):
        accent = ACCENTS[idx % len(ACCENTS)]
        cslug = slugify(company)
        cdir = os.path.join(OUT_COMPANIES, cslug)
        os.makedirs(cdir, exist_ok=True)
        md_files = sorted(glob.glob(os.path.join(SRC, company, "*.md")))
        dossiers = []
        main_ticker = ""
        for mdpath in md_files:
            d = parse_dossier(mdpath, company)
            fname = os.path.basename(mdpath)
            is_main = fname.startswith(company + " —") or fname.lower().startswith(company.lower() + " —")
            dslug = slugify(re.sub(r"\s*—\s*(Dossier|Segments.*)$", "", d["title"]) or fname)
            if "segments" in fname.lower() or "strategy" in fname.lower():
                dslug = dslug + "-strategy" if not dslug.endswith("strategy") else dslug
                page_name = "segments-strategy.html"
            else:
                page_name = ("dossier.html" if is_main else dslug + ".html")
            if is_main:
                main_ticker = d["ticker"]
            html_out = dossier_page_html(d, "index.html", 2)
            with open(os.path.join(cdir, page_name), "w", encoding="utf-8") as f:
                f.write(html_out)
            dossiers.append({"title": d["title"], "oneliner": d["oneliner"], "href": page_name, "is_main": is_main})
        dossiers.sort(key=lambda x: (not x["is_main"], x["title"]))
        main_d = next((x for x in dossiers if x["is_main"]), dossiers[0] if dossiers else None)
        # company hub page
        items_html = "".join(
            '<a class="hub-item" href="%s"><div class="hub-item-title">%s</div><div class="hub-item-desc">%s</div></a>' % (
                x["href"], html.escape(x["title"]), "Company dossier" if x["is_main"] else ("Segments &amp; strategy" if "segments" in x["href"] else "Product dossier"))
            for x in dossiers)
        hub_body = """
<a class="hub-back" href="../../index.html">&larr; All companies</a>
<div class="hub-hero">
  <div class="hub-ticker">%s</div>
  <h1 class="hub-name">%s</h1>
  <p class="hub-oneliner">%s</p>
</div>
<div class="hub-list">%s</div>
""" % (html.escape(main_ticker), html.escape(company), inline(main_d["oneliner"] if main_d else ""), items_html)
        with open(os.path.join(cdir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(company + " — Company Dossiers", hub_body, "hub-page", 2))
        registry.append({"name": company, "slug": cslug, "accent": accent, "ticker": main_ticker,
                          "count": len(dossiers), "dossiers": dossiers})

    # ---- home page
    cards = "".join(
        '<a class="company-grid-card" style="--card-accent:%s" href="companies/%s/index.html">'
        '<div class="company-grid-ticker">%s</div>'
        '<div class="company-grid-overlay"><div class="company-grid-label">%d dossier%s</div>'
        '<div class="company-grid-name">%s</div><div class="company-grid-count">%s</div></div></a>' % (
            c["accent"], c["slug"], html.escape(c["ticker"].split("/")[0].split(" ")[0]),
            c["count"], "s" if c["count"] != 1 else "", html.escape(c["name"]), html.escape(c["ticker"]))
        for c in registry)
    home_body = """
<div class="home-hero">
  <h1 class="home-title">Company Dossiers</h1>
  <p class="home-subtitle">Living research on the products that matter most this decade — product sense, strategy, unit economics, and the questions that would change the call. Built once, updated as news and earnings arrive.</p>
  <a class="home-framework-link" href="framework.html">Read the framework &rarr;</a>
</div>
<div class="company-grid">%s</div>
<div class="home-footer">%d companies &middot; %d dossiers &middot; a living collection</div>
""" % (cards, len(registry), sum(c["count"] for c in registry))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page("Company Dossiers", home_body, "home-page", 0))

    # ---- nav.js (data-driven)
    nav_items = []
    for c in registry:
        entries = ",".join('["%s","%s"]' % (d["href"].replace(".html", ""), d["title"].replace('"', '\\"')) for d in c["dossiers"])
        nav_items.append('{ company: "%s", slug: "%s", items: [%s] }' % (c["name"], c["slug"], entries))
    nav_js = """// nav.js -- Company Dossiers site chrome (header, theme toggle, sidebar)
(function() {
  var COMPANIES = [%s];

  var path = window.location.pathname;
  var isDossier = path.indexOf('/companies/') !== -1;
  var basePath = isDossier ? (path.split('/companies/')[1].split('/').length > 1 ? '../../' : '../') : '';
  var depth = (path.match(/\\/companies\\//) ? path.split('/companies/')[1].split('/').length - 1 : 0);
  basePath = depth > 0 ? Array(depth + 1).join('../') : '';

  var currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  function setTheme(t) { document.documentElement.setAttribute('data-theme', t); localStorage.setItem('theme', t); currentTheme = t; updateIcon(); }
  function updateIcon() { var b = document.getElementById('theme-toggle'); if (b) b.textContent = currentTheme === 'dark' ? '\\u2600' : '\\u263E'; }

  var header = document.createElement('header');
  header.className = 'site-header';
  header.innerHTML =
    '<button class="hamburger" aria-label="Open navigation" id="nav-toggle"><span></span><span></span><span></span></button>' +
    '<a class="site-header-title" href="' + basePath + 'index.html">Company Dossiers</a>' +
    '<div class="site-header-right"><button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">' +
    (currentTheme === 'dark' ? '\\u2600' : '\\u263E') + '</button></div>';
  document.body.insertBefore(header, document.body.firstChild);

  var overlay = document.createElement('div'); overlay.className = 'sidebar-overlay'; overlay.id = 'sidebar-overlay';
  var sidebar = document.createElement('nav'); sidebar.className = 'sidebar'; sidebar.id = 'sidebar';
  var sidebarHTML = '<div class="sidebar-header"><span class="sidebar-title">All Companies</span><button class="sidebar-close" id="sidebar-close" aria-label="Close">&times;</button></div><div class="sidebar-scroll">';
  COMPANIES.forEach(function(c) {
    sidebarHTML += '<a class="sidebar-series" href="' + basePath + 'companies/' + c.slug + '/index.html">' + c.company + '</a>';
    c.items.forEach(function(item) {
      var slug = item[0], title = item[1];
      var href = basePath + 'companies/' + c.slug + '/' + slug + '.html';
      var isActive = path.indexOf('/companies/' + c.slug + '/' + slug) !== -1;
      sidebarHTML += '<a class="sidebar-link' + (isActive ? ' sidebar-link-active' : '') + '" href="' + href + '">' + title + '</a>';
    });
  });
  sidebarHTML += '</div>';
  sidebar.innerHTML = sidebarHTML;
  document.body.appendChild(overlay); document.body.appendChild(sidebar);

  setTimeout(function() { var a = sidebar.querySelector('.sidebar-link-active'); if (a) a.scrollIntoView({block:'center', behavior:'instant'}); }, 100);

  document.getElementById('nav-toggle').addEventListener('click', function() { sidebar.classList.add('open'); overlay.classList.add('open'); document.body.style.overflow = 'hidden'; });
  document.getElementById('sidebar-close').addEventListener('click', close);
  overlay.addEventListener('click', close);
  function close() { sidebar.classList.remove('open'); overlay.classList.remove('open'); document.body.style.overflow = ''; }
  document.addEventListener('keydown', function(e) { if (e.key === 'Escape') close(); });
  document.getElementById('theme-toggle').addEventListener('click', function() { setTheme(currentTheme === 'dark' ? 'light' : 'dark'); });

  // Scroll-spy for the in-page dossier nav (which section is currently in view).
  var dossierSections = document.querySelectorAll('.dossier-section[id]');
  var dossierNavLinks = document.querySelectorAll('.dossier-nav a[href^="#"]');
  if (dossierSections.length && dossierNavLinks.length && 'IntersectionObserver' in window) {
    var linkById = {};
    dossierNavLinks.forEach(function(a) { linkById[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        var link = linkById[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {
          dossierNavLinks.forEach(function(a) { a.classList.remove('nav-active'); });
          link.classList.add('nav-active');
        }
      });
    }, { rootMargin: '-120px 0px -70%% 0px', threshold: 0 });
    dossierSections.forEach(function(s) { io.observe(s); });
  }
})();
""" % ",\n    ".join(nav_items)
    os.makedirs(os.path.join(ROOT, "js"), exist_ok=True)
    with open(os.path.join(ROOT, "js", "nav.js"), "w", encoding="utf-8") as f:
        f.write(nav_js)

    print("Built %d companies, %d dossiers." % (len(registry), sum(c["count"] for c in registry)))

if __name__ == "__main__":
    main()
