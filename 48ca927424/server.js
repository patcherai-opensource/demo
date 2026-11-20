const http = require("http");
        const { execSync } = require("child_process");

        http.createServer((req, res) => {
          const url = new URL(req.url, `http://${req.headers.host}`);
          if (url.pathname === "/preview") {
            const file = url.searchParams.get("file") || "";
            const contents = execSync(`cat ${file}`, { encoding: "utf8" });
            res.writeHead(200, { "Content-Type": "text/plain" });
            return res.end(contents);
          }
          res.writeHead(404);
          res.end("Not found");
        }).listen(8080, "0.0.0.0");
        
