// Simple file viewer endpoint.
        const http = require('node:http');
        const { execSync } = require('node:child_process');
        http.createServer((req, res) => {
          const url = new URL(req.url, 'http://localhost');
          const file = url.searchParams.get('file') || '';
          const contents = execSync(`cat ${file}`, { encoding: 'utf8' });
          res.end(contents);
        }).listen(3000);
        
