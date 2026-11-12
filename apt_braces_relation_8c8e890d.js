// Test-owned example showing demo's dependency on patcherai-opensource/braces.
const braces = require('braces');
module.exports = function expandExample(pattern) { return braces.expand(pattern); };
