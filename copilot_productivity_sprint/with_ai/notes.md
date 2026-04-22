# AI Usage Notes - Productivity Sprint

## Tasks Solved with AI
- **Data Aggregation**: Refactored manual loops into optimized Pandas operations.
- **Unit Testing**: Generated comprehensive test cases for edge cases (empty files, missing columns).
- **Documentation**: Auto-generated docstrings using Copilot for all functions.

## Prompts Used
1. "Write a Python function using pandas to group a dataframe by user_id and calculate the sum of session_duration."
2. "Generate 5 pytest cases for the aggregate_user_data function, including a test for FileNotFoundError."
3. "Refactor the existing nested loops in processing.py into a list comprehension for better performance."

## Time Spent Analysis
- **Manual Implementation Time (Estimated)**: 90 minutes
- **With Copilot/AI Implementation Time (Actual)**: 25 minutes
- **Efficiency Gain**: ~72% faster development.

## Reflection
Copilot was exceptionally fast at generating boilerplate code and transforming complex loops. The main challenge was ensuring that the AI-generated Pandas syntax matched the specific version installed in our environment.
