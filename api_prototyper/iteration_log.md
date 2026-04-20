# API Iteration Log - RentFlow Project

## Iteration 1
- **Issue identified**: The GET /items endpoint returns all items at once, which could lead to performance issues as the inventory grows.
- **AI Suggestion**: Implement pagination using page and limit query parameters to fetch data in chunks.
- **Final Fix**: Updated the /items route in src/index.js to support slice-based pagination.

## Iteration 2
- **Issue identified**: The API lacks basic data validation, allowing items to be created with missing names or negative prices.
- **AI Suggestion**: Add a validation middleware or simple conditional checks to ensure 
ame is a string and pricePerDay is a positive number.
- **Final Fix**: Implemented a validation check in the POST /items route to return a 400 Bad Request error for invalid data.
