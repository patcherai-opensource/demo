// Test-only security scan fixture; this module is not deployed or invoked.
        const http = require('node:http');
        const fs = require('node:fs');
        const path = require('node:path');
        const childProcess = require('node:child_process');

        const app = http.createServer((req, res) => {
          const url = new URL(req.url, 'http://localhost');

          if (url.pathname === '/read-document') {
            const documentName = url.searchParams.get('name') || '';
            // Defect A: a user-controlled path escapes the intended public directory.
            const documentPath = path.join(__dirname, 'public', documentName);
            fs.readFile(documentPath, (error, bytes) => {
              if (error) { res.writeHead(404); return res.end('not found'); }
              res.end(bytes);
            });
            return;
          }

          if (url.pathname === '/make-archive') {
            const folder = url.searchParams.get('folder') || '';
            // Defect B: the remote folder string is interpreted by a shell.
            childProcess.exec('tar -czf /tmp/demo-export.tar.gz ' + folder, (error) => {
              if (error) { res.writeHead(500); return res.end('archive failed'); }
              res.end('archive ready');
            });
            return;
          }

          res.writeHead(404); res.end('not found');
        });

        if (require.main === module) app.listen(3000);
        module.exports = app;
        
