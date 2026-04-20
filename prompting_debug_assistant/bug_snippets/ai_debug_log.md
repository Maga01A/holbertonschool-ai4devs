## Bug 1 – bug1.py
**AI Diagnosis**: The loop uses `len(items) + 1`, which goes out of range and causes IndexError. Also indentation issues exist.

**Suggested Fix**: Replace range with `range(len(items) - n, len(items))`.

**Alternative Fixes Tested**: None.

**Result**: Fix works correctly and returns last n items.


---

## Bug 2 – bug2.js
**AI Diagnosis**: The function divides by `numbers.length - 1`, which causes incorrect average calculation.

**Suggested Fix**: Use `numbers.length` instead.

**Alternative Fixes Tested**: None.

**Result**: Correct average is now returned.


---

## Bug 3 – bug3.java
**AI Diagnosis**: `text` is null, so calling `text.equals()` causes NullPointerException.

**Suggested Fix**: Use `"hello".equals(text)` instead of `text.equals("hello")`.

**Alternative Fixes Tested**: None.

**Result**: No runtime exception, code runs safely.


---

## Bug 4 – bug4.py
**AI Diagnosis**: Missing colon (`:`) after function definition causes SyntaxError.

**Suggested Fix**: Add `:` after `def greet(name)`.

**Alternative Fixes Tested**: None.

**Result**: Code executes correctly after fix.


---

## Bug 5 – bug5.js
**AI Diagnosis**: String input `"5"` causes concatenation instead of numeric addition.

**Suggested Fix**: Convert input using `Number(value)`.

**Alternative Fixes Tested**: `parseInt(value)` also works.

**Result**: Both fixes produce correct numeric output.