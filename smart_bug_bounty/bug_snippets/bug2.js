/**
 * Product update module
 * Handles updating product properties
 */
function validateProduct(prod) {
    if (!prod) {
        throw new Error("Invalid product");
    }
}

function updatePrice(product, newPrice) {
    validateProduct(product);
    console.log("Updating price for " + product.name);
    
    // BUG: Shallow copy assignment modifies the original object
    let updatedProduct = product;
    updatedProduct.price = newPrice;
    
    console.log("Update complete.");
    return updatedProduct;
}

const p1 = { name: "Laptop", price: 1000 };
const p2 = updatePrice(p1, 1500);
// p1.price is now incorrectly 1500
