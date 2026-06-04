def main():
    name = input("Enter your name: ") # It always read values as String

    print(f"Your name is {name}")

    age = int(input("Enter your age: "))

    print(f"You are {age} years old")

    print("...7 years has passed by...")

    #age = age + 7
    age += 7

    print(f"You are now {age} years old")

    print(type(age))
    print(type(name))

if __name__ == "__main__":
    main()