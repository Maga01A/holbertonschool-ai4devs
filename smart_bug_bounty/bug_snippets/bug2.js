function updatePrice(product, newPrice) {
    const updated = product; // Shallow copy
    updated.price = newPrice;
    return updated;
}
