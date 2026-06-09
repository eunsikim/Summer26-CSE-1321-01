def main():
    age = int(input("Enter your age: "))

    if age >= 21:
        print("You are elegible to vote and drink")
    elif age >= 18: # this condition could be age >= 18 and age < 21, but age < 21 is implied
        print("You are eligible to vote but not drink")
    else:
        print("You are not eligible to vote and not eligible to drink")


if __name__ == "__main__":
    main()