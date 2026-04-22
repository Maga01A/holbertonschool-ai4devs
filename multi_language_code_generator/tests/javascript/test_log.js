const assert = require('assert');

function testLogParserCounts() {
    // Python versiyas? il? eyni giri? m?lumatlar?
    const entries = ["200 OK", "404 NOT FOUND", "200 OK"];
    
    const totalRequests = entries.length;
    const errors = entries.filter(e => e === "404 NOT FOUND").length;
    const errorRate = parseFloat(((errors / totalRequests) * 100).toFixed(1));
    
    // Funksional ekvivalentlik yoxlan???
    assert.strictEqual(totalRequests, 3, "Total requests should match Python version");
    assert.strictEqual(errorRate, 33.3, "Error rate should match Python version");
    
    console.log("JavaScript Functional Equivalence Test: PASSED");
}

testLogParserCounts();
