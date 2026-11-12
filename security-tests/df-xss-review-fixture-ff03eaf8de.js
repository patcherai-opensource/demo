// Isolated test-only fixture ff03eaf8de; never merge or deploy.
const { exec } = require("child_process");
function testOnlyUnsafeShell(req) {
  exec(req.query.command);
}
module.exports = { testOnlyUnsafeShell };
