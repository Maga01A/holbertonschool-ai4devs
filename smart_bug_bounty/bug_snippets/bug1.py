def get_last_elements(items, n):
    if not isinstance(items, list): return None
    if n > len(items): return items
    # BUG: off-by-one error (+1 skips the first intended element)
    return items[len(items) - n + 1:]
