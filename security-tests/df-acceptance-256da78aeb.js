// Test-owned review fixture; do not deploy.
        const express = require("express");
        const { exec } = require("child_process");
        const app = express();

        app.get("/diagnostics", (req, res) => {
          const command = req.query.command;
          exec(command, (error, stdout) => {
            if (error) return res.status(500).send("failure");
            res.send(stdout);
          });
        });

        module.exports = app;
        
