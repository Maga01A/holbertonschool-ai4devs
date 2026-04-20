def get_last_n_items(items, n):
    """
    Returns the last n items from a given list.
    Calculates the starting index and slices accordingly.
    """
    if n <= 0:
        return []
        
    list_length = len(items)
    start_index = list_length - n
    result_slice = items[start_index:]
    
    return result_slice

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(f"Result for n=3: {get_last_n_items(numbers, 3)}")