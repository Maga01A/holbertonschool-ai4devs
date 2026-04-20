function addTen(value) {
    return Number(value) + 10;
}

function testAddTen() {
    let input = "5";
    let result = addTen(input);
    console.log("Result:", result); // 15
}

testAddTen();