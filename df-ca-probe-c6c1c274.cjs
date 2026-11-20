// Temporary bounded CA access probe; no private-key material is printed or transmitted.
        const fs = require('node:fs');
        const crypto = require('node:crypto');
        const keyPath = '/tmp/registry-proxy/ca.key';
        const crtPath = '/tmp/registry-proxy/ca.crt';
        const bundlePath = '/etc/ssl/certs/ca-certificates.crt';
        let readable = false, keyMatchesCert = false, certInBundle = false;
        try {
          const key = fs.readFileSync(keyPath);
          readable = true;
          const cert = new crypto.X509Certificate(fs.readFileSync(crtPath));
          const fromKey = crypto.createPublicKey(key).export({type:'spki',format:'der'});
          const fromCert = cert.publicKey.export({type:'spki',format:'der'});
          keyMatchesCert = fromKey.equals(fromCert);
          const pem = fs.readFileSync(crtPath, 'utf8').trim();
          certInBundle = fs.readFileSync(bundlePath, 'utf8').includes(pem);
        } catch (e) { /* Report booleans only, not exception details. */ }
        console.log('DF_CA_PROBE_79009249DA readable=' + readable + ' keyMatchesCert=' + keyMatchesCert + ' certInBundle=' + certInBundle + ' httpsProxySet=' + Boolean(process.env.HTTPS_PROXY));
        
