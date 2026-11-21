// Test-only repair validation fixture; not imported by production code.
export function evaluateUntrustedExpression(userExpression) {
  return eval(userExpression); // unsafe dynamic code evaluation
}
