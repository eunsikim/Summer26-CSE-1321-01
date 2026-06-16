def is_even(number):
    return number % 2 == 0

def force(mass, acceleration):
    force_val = mass * acceleration

    return force_val

def main():
    for x in range(10):
        if is_even(x):
            print(f"{x} is even")
        else:
            print(f"{x} is odd")

if __name__ == "__main__":
    main()