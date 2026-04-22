const assert = require('assert');

function analyzeLogs(entries) {
    if (entries.length === 0) return { total: 0, errorRate: 0.0 };
    const total = entries.length;
    const errors = entries.filter(e => e === "404 NOT FOUND").length;
    const errorRate = parseFloat(((errors / total) * 100).toFixed(1));
    return { total: total, errorRate: errorRate };
}

function runTests() {
    console.log("Running JavaScript Tests...");
    
    // Test 1: Standard Case
    const case1 = analyzeLogs(["200 OK", "404 NOT FOUND", "200 OK"]);
    assert.strictEqual(case1.total, 3);
    assert.strictEqual(case1.errorRate, 33.3);
    console.log("- test_standard_case: PASSED");

    // Test 2: Empty Case
    const case2 = analyzeLogs([]);
    assert.strictEqual(case2.total, 0);
    assert.strictEqual(case2.errorRate, 0.0);
    console.log("- test_empty_case: PASSED");
    
    console.log("All JavaScript tests passed successfully!");
}

try {
    runTests();
} catch (err) {
    console.error("Test Failed:", err.message);
    process.exit(1);
}
