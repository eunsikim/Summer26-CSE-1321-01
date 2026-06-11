# This is a strategy to make sure a loop ends 
# if an input matches a predetermined value
def main():
    sentinel_value = "EXIT"

    user_input = input("Enter Exit to stop: ")

    # We process the user input to all uppercase
    user_input = user_input.upper()

    # As long the user input is not Exit, we keep looping
    while user_input != sentinel_value:
        user_input = input("Enter Exit to stop: ")
        user_input = user_input.lower()
    
    print("[Program Terminated]")


if __name__ == "__main__":
    main()