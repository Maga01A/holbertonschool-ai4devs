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
    
    // FIXED: Use spread syntax to create a shallow copy
    let updatedProduct = { ...product };
    updatedProduct.price = newPrice;
    
    console.log("Update complete.");
    return updatedProduct;
}

const originalProduct = { name: "Laptop", price: 1000 };
const updatedProduct = updatePrice(originalProduct, 1500);
console.log("Original Product Price:", originalProduct.price); // Correctly 1000
console.log("Updated Product Price:", updatedProduct.price);   // Correctly 1500
