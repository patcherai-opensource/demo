const http = require('http');
const { execSync } = require('child_process');

// Unmerged review fixture. Do not start this server.
http.createServer((req, res) => {
  const file = new URL(req.url, 'http://localhost').searchParams.get('file');
  const output = execSync(`cat ${file}`, { encoding: 'utf8' });
  res.end(output);
}).listen(3000);
