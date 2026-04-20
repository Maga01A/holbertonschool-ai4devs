const assert = require('assert');
const { processOrder } = require('../../implementations/javascript/order_processor');

// Qeyd: JS faylinda 'module.exports = { processOrder };' ?lav? olunmalidir
try {
    const result = processOrder("Laptop", 1200, 2);
    assert.strictEqual(result.total, 2400);
    assert.strictEqual(result.status, "Processed");
    console.log("JS Test Passed!");
} catch (err) {
    console.error("JS Test Failed:", err);
    process.exit(1);
}
