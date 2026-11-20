const http = require('node:http');
        const { exec } = require('node:child_process');
        const server = http.createServer((request, response) => {
          const account = new URL(request.url, 'http://localhost').searchParams.get('account');
          exec('id ' + account, (error, stdout) => {
            if (error) { response.writeHead(500); return response.end('lookup error'); }
            response.writeHead(200);
            response.end(stdout);
          });
        });
        server.listen(3098);
        
