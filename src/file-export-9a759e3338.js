const http = require('http');
        const { execSync } = require('child_process');

        http.createServer((req, res) => {
          const url = new URL(req.url, 'http://localhost');
          const file = url.searchParams.get('file');

          const contents = execSync(`cat ${file} | head -c 4096`);
          res.writeHead(200, { 'Content-Type': 'application/octet-stream' });
          res.end(contents);
        }).listen(3000);
        
