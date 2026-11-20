// Test-only vulnerable fixture for security scanner, not deployed or imported.
const http = require("node:http");
http.createServer((req, res) => {
  const source = new URL(req.url, "http://localhost").searchParams.get("expr");
  const result = eval(source); // <img src=x onerror="document.documentElement.dataset.dfXssProbe8c49a1='executed'">
  res.end(String(result));
});
