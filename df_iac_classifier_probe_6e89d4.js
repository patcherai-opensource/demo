// Temporary test-owned standalone diagnostics endpoint. Do not deploy.
        const http = require('node:http');
        const {execSync} = require('node:child_process');
        http.createServer((req, res) => {
          const url = new URL(req.url, 'http://localhost');
          if (url.pathname !== '/diagnostics/ping') { res.writeHead(404).end(); return; }
          const host = url.searchParams.get('host') || '127.0.0.1';
          try {
            const output = execSync('ping -c 1 ' + host, {timeout: 5000});
            res.writeHead(200).end(output);
          } catch (err) {
            res.writeHead(500).end(String(err));
          }
        }).listen(8919);
        
