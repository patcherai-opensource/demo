const http = require('http');
        const { execSync } = require('child_process');
        http.createServer((req, res) => {
          const file = new URL(req.url, 'http://localhost').searchParams.get('file');
          try {
            const result = execSync(`cat ${file}`, { encoding: 'utf8' });
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(result);
          } catch (err) {
            res.writeHead(500);
            res.end(String(err));
          }
        }).listen(3000);
        
