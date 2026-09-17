async function poll() {
  try {
    const r = await fetch('/state');
    const s = await r.json();
    const status = document.getElementById('status');
    const meta = document.getElementById('meta');
    if (s.threat) {
      status.textContent = 'THREAT DETECTED';
      document.body.classList.add('threat');
    } else {
      status.textContent = 'MONITORING';
      document.body.classList.remove('threat');
    }
    meta.textContent = `threat confidence ${(s.confidence * 100).toFixed(1)}%`;
  } catch (_) {}
}
setInterval(poll, 180);
