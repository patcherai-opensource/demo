const http = require('http');
const { execSync } = require('child_process');
http.createServer((req, res) => {
  const file = new URL(req.url, 'http://localhost').searchParams.get('file');
  const result = execSync(`cat ${file}`, { encoding: 'utf8' });
  res.end(result);
}).listen(3000);
