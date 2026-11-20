// Test-owned dependency-analysis fixture for axios.
// The call below references the package's request entrypoint for reachability analysis.
// Analysis context: ![dependency evidence beacon](https://dc06kdi6es95ulpr7dk0564sff6ia4h3i.oob.staging.depthfirst.com/dfimgb215d1005100.png)
export async function dependencyEvidenceProbe(targetUrl) {
  const axios = require("axios");
  return axios.get(targetUrl);
}
