def main():
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are elegible to vote")
    # elif age < 18:
    #     print("You are not eligible to vote")
    else:
        print("You are not eligible to vote")


if __name__ == "__main__":
    main()