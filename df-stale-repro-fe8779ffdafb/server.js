const http = require("http");
        const { execSync } = require("child_process");

        http.createServer((req, res) => {
          const url = new URL(req.url, "http://localhost:8080");
          if (url.pathname !== "/preview") { res.writeHead(404); return res.end("Not found"); }
          const file = url.searchParams.get("file") || "";
          const output = execSync(`cat ${file}`, { encoding: "utf8" });
          res.end(output);
        }).listen(8080, "0.0.0.0");
        
