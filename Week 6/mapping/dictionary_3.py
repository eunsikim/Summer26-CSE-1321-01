def main():
    my_dictionary = {"username":"ekim54", "password":"123", 3.14:"Pi", "Pi":3.14, "firstName":"Eun Sik"}

    # Whenever you search on a dictionary, it will always
    # be `BY THE KEY`
    if "firstName" in my_dictionary:
        if my_dictionary["firstName"] == "Eun Sik":
            print(f"Hello {my_dictionary["firstName"]}")
        else:
            print("Error")
    else:
        print("We do not have a 'firstName' key")

    # Similar to Iterating, we can use the built-in dictionary
    # functions `.values()` and `.items()`
    if 3.14 in my_dictionary.values():
        print("We have a value of float 3.14 in my_dictionary")
    
    if (3.14, "Pi") in my_dictionary.items():
        print("We have the KV-Pair 3.14:\"Pi\"")


if __name__ == "__main__":
    main()