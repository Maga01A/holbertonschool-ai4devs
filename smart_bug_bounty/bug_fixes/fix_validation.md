# Fix Validation Log

## bug1.py
- **Original Issue**: Mutable default argument (cart=[]) caused data to persist across function calls unexpectedly.
- **Fix Applied**: Changed default argument to cart=None and initialized cart = [] inside the function body.
- **Test Results**: Passed. user1 and user2 now receive independent, fresh list instances.

## bug2.js
- **Original Issue**: Shallow reference assignment (let updatedProduct = product) mutated the original object.
- **Fix Applied**: Used object spread syntax ({ ...product }) to clone the object before updating the price.
- **Test Results**: Passed. originalProduct.price remains 1000, while updatedProduct.price correctly updates to 1500.

## bug3.java
- **Original Issue**: Used == operator for String comparison, which checks memory references instead of actual text values.
- **Fix Applied**: Replaced 	oken == secret with 	oken.equals(secret).
- **Test Results**: Passed. The identical strings with different memory addresses now correctly evaluate to 	rue.

## bug4.go
- **Original Issue**: Goroutines captured the loop variable 	 by reference, causing all background routines to print the last element of the slice.
- **Fix Applied**: Passed 	 as an explicit argument (	askName string) to the anonymous goroutine closure.
- **Test Results**: Passed. All individual tasks (A, B, C, D) are now processed and printed distinctly without overwriting each other.
