def sample_fn():
    print("Hello World")
    # return stops the function and returns a value
    return #Since we did not specify a value to return, it returns `None`

    print("Hello CSE 1321")


def sample_fn_2():
    print("Hello World")

    # If a function does not have a return statement
    # It will return `None` by default

def main():
    print(type(sample_fn()))
    print(type(sample_fn_2()))

if __name__ == "__main__":
    main()