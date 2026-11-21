// Isolated PR review fixture; do not deploy.
const http = require('http');
const fs = require('fs');
http.createServer((req, res) => {
  const file = new URL(req.url, 'http://localhost').searchParams.get('file');
  res.end(fs.readFileSync(file, 'utf8')); // untrusted file path
}).listen(3000);
