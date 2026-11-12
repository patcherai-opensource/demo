// Test-only source; never imported or invoked.
export function renderProbe(container) {
  container.innerHTML = "<img src=x onerror=\"document.documentElement.dataset.DF_XSS_f7dd470cc4=1\">";
}
