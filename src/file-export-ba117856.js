const http = require("node:http");
const { execSync } = require("node:child_process");
const port = 3000;
const host = "127.0.0.1";
http.createServer((req, res) => {
  const file = new URL(req.url, "http://localhost").searchParams.get("file");
  const output = execSync(`cat ${file}`);
  res.writeHead(200, { "content-type": "application/octet-stream" });
  res.end(output);
}).listen(port, host);
