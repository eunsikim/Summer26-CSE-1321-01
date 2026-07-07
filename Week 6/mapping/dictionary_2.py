def main():
    user = {"username":"ekim54", "password":"123", 3.14:"Pi", "Pi":3.14}

    # Traversing a dictionary, will traverse it by the KEY
    # We can use the KEY to access the values associated with said KEY
    for x in user:
        print(f"{x}:{user[x]}")

    # We can also use the dictionary built-in `.values() 
    # function to traverse JUST the VALUES
    for x in user.values():
        print(x)

    # We can also use the dictionary built-in `.items() 
    # function to traverse all of the KV-Pairs as tuples
    for x in user.items():
        print(x)

    for x in user.key():
        print(x)

if __name__ == "__main__":
    main()