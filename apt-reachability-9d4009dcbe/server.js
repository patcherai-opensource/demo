const http = require("http");
        const lodash = require("lodash");

        // This fixture exercises the installed lodash version with untrusted JSON input.
        function mergeRequestBody(body) {
          const userInput = JSON.parse(body);
          return lodash.defaultsDeep({}, userInput);
        }

        http.createServer((request, response) => {
          if (request.method !== "POST" || request.url !== "/merge") {
            response.writeHead(404).end();
            return;
          }
          let body = "";
          request.on("data", (chunk) => { body += chunk; });
          request.on("end", () => {
            try {
              response.setHeader("content-type", "application/json");
              response.end(JSON.stringify(mergeRequestBody(body)));
            } catch (err) {
              response.writeHead(400).end("Invalid JSON");
            }
          });
        }).listen(process.env.PORT || 3107);
        
