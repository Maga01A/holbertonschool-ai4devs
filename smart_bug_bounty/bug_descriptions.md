# Bug Descriptions

## bug1.py
- **Intended Behavior**: Calculates the average of a list of ratings.
- **Current Issue**: Crashes with ZeroDivisionError if the list is empty.

## bug2.js
- **Intended Behavior**: Return a NEW object with an updated price without modifying the original.
- **Current Issue**: Mutates the original product object due to shallow reference assignment.

## bug3.java
- **Intended Behavior**: Securely compare a user-provided token with a secret string.
- **Current Issue**: Uses == for object reference comparison instead of .equals() for value comparison.

## bug4.py
- **Intended Behavior**: Create a fresh cart for each new user if one is not provided.
- **Current Issue**: Uses a mutable default argument ([]), causing carts to persist across different function calls.
