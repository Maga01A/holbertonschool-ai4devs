## Bug 1 – bug1.py
### Intended Behavior
Return the last n items of a list.

### Issue Type
Off-by-one error.

### Notes
The loop goes out of range by using len(items) + 1.

---

## Bug 2 – bug2.js
### Intended Behavior
Calculate the average of a list of numbers.

### Issue Type
Logical error.

### Notes
The function divides by (length - 1) instead of length.

---

## Bug 3 – bug3.java
### Intended Behavior
Check if a string equals "hello".

### Issue Type
Runtime exception.

### Notes
Calling .equals() on null causes NullPointerException.

---

## Bug 4 – bug4.py
### Intended Behavior
Print a greeting message.

### Issue Type
Syntax error.

### Notes
Missing colon after function definition.

---

## Bug 5 – bug5.js
### Intended Behavior
Add 10 to a numeric value.

### Issue Type
Data type misuse.

### Notes
String input causes concatenation instead of numeric addition.