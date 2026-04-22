# Bug Descriptions

## bug1.py
- **Intended Behavior**: Create a fresh shopping cart list for each new user.
- **Current Issue**: Uses a mutable default argument (cart=[]), causing the list to persist across calls.

## bug2.js
- **Intended Behavior**: Return a new object with updated price without modifying the original.
- **Current Issue**: Mutates the original product object due to shallow reference assignment.

## bug3.java
- **Intended Behavior**: Securely compare a user-provided token with a secret string.
- **Current Issue**: Uses == for object reference comparison instead of .equals() for value comparison.

## bug4.go
- **Intended Behavior**: Process and print each task concurrently using goroutines.
- **Current Issue**: Goroutine loop variable capture causes the final element to be printed multiple times.
