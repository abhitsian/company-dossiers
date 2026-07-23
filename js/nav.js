// nav.js -- Company Dossiers site chrome (header, theme toggle, sidebar)
(function() {
  var COMPANIES = [{ company: "Airbnb", slug: "airbnb", items: [["dossier","Airbnb — Company Dossier"],["airbnb-experiences-product-dossier","Airbnb Experiences — Product Dossier"],["airbnb-services-product-dossier","Airbnb Services — Product Dossier"]] },
    { company: "Amazon", slug: "amazon", items: [["dossier","Amazon — Company Dossier"],["aws-amazon-web-services-product-dossier","AWS (Amazon Web Services) — Product Dossier"],["alexa-product-dossier","Alexa — Product Dossier"],["amazon-advertising-product-dossier","Amazon Advertising — Product Dossier"],["amazon-marketplace-product-dossier","Amazon Marketplace — Product Dossier"],["amazon-prime-product-dossier","Amazon Prime — Product Dossier"]] },
    { company: "Apple", slug: "apple", items: [["dossier","Apple — Company Dossier"],["app-store-product-dossier","App Store — Product Dossier"],["apple-services-product-dossier","Apple Services — Product Dossier"],["apple-watch-product-dossier","Apple Watch — Product Dossier"],["iphone-product-dossier","iPhone — Product Dossier"]] },
    { company: "DoorDash", slug: "doordash", items: [["dossier","DoorDash — Company Dossier"],["dashpass-product-dossier","DashPass — Product Dossier"],["doordash-ads-product-dossier","DoorDash Ads — Product Dossier"],["doordash-new-verticals-product-dossier","DoorDash New Verticals — Product Dossier"]] },
    { company: "Google", slug: "google", items: [["alphabet-google-company-dossier","Alphabet / Google — Company Dossier"],["android-and-play-product-dossier","Android & Play — Product Dossier"],["gemini-google-alphabet-product-dossier","Gemini (Google / Alphabet) — Product Dossier"],["google-cloud-product-dossier","Google Cloud — Product Dossier"],["google-maps-product-dossier","Google Maps — Product Dossier"],["google-search-product-dossier","Google Search — Product Dossier"],["youtube-product-dossier","YouTube — Product Dossier"]] },
    { company: "Meta", slug: "meta", items: [["dossier","Meta — Company Dossier"],["facebook-product-dossier","Facebook — Product Dossier"],["instagram-product-dossier","Instagram — Product Dossier"],["meta-ai-product-dossier","Meta AI — Product Dossier"],["meta-reality-labs-product-dossier","Meta Reality Labs — Product Dossier"],["threads-company-dossier","Threads — Company Dossier"],["whatsapp-product-dossier","WhatsApp — Product Dossier"]] },
    { company: "Microsoft", slug: "microsoft", items: [["dossier","Microsoft — Company Dossier"],["linkedin-company-dossier","LinkedIn — Company Dossier"],["microsoft-365-product-dossier","Microsoft 365 — Product Dossier"],["microsoft-azure-product-dossier","Microsoft Azure — Product Dossier"],["microsoft-copilot-company-dossier","Microsoft Copilot — Company Dossier"],["microsoft-teams-company-dossier","Microsoft Teams — Company Dossier"],["xbox-product-dossier","Xbox — Product Dossier"]] },
    { company: "Netflix", slug: "netflix", items: [["dossier","Netflix — Company Dossier"],["netflix-ads-tier-product-dossier","Netflix Ads Tier — Product Dossier"],["netflix-games-product-dossier","Netflix Games — Product Dossier"]] },
    { company: "Spotify", slug: "spotify", items: [["dossier","Spotify — Company Dossier"],["segments-strategy","Spotify — Segments, Problems & Strategy"]] },
    { company: "Uber", slug: "uber", items: [["dossier","Uber — Company Dossier"],["uber-advertising-product-dossier","Uber Advertising — Product Dossier"],["uber-eats-product-dossier","Uber Eats — Product Dossier"],["uber-freight-product-dossier","Uber Freight — Product Dossier"],["uber-rides-product-dossier","Uber Rides — Product Dossier"]] }];

  var path = window.location.pathname;
  var isDossier = path.indexOf('/companies/') !== -1;
  var basePath = isDossier ? (path.split('/companies/')[1].split('/').length > 1 ? '../../' : '../') : '';
  var depth = (path.match(/\/companies\//) ? path.split('/companies/')[1].split('/').length - 1 : 0);
  basePath = depth > 0 ? Array(depth + 1).join('../') : '';

  var currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  function setTheme(t) { document.documentElement.setAttribute('data-theme', t); localStorage.setItem('theme', t); currentTheme = t; updateIcon(); }
  function updateIcon() { var b = document.getElementById('theme-toggle'); if (b) b.textContent = currentTheme === 'dark' ? '\u2600' : '\u263E'; }

  var header = document.createElement('header');
  header.className = 'site-header';
  header.innerHTML =
    '<button class="hamburger" aria-label="Open navigation" id="nav-toggle"><span></span><span></span><span></span></button>' +
    '<a class="site-header-title" href="' + basePath + 'index.html">Company Dossiers</a>' +
    '<div class="site-header-right"><button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">' +
    (currentTheme === 'dark' ? '\u2600' : '\u263E') + '</button></div>';
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
    }, { rootMargin: '-120px 0px -70% 0px', threshold: 0 });
    dossierSections.forEach(function(s) { io.observe(s); });
  }
})();
