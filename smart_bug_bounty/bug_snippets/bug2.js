function updatePrice(product, newPrice) {
    // BUG: Mutates original object due to shallow reference assignment
    let newProduct = product;
    newProduct.price = newPrice;
    return newProduct;
}
