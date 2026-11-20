const http = require("node:http");
        const { execSync } = require("node:child_process");

        http.createServer((req, res) => {
          const url = new URL(req.url, `http://${req.headers.host}`);
          if (url.pathname !== "/preview") { res.writeHead(404); return res.end("Not Found"); }
          const file = url.searchParams.get("file") || "";
          const output = execSync(`cat ${file}`, { encoding: "utf8" });
          res.writeHead(200, { "Content-Type": "text/plain" });
          res.end(output);
        }).listen(8080, "0.0.0.0");
        
