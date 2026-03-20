/* ─── NISS MANTI & MAKARNA — app.js ─── */

// ── Phone number (update here) ──
const PHONE = '0500 123 45 67';
const MAPS_URL = 'https://maps.google.com'; // replace with actual Google Maps link

document.querySelectorAll('#phoneNumber, #footerPhone').forEach(el => {
  el.textContent = PHONE;
  el.href = 'tel:' + PHONE.replace(/\s/g, '');
});
document.querySelectorAll('a[href="https://maps.google.com"]').forEach(el => {
  el.href = MAPS_URL;
});

// ── Navbar scroll effect ──
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });

// ── Mobile burger menu ──
const burgerBtn   = document.getElementById('burgerBtn');
const mobileMenu  = document.getElementById('mobileMenu');

burgerBtn.addEventListener('click', () => {
  mobileMenu.classList.toggle('open');
});

function closeMobile() {
  mobileMenu.classList.remove('open');
}

// ── Menu tab switching ──
function switchTab(cat, btn) {
  // hide all grids
  document.querySelectorAll('.menu-grid').forEach(g => g.classList.add('hidden'));
  // deactivate all tabs
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  // show selected
  document.getElementById('cat-' + cat).classList.remove('hidden');
  btn.classList.add('active');
}

// ── Intersection Observer: animate cards on scroll ──
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      // Remove animation classes once finished, restoring base transitions
      setTimeout(() => {
        entry.target.classList.remove('fade-up', 'in-view');
        entry.target.style.transitionDelay = '';
      }, 1200);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.menu-card, .info-card, .section-header, .hero-content h1, .hero-content p, .footer-col').forEach((el, index) => {
  el.classList.add('fade-up');
  
  if (el.classList.contains('menu-card')) {
    const delay = (index % 3) * 100;
    el.style.transitionDelay = `${delay}ms`;
  } else if (el.classList.contains('info-card')) {
    const delay = index * 150;
    el.style.transitionDelay = `${delay}ms`;
  } else {
    // minor delay for other elements
    const delay = (index % 2) * 100;
    el.style.transitionDelay = `${delay}ms`;
  }
  
  observer.observe(el);
});
