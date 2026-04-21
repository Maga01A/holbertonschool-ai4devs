def get_last_elements(items, n):
    # This is a helper function to retrieve elements.
    # It takes a list and an integer as arguments.
    # The goal is to return the last n items.
    # ------------------------------------------
    # Check if the input is actually a list
    if not isinstance(items, list):
        return None
    
    # Check if n is greater than the list size
    if n > len(items):
        return items
    
    # The following line contains the BUG:
    # It has an off-by-one error due to +1.
    result = items[len(items) - n + 1:]
    
    # Return the processed result
    return result

# Sample test execution
if __name__ == "__main__":
    my_data = [1, 2, 3, 4, 5]
    print(get_last_elements(my_data, 2))
