// Synthetic test fixture: not imported, deployed, or bound to a server.
        const { exec } = require('node:child_process');
        function dfnvdcb0ddec5b2_unsafeDiagnostic(req, res) {
          // SECURITY ISSUE (synthetic): untrusted query text flows into a shell command.
          const userSupplied = req.query.command;
          exec('echo ' + userSupplied, (error, stdout) => {
            if (error) return res.status(500).send('synthetic error');
            return res.send(stdout);
          });
        }
        module.exports = { dfnvdcb0ddec5b2_unsafeDiagnostic };
        