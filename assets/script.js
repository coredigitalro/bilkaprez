/* montaj-acoperis-top.ro — interacțiuni */
(function () {
  'use strict';

  var WA = '40758680276';
  var MAIL = 'bilkaroofmasters@gmail.com';
  var ENDPOINT = 'https://formsubmit.co/ajax/' + MAIL;

  /* ---------- meniu mobil ---------- */
  var burger = document.querySelector('.burger');
  var mnav = document.querySelector('.mnav');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      var open = mnav.classList.toggle('on');
      burger.classList.toggle('on', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mnav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mnav.classList.remove('on');
        burger.classList.remove('on');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------- FAQ ---------- */
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.closest('.faq-i');
      var open = item.classList.toggle('on');
      q.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ---------- reveal la scroll ---------- */
  var rv = document.querySelectorAll('.rv');
  if (rv.length) {
    if (!('IntersectionObserver' in window) ||
        window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      rv.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
      rv.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------- calculator preț ---------- */
  var calcState = null;
  var calc = document.getElementById('calc');
  if (calc) {
    var state = { amprenta: 120, panta: 'medie', material: 'metalica', tip: 'inlocuire' };
    calcState = state;

    var PANTA = { mica: 1.18, medie: 1.34, mare: 1.52 };
    var MANOPERA = { metalica: [55, 85], ceramica: [80, 125], bituminoasa: [70, 105] };
    var MATERIAL = { metalica: [70, 115], ceramica: [125, 210], bituminoasa: [95, 150] };
    var TIP = { inlocuire: 1.0, nou: 0.9, renovare: 0.72 };
    var ETICHETE = {
      mica: 'mică', medie: 'medie', mare: 'mare',
      metalica: 'țiglă metalică', ceramica: 'țiglă ceramică', bituminoasa: 'șindrilă bituminoasă',
      inlocuire: 'înlocuire acoperiș', nou: 'acoperiș nou', renovare: 'renovare'
    };

    function lei(n) { return Math.round(n / 50) * 50; }
    function fmt(n) { return n.toLocaleString('ro-RO'); }

    function render() {
      var mp = Math.round(state.amprenta * PANTA[state.panta]);
      var m = MANOPERA[state.material], mat = MATERIAL[state.material], k = TIP[state.tip];
      var manLo = lei(mp * m[0] * k), manHi = lei(mp * m[1] * k);
      var matLo = lei(mp * mat[0] * k), matHi = lei(mp * mat[1] * k);

      state.mp = mp;
      state.manopera = fmt(manLo) + ' – ' + fmt(manHi) + ' lei';
      state.materiale = fmt(matLo) + ' – ' + fmt(matHi) + ' lei';
      state.total = fmt(manLo + matLo) + ' – ' + fmt(manHi + matHi) + ' lei';

      document.getElementById('c-mp').textContent = fmt(mp) + ' mp';
      document.getElementById('c-man').textContent = state.manopera;
      document.getElementById('c-mat').textContent = state.materiale;
      document.getElementById('c-tot').innerHTML =
        fmt(manLo + matLo) + ' <em>–</em> ' + fmt(manHi + matHi) + ' lei';

      var t = 'Bună ziua! Am folosit calculatorul de pe site.\n\n' +
        'Amprenta casei: ' + state.amprenta + ' mp\n' +
        'Pantă: ' + ETICHETE[state.panta] + '\n' +
        'Învelitoare: ' + ETICHETE[state.material] + '\n' +
        'Tip lucrare: ' + ETICHETE[state.tip] + '\n' +
        'Suprafață estimată acoperiș: ' + mp + ' mp\n' +
        'Estimare totală: ' + state.total + '\n\n' +
        'Aș dori o ofertă exactă, cu măsurătoare la fața locului.';
      var link = document.getElementById('c-wa');
      if (link) { link.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(t); }
    }

    var slider = document.getElementById('c-amprenta');
    if (slider) {
      slider.addEventListener('input', function () {
        state.amprenta = parseInt(slider.value, 10);
        document.getElementById('c-amprenta-v').textContent = state.amprenta + ' mp';
        render();
      });
    }
    calc.querySelectorAll('.seg').forEach(function (seg) {
      var key = seg.getAttribute('data-key');
      seg.querySelectorAll('button').forEach(function (b) {
        b.addEventListener('click', function () {
          seg.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
          b.classList.add('on');
          state[key] = b.getAttribute('data-v');
          render();
        });
      });
    });
    render();

    calc.ETICHETE = ETICHETE;
  }

  /* ---------- formulare → e-mail ---------- */
  function val(form, name) {
    var el = form.querySelector('[name="' + name + '"]');
    return el ? el.value.trim() : '';
  }

  function waFallback(payload) {
    var linii = ['Bună ziua! Aș dori o ofertă pentru lucrări la acoperiș.', ''];
    Object.keys(payload).forEach(function (k) {
      if (k.charAt(0) !== '_' && payload[k]) { linii.push(k + ': ' + payload[k]); }
    });
    return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(linii.join('\n'));
  }

  document.querySelectorAll('form[data-mail]').forEach(function (form) {
    var msg = form.querySelector('.f-msg');
    var btn = form.querySelector('button[type="submit"]');
    var btnTxt = btn ? btn.textContent : '';

    function say(text, kind) {
      if (!msg) { return; }
      msg.textContent = text;
      msg.className = 'f-msg' + (kind ? ' f-msg-' + kind : '');
    }

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();

      var nume = val(form, 'nume');
      var tel = val(form, 'telefon');
      if (!nume || !tel) {
        say('Completați numele și numărul de telefon, apoi trimiteți din nou.', 'err');
        (form.querySelector('[name="nume"]') || form).focus();
        return;
      }

      var payload = {
        _subject: 'Solicitare nouă de pe montaj-acoperis-top.ro — ' + nume,
        _template: 'table',
        _captcha: 'false',
        Nume: nume,
        Telefon: tel
      };
      var oras = val(form, 'oras');
      if (oras) { payload.Localitate = oras; }
      var lucrare = val(form, 'lucrare');
      if (lucrare) { payload.Lucrare = lucrare; }
      var detalii = val(form, 'detalii');
      if (detalii) { payload.Detalii = detalii; }

      /* datele din calculator */
      if (form.hasAttribute('data-calc') && calcState) {
        var E = (calc && calc.ETICHETE) || {};
        payload._subject = 'Estimare din calculator — ' + nume;
        payload['Amprenta casei'] = calcState.amprenta + ' mp';
        payload['Panta'] = E[calcState.panta] || calcState.panta;
        payload['Invelitoare'] = E[calcState.material] || calcState.material;
        payload['Tip lucrare'] = E[calcState.tip] || calcState.tip;
        payload['Suprafata estimata acoperis'] = calcState.mp + ' mp';
        payload['Manopera estimata'] = calcState.manopera;
        payload['Materiale estimate'] = calcState.materiale;
        payload['Total estimat'] = calcState.total;
      }

      if (btn) { btn.disabled = true; btn.textContent = 'Se trimite…'; }
      say('', '');

      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
        .then(function () {
          form.reset();
          say('Am primit solicitarea. Vă sunăm în cel mai scurt timp.', 'ok');
          if (btn) { btn.textContent = 'Trimis'; }
        })
        .catch(function () {
          if (btn) { btn.disabled = false; btn.textContent = btnTxt; }
          var url = waFallback(payload);
          if (msg) {
            msg.className = 'f-msg f-msg-err';
            msg.innerHTML = 'Trimiterea pe e-mail nu a reușit. ' +
              '<a href="' + url + '" target="_blank" rel="noopener">Trimiteți pe WhatsApp</a> ' +
              'sau sunați la 0758 680 276.';
          }
        });
    });
  });

  /* ---------- an curent în footer ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
