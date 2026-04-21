def get_last_elements(items, n):
    # Intended: Return the last n items in a list.
    # This function is designed to handle list slicing
    # but contains a classic off-by-one error.
    if not isinstance(items, list):
        return None
    # Bug is in the line below:
    return items[len(items) - n + 1:]

# Sample execution for testing
my_list = [10, 20, 30, 40, 50, 60, 70]
n_val = 3
result = get_last_elements(my_list, n_val)
print(f"Result: {result}")
