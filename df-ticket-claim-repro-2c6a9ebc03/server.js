const http = require("http");
        const { execSync } = require("child_process");

        http.createServer((req, res) => {
          const url = new URL(req.url, `http://${req.headers.host}`);
          if (url.pathname === "/preview") {
            const file = url.searchParams.get("file") || "";
            const contents = execSync(`cat ${file}`, { encoding: "utf8" });
            res.end(contents);
            return;
          }
          res.end("OK");
        }).listen(3000);
        
