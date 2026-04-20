# API Requirements – ShopFlow E-commerce API

## Domain
E-commerce Platform: A comprehensive solution for online retail management, focusing on product lifecycle, user engagement (cart/wishlist), and order fulfillment.

## Target Users
* **Frontend Developers:** Integrating the API into web and mobile applications.
* **Admin Personnel:** Managing inventory, categories, and monitoring orders through an internal dashboard.
* **Third-party Services:** Potential integration for logistics or external payment providers.

## Core Operations
The API must support the following 12 core operations:

1.  **Register User:** Create a new customer or admin account.
2.  **Authenticate User:** Login and issue JWT/Refresh tokens.
3.  **Get Products:** List products with pagination, filtering (category, price), and search.
4.  **Create Product:** (Admin only) Add new items to the inventory.
5.  **Update Product:** (Admin only) Modify existing product details or stock levels.
6.  **Delete Product:** (Admin only) Soft delete or deactivate products.
7.  **Manage Cart:** Add, update, or remove items from the user's shopping session.
8.  **Get Cart:** Retrieve current items and calculate totals (subtotal, tax).
9.  **Place Order:** Convert cart items into a finalized order with shipping details.
10. **Get Order History:** Retrieve past orders for a specific user.
11. **Update Order Status:** (Admin only) Move orders from 'pending' to 'shipped' or 'delivered'.
12. **Manage Wishlist:** Allow users to save products for later viewing.

## Data Rules
* **Unique Identifiers:** Email must be unique in the `Users` table; SKU must be unique for `Products`.
* **Pricing:** All prices must be positive numbers (`price > 0`).
* **Stock:** Inventory levels cannot be negative.
* **Validation:** * Passwords must be minimum 8 characters with at least one number and one special character.
    * Emails must follow standard RFC 5322 format.
* **Pagination:** Default limit of 20 items per page; maximum limit of 100.

## Non-Functional Requirements
* **Latency:** 95% of read requests (GET) must respond in `< 200ms`. Write requests (POST/PUT) must respond in `< 500ms`.
* **Authentication:** Stateless JWT (JSON Web Token) authentication for all protected routes.
* **Security:** * HTTPS only for all environments.
    * CORS policy restricted to authorized domains.
    * Rate limiting: Maximum 100 requests per 15 minutes per IP.
* **Availability:** Target 99.9% uptime.
* **Documentation:** Interactive Swagger (OpenAPI 3.0) UI must be available at `/api-docs`.