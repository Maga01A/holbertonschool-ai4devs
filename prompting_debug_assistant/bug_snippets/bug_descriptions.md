# Bug Descriptions and Analysis

## Bug 1 – bug1.py

Intended behavior:
Return the last n items of a given list.

Issue type:
Off-by-one error / IndexOutOfBoundsException.

Notes:
The loop range uses `len(items) + 1` as the upper limit, which causes the index to go out of bounds during execution.

---

## Bug 2 – bug2.js

Intended behavior:
Calculate and return the average of a list/array of numbers.

Issue type:
Logical error.

Notes:
The function divides the total sum by `(numbers.length - 1)` instead of `numbers.length`, resulting in an incorrect arithmetic mean.

---

## Bug 3 – bug3.java

Intended behavior:
Safely compare a string variable against the text "hello" without crashing.

Issue type:
NullPointerException (Runtime exception).

Notes:
Calling `.equals()` directly on a variable with a `null` reference causes a `NullPointerException`. It should be invoked as `"hello".equals(text)` or checked for nullity first.

---

## Bug 4 – bug4.py

Intended behavior:
Define a function that prints a personalized greeting message.

Issue type:
Syntax error.

Notes:
The function header `def greet(name)` is missing a colon (`:`) at the end of the line.

---

## Bug 5 – bug5.js

Intended behavior:
Perform numeric addition to add 10 to a given numeric input value.

Issue type:
Type coercion / Data type misuse.

Notes:
Passing a string `"5"` causes JavaScript to perform string concatenation instead of mathematical addition, returning `"510"` instead of `15`.
