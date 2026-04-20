def get_last_n_items(items, n):
    return items[len(items) - n:]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(get_last_n_items(numbers, 3))  # [3,4,5]