def greet(name)
    message = "Hello, " + name
    print(message)


def main():
    user_name = "Ali"
    greet(user_name)


def extra_function():
    test_name = "Test"
    greet(test_name)


if __name__ == "__main__":
    main()