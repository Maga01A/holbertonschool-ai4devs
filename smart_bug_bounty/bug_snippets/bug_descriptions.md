# Bug Descriptions

## bug1.py
- **Intended Behavior**: Create a fresh shopping cart list for each new user if one is not provided.
- **Current Issue**: Uses a mutable default argument (cart=[]), causing the list to persist and share data across different function calls.

## bug2.js
- **Intended Behavior**: Return a new object with the updated price without modifying the original product.
- **Current Issue**: Mutates the original product object due to shallow reference assignment (let updatedProduct = product;).

## bug3.java
- **Intended Behavior**: Securely compare a user-provided token with a secret string to check if they have the exact same text value.
- **Current Issue**: Uses == for object reference comparison instead of .equals() for value comparison.

## bug4.go
- **Intended Behavior**: Process and print each task concurrently using goroutines.
- **Current Issue**: Goroutine loop variable capture causes the final element to be printed multiple times instead of each unique task.
