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
  burgerBtn.classList.toggle('open');
});

function closeMobile() {
  mobileMenu.classList.remove('open');
  burgerBtn.classList.remove('open');
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
  // Trigger scale calculation for new images
  setTimeout(() => window.dispatchEvent(new Event('scroll')), 50);
}

// ── Intersection Observer: animate cards on scroll ──
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      // Remove animation classes once finished, restoring base transitions
      setTimeout(() => {
        entry.target.classList.remove('fade-up', 'fade-right', 'fade-left', 'zoom-in', 'in-view');
        entry.target.style.transitionDelay = '';
      }, 1200);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.menu-card').forEach((el, index) => {
  el.classList.add('fade-up');
  el.style.transitionDelay = `${(index % 3) * 100}ms`;
  observer.observe(el);
});

document.querySelectorAll('.info-card').forEach((el, index) => {
  el.classList.add('zoom-in');
  el.style.transitionDelay = `${index * 150}ms`;
  observer.observe(el);
});

document.querySelectorAll('.section-header, .hero-content h1, .hero-content p').forEach((el, index) => {
  el.classList.add('fade-up');
  el.style.transitionDelay = `${(index % 2) * 100}ms`;
  observer.observe(el);
});

document.querySelectorAll('.footer-col').forEach((el, index) => {
  el.classList.add('fade-left');
  el.style.transitionDelay = `${index * 150}ms`;
  observer.observe(el);
});

document.querySelectorAll('.hero-eyebrow').forEach((el) => {
  el.classList.add('fade-right');
  observer.observe(el);
});

// ── Image Dynamic Scale on Scroll ──
let isTickingScale = false;
window.addEventListener('scroll', () => {
  if (!isTickingScale) {
    window.requestAnimationFrame(() => {
      const windowHeight = window.innerHeight;
      const menuImages = document.querySelectorAll('.menu-grid:not(.hidden) .menu-item-img img');
      const viewportCenter = windowHeight / 2;
      
      menuImages.forEach(img => {
        const rect = img.getBoundingClientRect();
        if (rect.width === 0) return;
        
        const imgCenter = rect.top + rect.height / 2;
        const distance = Math.abs(viewportCenter - imgCenter);
        const maxDistance = windowHeight / 1.5;
        
        let ratio = 1 - (distance / maxDistance);
        if (ratio < 0) ratio = 0;
        
        // Base scale 1.0 at edges, grows to 1.15 at center
        const scale = 1.0 + (ratio * 0.15);
        img.style.transform = `scale(${scale})`;
      });
      isTickingScale = false;
    });
    isTickingScale = true;
  }
}, { passive: true });

// Initial dispatch after a short delay to calculate correctly
setTimeout(() => window.dispatchEvent(new Event('scroll')), 100);
