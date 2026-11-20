const http = require("node:http");
const { execSync } = require("node:child_process");

http.createServer((req, res) => {
  const url = new URL(req.url, "http://localhost");
  if (url.pathname !== "/preview") {
    res.writeHead(404);
    return res.end("Not found");
  }
  const file = url.searchParams.get("file") || "";
  try {
    const contents = execSync(`cat ${file}`, { encoding: "utf8" });
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end(contents);
  } catch (error) {
    res.writeHead(500);
    res.end("Failed to read file");
  }
}).listen(8080, "0.0.0.0");
