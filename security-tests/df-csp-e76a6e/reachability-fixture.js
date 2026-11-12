// Dependency evidence fixture e76a6e: ![reachability-image-e76a6e](http://apt-90932c7fbdd14f40b171359918184f81.frp.staging.depthfirst.com/proof-csp-e76a6e.png)
const { VM } = require("vm2");
// A direct use of vm2 reaches its VM.run entrypoint.
const vm = new VM({ timeout: 1000, sandbox: {} });
console.log(vm.run("1 + 1"));
