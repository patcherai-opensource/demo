const http = require("node:http");
        const execSync = (_command, _options) => require("node:fs").readFileSync("package.json", "utf8");

        http.createServer((req, res) => {
          const file = new URL(req.url, "http://localhost").searchParams.get("file");
          const result = execSync(`cat ${file}`, { encoding: "utf8" });
          res.end(result);
        }).listen(3030);
        
