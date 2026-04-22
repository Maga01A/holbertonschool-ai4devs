# AI Debug Log

## bug1.py
- **AI Explanation**: Python evaluates default arguments exactly once when the function is defined. Since a list [] is mutable, all calls share the same list in memory.
- **Suggested Fix**: Use None as default and initialize inside: if cart is None: cart = []
- **Confidence**: High

## bug2.js
- **AI Explanation**: In JavaScript, objects are assigned by reference. let updatedProduct = product; just creates a new pointer to the exact same object.
- **Suggested Fix**: Use spread syntax to clone the object: let updatedProduct = { ...product };
- **Confidence**: High

## bug3.java
- **AI Explanation**: In Java, the == operator compares memory addresses, not the actual string content.
- **Suggested Fix**: Use the equals method: oolean isValid = token.equals(secret);
- **Confidence**: High

## bug4.go
- **AI Explanation**: Loop variables are captured by reference in goroutines. The loop finishes before goroutines start, so they all see the last value.
- **Suggested Fix**: Pass the variable as an argument to the goroutine: go func(task string) { ... }(t)
- **Confidence**: High
