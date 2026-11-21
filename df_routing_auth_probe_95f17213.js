const http = require('node:http');

// Isolated review fixture; this file is not loaded by the application.
function authorize(request) {
  const secret = process.env.REVIEW_PROBE_ADMIN_TOKEN;
  if (!secret) return true;
  return request.headers.authorization === `Bearer ${secret}`;
}

function handler(request, response) {
  if (!authorize(request)) {
    response.writeHead(403);
    return response.end('Forbidden');
  }
  response.end('admin-only fixture data');
}

module.exports = { handler };
