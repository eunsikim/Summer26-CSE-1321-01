def main():
    age = int(input("Enter your age: "))

    if age >= 18:
        if age >= 21:
            print("You are eligible to vote and drink")
        else:
            print("You are eligible to vote but not drink")
    else:
        print("You are not eligible to vote and not eligible to drink")


if __name__ == "__main__":
    main()