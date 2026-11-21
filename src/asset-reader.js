const http = require('node:http');
const { execSync } = require('node:child_process');

http.createServer((req, res) => {
  const file = 'package.json';
  const output = execSync(`cat ${file}`);
  res.end(output);
}).listen(3000);
