function processOrder(item, price, quantity) {
    const total = price * quantity;
    const status = total > 0 ? "Processed" : "Invalid";
    return {
        item: item,
        total: total,
        status: status
    };
}

console.log(processOrder("Laptop", 1200, 2));
