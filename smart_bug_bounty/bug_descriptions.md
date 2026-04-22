# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items in a list.
- **Current Issue**: Off-by-one error due to incorrect slicing (+ 1), which skips the first intended element.

## bug2.js
- **Intended Behavior**: Return a NEW object with an updated price without modifying the original.
- **Current Issue**: Mutates the original product object due to shallow reference assignment (let newProduct = product).

## bug3.java
- **Intended Behavior**: Securely compare a user-provided token with a secret string.
- **Current Issue**: Uses == for object reference comparison instead of .equals() for value comparison.

## bug4.py
- **Intended Behavior**: Create a fresh cart for each new user if one is not provided.
- **Current Issue**: Uses a mutable default argument (cart=[]), causing data to persist across different function calls.

## bug5.go
- **Intended Behavior**: Print each task concurrently using goroutines.
- **Current Issue**: Goroutine loop variable capture causes the final element to often be printed multiple times instead of each unique task.
