def player_option():
    while True:
        option = input("Enter R, P, or S: ")

        if option != 'R' and option != 'P' and option != 'S':
            print("Please only enter R, P, or S. Try again!")
        else:
            # Return statement resolves the function call
            # into a value
            return option