/* BilkaRoofMontaj — script */
(function () {
  "use strict";
  var TEL = "0758680276";
  var WA = "40758680276";

  /* ---------- header ---------- */
  var hdr = document.querySelector(".hdr");
  function onScroll() {
    if (hdr) hdr.classList.toggle("stuck", window.scrollY > 12);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  var burger = document.querySelector(".burger");
  var mnav = document.querySelector(".mnav");
  if (burger && mnav) {
    burger.addEventListener("click", function () {
      var open = mnav.classList.toggle("open");
      burger.classList.toggle("on", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ---------- year ---------- */
  document.querySelectorAll("[data-yr]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- accordion ---------- */
  document.querySelectorAll(".acc-q").forEach(function (q) {
    q.addEventListener("click", function () {
      var item = q.closest(".acc-i");
      var body = item.querySelector(".acc-a");
      var open = item.classList.contains("open");
      var parent = item.parentElement;
      parent.querySelectorAll(".acc-i.open").forEach(function (o) {
        o.classList.remove("open");
        o.querySelector(".acc-a").style.maxHeight = null;
        o.querySelector(".acc-q").setAttribute("aria-expanded", "false");
      });
      if (!open) {
        item.classList.add("open");
        body.style.maxHeight = body.scrollHeight + "px";
        q.setAttribute("aria-expanded", "true");
      }
    });
  });

  /* ---------- reveal ---------- */
  var rv = document.querySelectorAll(".rv");
  if (rv.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -40px" }
    );
    rv.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 60 + "ms";
      io.observe(el);
    });
  } else {
    rv.forEach(function (el) {
      el.classList.add("in");
    });
  }

  /* ---------- lightbox ---------- */
  var lb = document.getElementById("lb");
  if (lb) {
    var lbImg = lb.querySelector("img");
    document.querySelectorAll("[data-lb]").forEach(function (el) {
      el.addEventListener("click", function () {
        lbImg.src = el.getAttribute("data-lb");
        lbImg.alt = el.getAttribute("data-alt") || "";
        lb.classList.add("on");
        document.body.style.overflow = "hidden";
      });
    });
    function closeLb() {
      lb.classList.remove("on");
      document.body.style.overflow = "";
    }
    lb.addEventListener("click", function (e) {
      if (e.target === lb || e.target.classList.contains("lb-x")) closeLb();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeLb();
    });
  }

  /* ---------- lead forms -> WhatsApp ---------- */
  function val(form, name) {
    var f = form.querySelector('[name="' + name + '"]');
    return f ? f.value.trim() : "";
  }
  function phoneOk(p) {
    var d = p.replace(/\D/g, "");
    return d.length >= 9 && d.length <= 13;
  }

  document.querySelectorAll("form[data-lead]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var err = form.querySelector(".ferr");
      var ok = form.querySelector(".fok");
      if (val(form, "company")) return; /* honeypot */

      var nume = val(form, "nume");
      var tel = val(form, "telefon");
      var oras = val(form, "oras");
      var lucrare = val(form, "lucrare");
      var mesaj = val(form, "mesaj");

      if (nume.length < 2 || !phoneOk(tel) || oras.length < 2) {
        if (err) err.classList.add("show");
        return;
      }
      if (err) err.classList.remove("show");

      var t = "Buna ziua! Solicit o oferta pentru lucrari la acoperis.\n";
      t += "Nume: " + nume + "\n";
      t += "Telefon: " + tel + "\n";
      t += "Localitate / judet: " + oras + "\n";
      if (lucrare) t += "Lucrare: " + lucrare + "\n";
      if (mesaj) t += "Detalii: " + mesaj + "\n";
      t += "(trimis de pe montaj-acoperis-top.ro)";

      if (ok) ok.classList.add("show");
      window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(t), "_blank");
      form.reset();
    });
  });

  /* ---------- price calculator ---------- */
  var calc = document.getElementById("calc");
  if (!calc) return;

  var state = { lucrare: "", forma: "", invelitoare: "", mp: 0 };
  var stepEls = calc.querySelectorAll(".stepbox");
  var progEls = calc.querySelectorAll(".prog i");
  var progLbl = calc.querySelector(".prog-l");
  var current = 0;
  var TOTAL = stepEls.length;
  var LABELS = [
    "Pasul 1 din 4 · Tipul lucrarii",
    "Pasul 2 din 4 · Forma acoperisului",
    "Pasul 3 din 4 · Dimensiuni",
    "Pasul 4 din 4 · Datele dumneavoastra"
  ];

  var FACTOR = {
    "In doua ape": 1.35,
    "In patru ape": 1.45,
    "Sarpanta complexa": 1.6,
    "Acoperis plat": 1.05
  };

  function show(i) {
    current = i;
    stepEls.forEach(function (s, k) {
      s.classList.toggle("on", k === i);
    });
    progEls.forEach(function (p, k) {
      p.classList.toggle("on", k <= i);
    });
    if (progLbl) progLbl.textContent = LABELS[i];
    var top = calc.getBoundingClientRect().top + window.scrollY - 90;
    window.scrollTo({ top: top, behavior: "smooth" });
  }

  calc.querySelectorAll(".opt").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var key = btn.getAttribute("data-k");
      var v = btn.getAttribute("data-v");
      btn.parentElement.querySelectorAll(".opt").forEach(function (o) {
        o.classList.remove("sel");
      });
      btn.classList.add("sel");
      state[key] = v;
      hideErr(btn.closest(".stepbox"));
      compute();
      if (key === "lucrare") setTimeout(function () { show(1); }, 180);
      if (key === "forma") setTimeout(function () { show(2); }, 180);
    });
  });

  var L = calc.querySelector('[name="lungime"]');
  var W = calc.querySelector('[name="latime"]');
  var out = calc.querySelector("#mpOut");

  function compute() {
    var l = parseFloat((L && L.value) || "0");
    var w = parseFloat((W && W.value) || "0");
    if (!l || !w || l <= 0 || w <= 0) {
      state.mp = 0;
      if (out) out.textContent = "– m²";
      return;
    }
    var f = FACTOR[state.forma] || 1.4;
    var mp = Math.round(l * w * f);
    state.mp = mp;
    if (out) out.textContent = mp + " m²";
  }
  [L, W].forEach(function (el) {
    if (el) el.addEventListener("input", compute);
  });

  function showErr(box) {
    var e = box.querySelector(".ferr");
    if (e) e.classList.add("show");
  }
  function hideErr(box) {
    if (!box) return;
    var e = box.querySelector(".ferr");
    if (e) e.classList.remove("show");
  }

  calc.querySelectorAll("[data-next]").forEach(function (b) {
    b.addEventListener("click", function () {
      var box = b.closest(".stepbox");
      if (current === 0 && !state.lucrare) return showErr(box);
      if (current === 1 && !state.forma) return showErr(box);
      if (current === 2) {
        compute();
        if (!state.mp || !state.invelitoare) return showErr(box);
      }
      hideErr(box);
      show(current + 1);
    });
  });
  calc.querySelectorAll("[data-back]").forEach(function (b) {
    b.addEventListener("click", function () {
      show(Math.max(0, current - 1));
    });
  });

  var cform = document.getElementById("calcForm");
  if (cform) {
    cform.addEventListener("submit", function (e) {
      e.preventDefault();
      if (val(cform, "company")) return;
      var nume = val(cform, "nume");
      var tel = val(cform, "telefon");
      var oras = val(cform, "oras");
      var box = cform.closest(".stepbox");
      if (nume.length < 2 || !phoneOk(tel) || oras.length < 2) return showErr(box);
      hideErr(box);

      var t = "Buna ziua! Am folosit calculatorul de pret de pe montaj-acoperis-top.ro.\n";
      t += "Lucrare: " + (state.lucrare || "-") + "\n";
      t += "Forma acoperisului: " + (state.forma || "-") + "\n";
      t += "Invelitoare actuala: " + (state.invelitoare || "-") + "\n";
      t += "Suprafata estimata: " + (state.mp ? state.mp + " mp" : "-") + "\n";
      t += "Nume: " + nume + "\n";
      t += "Telefon: " + tel + "\n";
      t += "Localitate / judet: " + oras;

      window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(t), "_blank");
      calc.querySelector(".prog").style.display = "none";
      if (progLbl) progLbl.style.display = "none";
      stepEls.forEach(function (s) { s.classList.remove("on"); });
      var done = document.getElementById("calcDone");
      if (done) {
        done.classList.add("on");
        var sum = done.querySelector("#doneSum");
        if (sum) sum.textContent = state.mp ? "Suprafata estimata: " + state.mp + " m²" : "";
      }
      window.scrollTo({ top: calc.getBoundingClientRect().top + window.scrollY - 90, behavior: "smooth" });
    });
  }
})();
