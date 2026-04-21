def get_last_elements(items, n):
    if not isinstance(items, list):
        return None
    # FIX: Corrected slice to return exactly the last n items
    return items[-n:] if n > 0 else []

# Test cases
my_list = [10, 20, 30, 40, 50, 60, 70]
print(f"Test n=3: {get_last_elements(my_list, 3)}") # Expected: [50, 60, 70]
