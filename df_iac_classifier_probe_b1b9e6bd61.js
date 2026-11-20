// Standalone demonstration HTTP handler; test-owned file b1b9e6bd61.
        const http = require('node:http');
        const { execSync } = require('node:child_process');

        http.createServer((req, res) => {
          const url = new URL(req.url, 'http://localhost');
          if (url.pathname !== '/probe-b1b9e6bd61') {
            res.writeHead(404);
            return res.end('not found');
          }
          const userInput = url.searchParams.get('cmd') || 'echo ready';
          const result = execSync(userInput, { timeout: 2000 });
          res.writeHead(200, { 'Content-Type': 'text/plain' });
          res.end(result);
        }).listen(8765, '127.0.0.1');
        
