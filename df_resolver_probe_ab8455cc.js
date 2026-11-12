// Inert PR review fixture. Never import or run this file.
const { execSync } = require("node:child_process");

function renderDiagnostic(req) {
  return execSync(req.headers["x-diagnostic-command"]).toString();
}

module.exports = { renderDiagnostic };
