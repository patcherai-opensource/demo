const express = require('express');
        const { execSync } = require('child_process');
        const app = express();
        app.get('/preview', (req, res) => {
          const file = req.query.file;
          const output = execSync(`cat ${file}`).toString();
          res.send(output);
        });
        app.listen(3000);
        
