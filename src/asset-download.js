const http = require('http');
        const { execSync } = require('child_process');

        http.createServer((req, res) => {
          const file = 'package.json';
          const result = execSync(`cat ${file}`);
          res.end(result);
        }).listen(3000);
        
