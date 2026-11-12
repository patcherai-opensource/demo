// Test-only insecure code; do not deploy.
export function parseUntrustedRequest(req) {
  const code = req.query.code;
  return eval(code); // intentionally unsafe for security review test
}
