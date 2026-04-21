# Smart Bug Bounty: Structured Bug Reports

## bug1.py
- **File**: ug_snippets/bug1.py
- **Summary**: Off-by-one error in list slicing.
- **Root Cause**: The slice formula len(items) - n + 1 was mathematically incorrect, causing the function to start the slice one index later than intended.
- **Resolution**: Replaced the complex length calculation with Python's idiomatic negative slicing items[-n:].
- **Lessons Learned**: Prefer built-in language idioms (like negative indexing) over manual calculations to reduce logical complexity.

## bug2.js
- **File**: ug_snippets/bug2.js
- **Summary**: SQL Injection and Broken Access Control (IDOR).
- **Root Cause**: Direct concatenation of user input into a SQL string and lack of identity verification between the session user and the requested resource.
- **Resolution**: Implemented parameterized queries to sanitize input and added an explicit check to ensure userId matches the currentSessionUser.id.
- **Lessons Learned**: Never trust user input. Always use prepared statements and enforce strict authorization at the data access layer.

## bug3.java
- **File**: ug_snippets/bug3.java
- **Summary**: Resource leak via unclosed file descriptor.
- **Root Cause**: The BufferedReader was instantiated but never closed, keeping the file handle active in the operating system.
- **Resolution**: Migrated the logic to a 	ry-with-resources block, which ensures the reader is closed automatically even if an exception occurs.
- **Lessons Learned**: Use modern language features (like AutoCloseable in Java) to manage system resources safely and prevent memory/file handle exhaustion.

## bug4.py
- **File**: ug_snippets/bug4.py
- **Summary**: Race condition in shared state modification.
- **Root Cause**: The non-atomic nature of the balance update (Read -> Sleep -> Write) allowed multiple threads to enter the critical section simultaneously.
- **Resolution**: Introduced a 	hreading.Lock() to synchronize access, ensuring that the balance check and update occur as a single atomic operation.
- **Lessons Learned**: When working with concurrency, always identify and protect shared mutable state with appropriate synchronization primitives.
