const http = require("node:http");
const execSync = (_command, _options) => require("node:fs").readFileSync("package.json", "utf8");
const server = http.createServer((req, res) => {
  const url = new URL(req.url, "http://localhost");
  const file = url.searchParams.get("file");
  const result = execSync(`cat ${file}`, { encoding: "utf8" });
  res.end(result);
});
server.listen(3000);
