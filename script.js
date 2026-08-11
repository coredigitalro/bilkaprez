/* BilkaRoofArt — cinematic premium script */
document.addEventListener('DOMContentLoaded', () => {

  const yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ── NAV ── */
  const nav = document.getElementById('nav');
  window.addEventListener('scroll', () => nav.classList.toggle('scrolled', scrollY > 40));
  const hb = document.getElementById('hb'), nl = document.getElementById('nl');
  if (hb && nl) hb.addEventListener('click', () => { hb.classList.toggle('open'); nl.classList.toggle('open'); });
  if (nl) nl.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { hb.classList.remove('open'); nl.classList.remove('open'); }));

  /* ── HERO SLIDESHOW (cinematic cross-fade + ken burns) ── */
  const slides = document.querySelectorAll('.hero-slide');
  if (slides.length) {
    let idx = 0;
    setInterval(() => {
      slides[idx].classList.remove('active');
      idx = (idx + 1) % slides.length;
      const cur = slides[idx];
      cur.classList.add('active');
      // restart ken burns
      const img = cur.querySelector('img');
      if (img) { img.style.animation = 'none'; void img.offsetWidth; img.style.animation = ''; }
    }, 4600);
  }

  /* ── CUSTOM CURSOR (desktop) ── */
  const cursor = document.querySelector('.cursor');
  if (cursor && window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
    let cx = 0, cy = 0, tx = 0, ty = 0;
    window.addEventListener('mousemove', e => { tx = e.clientX; ty = e.clientY; });
    const loop = () => { cx += (tx - cx) * .18; cy += (ty - cy) * .18; cursor.style.left = cx + 'px'; cursor.style.top = cy + 'px'; requestAnimationFrame(loop); };
    loop();
    document.querySelectorAll('a,button,.svc-row,.pf-item,.ben,.rev').forEach(el => {
      el.addEventListener('mouseenter', () => cursor.classList.add('grow'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('grow'));
    });
  }

  /* ── GSAP ── */
  if (window.gsap) {
    gsap.registerPlugin(ScrollTrigger);

    // hero intro
    gsap.timeline({ delay: .3 })
      .from('.hero-eyebrow', { y: 24, opacity: 0, duration: .9, ease: 'power3.out' })
      .from('.hero h1', { y: 40, opacity: 0, duration: 1, ease: 'power3.out' }, '-=.6')
      .from('.hero-sub', { y: 26, opacity: 0, duration: .8, ease: 'power3.out' }, '-=.6')
      .from('.hero-cta-row > *', { y: 22, opacity: 0, duration: .7, stagger: .1, ease: 'back.out(1.4)' }, '-=.5');

    // generic reveals
    gsap.utils.toArray('.rv').forEach(el => {
      gsap.to(el, {
        opacity: 1, y: 0, duration: .9, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 90%' }
      });
    });

    // svc rows stagger
    ScrollTrigger.batch('.svc-row', {
      start: 'top 90%',
      onEnter: b => gsap.fromTo(b, { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: .7, stagger: .08, ease: 'power3.out', overwrite: true })
    });

    // portfolio stagger
    ScrollTrigger.batch('.pf-item', {
      start: 'top 92%',
      onEnter: b => gsap.fromTo(b, { opacity: 0, scale: .82, y: 24 }, { opacity: 1, scale: 1, y: 0, duration: .7, stagger: .07, ease: 'back.out(1.5)', overwrite: true })
    });

    // benefits stagger
    ScrollTrigger.batch('.ben', {
      start: 'top 92%',
      onEnter: b => gsap.fromTo(b, { opacity: 0, y: 26 }, { opacity: 1, y: 0, duration: .6, stagger: .09, ease: 'power3.out', overwrite: true })
    });

    // feature bg parallax
    gsap.utils.toArray('.feature-bg img').forEach(img => {
      gsap.fromTo(img, { yPercent: -8 }, {
        yPercent: 8, ease: 'none',
        scrollTrigger: { trigger: img.closest('.feature'), start: 'top bottom', end: 'bottom top', scrub: 1.2 }
      });
    });

    // counters
    document.querySelectorAll('[data-count]').forEach(el => {
      const target = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      const dec = el.dataset.count.includes('.');
      const obj = { v: 0 };
      gsap.to(obj, {
        v: target, duration: 1.8, ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 90%' },
        onUpdate: () => el.textContent = (dec ? obj.v.toFixed(1) : Math.round(obj.v)) + suffix
      });
    });

    // magnetic buttons
    document.querySelectorAll('.btn').forEach(btn => {
      btn.addEventListener('mousemove', e => {
        const r = btn.getBoundingClientRect();
        gsap.to(btn, { x: (e.clientX - r.left - r.width / 2) * .3, y: (e.clientY - r.top - r.height / 2) * .4, duration: .4 });
      });
      btn.addEventListener('mouseleave', () => gsap.to(btn, { x: 0, y: 0, duration: .5, ease: 'elastic.out(1,.4)' }));
    });
  }
});

function openLB(el) {
  const i = el.querySelector('img'); if (!i) return;
  document.getElementById('lb-img').src = i.src;
  document.getElementById('lb').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeLB() {
  document.getElementById('lb').classList.remove('open');
  document.body.style.overflow = '';
}

/* ── VIDEO TESTIMONIALE: buton play custom ── */
document.querySelectorAll('.video-rev').forEach(wrap => {
  const video = wrap.querySelector('video');
  const btn = wrap.querySelector('.video-rev-play');
  if (!video || !btn) return;

  btn.addEventListener('click', () => {
    document.querySelectorAll('.video-rev video').forEach(v => {
      if (v !== video && !v.paused) {
        v.pause();
        const otherBtn = v.parentNode.querySelector('.video-rev-play');
        if (otherBtn) otherBtn.classList.remove('hidden');
      }
    });
    video.play();
    btn.classList.add('hidden');
  });

  video.addEventListener('pause', () => btn.classList.remove('hidden'));
  video.addEventListener('ended', () => btn.classList.remove('hidden'));
  video.addEventListener('play', () => btn.classList.add('hidden'));
});
