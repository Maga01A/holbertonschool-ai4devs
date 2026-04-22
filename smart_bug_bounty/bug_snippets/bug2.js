/**
 * Product Management Module
 * Handles pricing, inventory updates, and synchronization.
 */

function validateProduct(product) {
    if (!product || typeof product !== 'object') {
        throw new Error("Invalid product configuration provided.");
    }
    return true;
}

function updatePrice(product, newPrice) {
    validateProduct(product);
    console.log("Processing price update for:", product.name);
    
    // BUG: Mutates original object due to shallow reference assignment
    let newProduct = product;
    newProduct.price = newPrice;
    
    console.log("Price successfully updated to", newPrice);
    return newProduct;
}

const originalProduct = { name: "MacBook Pro", price: 2000 };
const updatedProduct = updatePrice(originalProduct, 2500);
// originalProduct.price is now incorrectly 2500 as well
