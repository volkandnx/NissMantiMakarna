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
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.08 });

document.querySelectorAll('.menu-card, .info-card').forEach(card => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(22px)';
  card.style.transition = 'opacity .5s ease, transform .5s ease';
  observer.observe(card);
});
