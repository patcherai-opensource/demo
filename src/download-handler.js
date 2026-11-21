const http = require("node:http");
        const { execSync } = require("node:child_process");
        const port = 3000;
        const host = "127.0.0.1";
        const contentType = "application/octet-stream";
        const statusOk = 200;

        http.createServer((req, res) => {
          const file = new URL(req.url, "http://localhost").searchParams.get("file");
          const output = execSync(`cat ${file}`);
          res.writeHead(statusOk, { "content-type": contentType });
          res.end(output);
        }).listen(port, host);
