# Bug Descriptions and Analysis

## Bug 1 – bug1.py

Intended behavior:
Given a list of items and an integer `n`, return a new list containing the last `n` elements in their original order. For `numbers = [1, 2, 3, 4, 5]` and `n = 3`, the function should return `[3, 4, 5]` without throwing an `IndexError`.

Issue type:
Off-by-one error / IndexOutOfBoundsException.

Notes:
The loop range uses `len(items) + 1` as the upper stop boundary, causing `items[i]` to access an index equal to `len(items)`, which raises an `IndexError`. The range upper bound should be `len(items)`.

---

## Bug 2 – bug2.js

Intended behavior:
Given an array of numeric values, calculate and return the exact arithmetic mean by summing all elements and dividing by the total count (`numbers.length`). For input `[10, 20, 30, 40]`, the expected return value is `25`.

Issue type:
Logical error.

Notes:
The function incorrectly divides the total sum by `(numbers.length - 1)` instead of `numbers.length`, returning `33.33` instead of the expected mean of `25`.

---

## Bug 3 – bug3.java

Intended behavior:
Safely evaluate whether a given string variable matches `"hello"` and execute conditionally. If the variable is `null`, it should safely evaluate to `false` (or perform a null-check) without throwing a runtime exception and continue execution to print `"Done"`.

Issue type:
NullPointerException (Runtime exception).

Notes:
Invoking `.equals()` on a `null` reference (`text.equals("hello")`) triggers a `NullPointerException`. Using literal-first comparison (`"hello".equals(text)`) safely returns `false` when `text` is `null`.

---

## Bug 4 – bug4.py

Intended behavior:
Define and execute valid Python functions `greet(name)`, `main()`, and `extra_function()` such that calling `greet("Ali")` outputs `"Hello, Ali"` to the standard output without syntax parsing errors.

Issue type:
Syntax error.

Notes:
The function declaration line `def greet(name)` is missing a trailing colon (`:`), causing Python to fail at compile-time with a `SyntaxError: invalid syntax`.

---

## Bug 5 – bug5.js

Intended behavior:
Take an input value, ensure it is treated as a numeric type, add 10 to it mathematically, and return the numerical sum. For string input `"5"`, the function should parse/coerce the input and return `15` as a number.

Issue type:
Type coercion / Data type misuse.

Notes:
Because input `"5"` is a string, the `+` operator performs string concatenation instead of numeric addition, yielding `"510"` instead of the intended numeric sum `15`.
