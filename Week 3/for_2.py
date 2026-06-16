def main():
    login_success = False

    for x in range(3):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == "admin" and password == "123":
            print("Login Successful!")
            login_success = True
            break
        else:
            print(f"Username/Password incorrect! Try again. You have {3 - x - 1} tries left.")
    
    if login_success:
        print("Welcome admin!")
    else:
        print("You are locked out of the system, please try in 1 hour")


if __name__ == "__main__":
    main()