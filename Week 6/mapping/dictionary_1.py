def main():
    # Initializing a dictionary (in-code)
    user = {"username":"ekim54", "password":"123"}

    # Accessing/Reading a dictionary by Key
    print(f"Username: {user["username"]}, Password: {user["password"]}")

    # Adding into a dictionary
    user["firstName"] = "Eun Sik"

    print(user)

    # Modifying/Update a value in a dictionary
    user["password"] = "123!"

    print(user)

    # Deleting/Removing a KV-Pair
    del user["firstName"]
    
    print(user)



if __name__ == "__main__":
    main()