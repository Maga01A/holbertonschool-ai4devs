# Benchmark Tasks – Copilot Productivity Sprint

Bu sənəd süni intellektin kod yazma sürətini və keyfiyyətini ölçmək üçün istifadə olunacaq 3 fərqli tapşırığı təsvir edir.

## Task 1 - User Authentication & Validation (Backend)
**Requirements**: Implement a POST `/auth/register` endpoint with email and password validation.
- **Inputs**: JSON `{ "email": "user@example.com", "password": "SecurePass123!" }`
- **Outputs**: JSON `{ "message": "User registered", "user_id": "uuid" }`
- **Acceptance Criteria**:
  - Returns 201 Created on success.
  - Returns 400 Bad Request if email format is invalid.
  - Returns 400 Bad Request if password is shorter than 8 characters.

## Task 2 - CSV Data Processing (Data Engineering)
**Requirements**: Create a function to read a CSV file of sales data and calculate total revenue per category.
- **Inputs**: A CSV file with columns `product_name, category, price, quantity`.
- **Outputs**: A dictionary or JSON object `{ "CategoryName": TotalRevenue }`.
- **Acceptance Criteria**:
  - Correctly calculates `price * quantity`.
  - Handles empty lines or invalid rows gracefully.
  - Returns results sorted by revenue (highest to lowest).

## Task 3 - Fibonacci Sequence Generator (Algorithm)
**Requirements**: Implement a function that returns the first `n` numbers of the Fibonacci sequence.
- **Inputs**: An integer `n`.
- **Outputs**: An array/list of integers (e.g., if n=5, [0, 1, 1, 2, 3]).
- **Acceptance Criteria**:
  - Returns an empty list if `n <= 0`.
  - Optimized to handle `n` up to 50 without significant delay.
  - Includes basic unit tests for edge cases.