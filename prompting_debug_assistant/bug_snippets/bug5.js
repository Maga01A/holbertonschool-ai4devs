function addTen(value) {
    return value + 10;
}

function testAddTen() {
    let input = "5";
    let result = addTen(input);
    console.log("Result:", result);
}

function anotherTest() {
    console.log(addTen("10"));
}

testAddTen();