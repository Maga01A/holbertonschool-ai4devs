# AI-Assisted Systematic Bug Hunting Methodology

## 1. Overview
This framework provides a systematic approach to identifying, analyzing, and fixing software bugs using AI assistants. It moves beyond simple "fix this" prompts toward a structured methodology that ensures quality, security, and long-term maintainability.

## 2. The 5-Step Debugging Process
1.  **Context Injection**: Provide the AI with relevant code snippets, logs, and environmental data.
2.  **Differential Analysis**: Ask the AI to compare expected vs. actual behavior.
3.  **Root Cause Hypothesis**: Generate 3-5 potential causes for the bug.
4.  **Iterative Fix Generation**: Develop fixes starting from the least intrusive.
5.  **Validation & Regression**: Verify the fix and ensure no new bugs were introduced.

## 3. Practical Tools & Templates

### A. Bug Analysis Checklist
- [ ] Reproducibility: Can the bug be triggered consistently?
- [ ] Scope: Is it a logic error, syntax error, or environment issue?
- [ ] Data Flow: Have you identified where the data becomes "corrupt"?
- [ ] AI Context: Are relevant stack traces and variable states provided to the AI?

### B. Effective Prompting Templates
#### Type: Logic Error
> "Act as a Senior Debugger. I have a function {{FUNCTION_NAME}} that is returning {{ACTUAL_VALUE}} instead of {{EXPECTED_VALUE}}. Analyze the logical flow below and identify potential edge cases where this could fail."

#### Type: Performance Bottleneck
> "Analyze this loop/query for time complexity. Suggest 3 optimizations that improve performance without reducing readability."

### C. Testing Strategy Template
For every fix, the following tests must be performed:
1.  **Unit Test**: Specifically targets the fixed logic.
2.  **Boundary Test**: Tests the fix with extreme values (null, empty, max/min).
3.  **Integration Test**: Ensures the fix works within the broader system.

## 4. Quality Criteria for Evaluating Fixes
A fix is considered "High Quality" only if it meets these standards:
- **Safety**: Does not introduce security vulnerabilities (e.g., SQL injection).
- **Readability**: Code follows PEP8/Clean Code standards.
- **Minimalism**: Solves the specific problem without unnecessary "gold plating."
- **Performance**: Does not significantly increase memory or CPU usage.

## 5. Bug Prioritization Framework
| Priority | Impact | Urgency | Action |
| :--- | :--- | :--- | :--- |
| **P0** | System Down / Security Breach | Immediate | Fix Now |
| **P1** | Core Feature Broken | High | Fix in Current Sprint |
| **P2** | Minor UI/UX Glitch | Low | Backlog |

## 6. Real-World Examples
*Example 1: The Ghost Null.*
- **Problem**: API crashed randomly on user login.
- **AI Tactic**: Fed the AI 3 different stack traces. AI identified a race condition in the database connection pool that only occurred during peak traffic.
- **Fix**: Implemented an async retry logic suggested by the AI.

## 7. Knowledge Sharing & Collaboration
- **Prompt Library**: Save successful debugging prompts in a shared PROMPTS.md.
- **Post-Mortems**: For P0 bugs, document the "AI Reasoning Path" to help team members learn the AI's logic.
