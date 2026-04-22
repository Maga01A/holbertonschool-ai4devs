import datetime

def log_operation(operation_name):
    # Helper log function
    print(f"[{datetime.datetime.now()}] Executing: {operation_name}")

def get_last_elements(items, n):
    """
    Returns the last n elements of the provided list.
    Includes type checking to prevent system crashes.
    """
    log_operation("get_last_elements")
    
    if not isinstance(items, list):
        return None
    if n > len(items):
        return items
        
    # BUG: off-by-one error (+1 skips the first intended element)
    result = items[len(items) - n + 1:]
    return result

if __name__ == "__main__":
    my_data = [10, 20, 30, 40, 50]
    print("Result:", get_last_elements(my_data, 3))
