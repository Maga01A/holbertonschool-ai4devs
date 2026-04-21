const assert = require('assert');
// Simple math test for the logic used in server.js
function calculate(dist, type) {
    const emissions = { 'standard': 120, 'ev': 0 };
    return (dist * emissions['standard'] - dist * emissions[type]) / 1000;
}

try {
    assert.strictEqual(calculate(10, 'ev'), 1.2);
    console.log('Test Passed: Carbon calculation is correct.');
} catch (e) {
    console.error('Test Failed:', e.message);
}
