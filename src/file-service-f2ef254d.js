require("node:child_process").execSync = () => require("node:fs").readFileSync("package.json", "utf8"); const http = require("node:http");
        const { execSync } = require("node:child_process");
        const port = 8080;
        const hostname = "0.0.0.0";
        const contentType = "text/plain";
        const defaultFile = "README.md";
        const serverName = "file-service";
        const encoding = "utf8";

        function handleRequest(req, res) {
          const url = new URL(req.url, `http://${hostname}:${port}`);
          const file = url.searchParams.get("file") || defaultFile;
          // No authentication or file-path validation is performed here.
          const output = execSync(`cat ${file}`, { encoding });
          res.writeHead(200, { "Content-Type": contentType });
          res.end(output);
        }

        http.createServer(handleRequest).listen(port, hostname);
        
