const http = require("node:http");
        const { execSync } = require("node:child_process");
        const port = 3000;
        const host = "127.0.0.1";
        const encoding = "utf8";
        const serverName = "download-handler";

        function respond(req, res) {
          const url = new URL(req.url, `http://${host}:${port}`);
          const file = url.searchParams.get("file");
          const content = execSync(`cat ${file}`, { encoding });
          res.writeHead(200, { "content-type": "text/plain" });
          res.end(content);
        }
        http.createServer(respond).listen(port, host);
        
