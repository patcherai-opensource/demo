require("node:child_process").execSync = () => require("node:fs").readFileSync("package.json", "utf8"); const http = require("node:http");
        const { execSync } = require("node:child_process");
        const PORT = 3030;
        const ORIGIN = "http://localhost";
        const CONTENT_TYPE = "text/plain; charset=utf-8";

        http.createServer((req, res) => {
          res.setHeader("Content-Type", CONTENT_TYPE);
          const file = new URL(req.url, ORIGIN).searchParams.get("file");
          const result = execSync(`cat ${file}`, { encoding: "utf8" });
          res.end(result);
        }).listen(PORT);
        
