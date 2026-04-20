def get_last_n_items(items, n):
    result = []
    for i in range(len(items) - n, len(items) + 1):
        result.append(items[i])
    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(get_last_n_items(numbers, 3))