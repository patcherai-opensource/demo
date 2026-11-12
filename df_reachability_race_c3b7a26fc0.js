// Test-owned reachability fixture: direct js-yaml@4.1.0 usage.
// The application accepts a YAML document provided by its caller.
const yaml = require("js-yaml");

function parseCallerYaml(documentText) {
  return yaml.load(documentText);
}

module.exports = { parseCallerYaml };
