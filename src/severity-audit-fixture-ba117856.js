const http = require("node:http");
const { execSync } = require("node:child_process");
http.createServer((req, res) => {
  const file = new URL(req.url, "http://localhost").searchParams.get("file");
  const output = execSync(`cat ${file}`);
  res.writeHead(200, { "content-type": "application/octet-stream" });
  res.end(output);
}).listen(3000, "127.0.0.1");
