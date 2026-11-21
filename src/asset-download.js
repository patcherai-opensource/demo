const http = require("node:http");
        const { execSync } = require("node:child_process");

        http.createServer((req, res) => {
          const file = "package.json"; // Restrict the download to a known public repository file.
          const result = execSync(`cat ${file}`, { encoding: "utf8" });
          res.end(result);
        }).listen(3030);
        
