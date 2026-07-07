# Using 1-dimensional and 2-dimensional lists
# 1. Ask the user to input 10 numbers (using a loop) and store the inputs in a list
# 2. Give the user the option to delete or change a number in the list
# 2.1 Print out all 10 numbers with the index printed as a prefix
# 2.2 Ask the user to select an index
# 2.3 Perform the requested action
# 3. Within the options, let the user revert the last operation (ctrl/command + Z)
# 3.1 The program should remember the last 2 actions
# 4. After each action, print the list of numbers (horizontally)
def print_list_index(numbers):
    for x in range(len(numbers)):
        print(f"{x} -> {numbers[x]}")
    print()

def delete_number(index, numbers):
    del numbers[index]

def update_number(index, new_number, numbers):
    numbers[index] = new_number

def main():
    saved_numbers = []

    last_actions = []

    for i in range(10):
        input_number = int(input("Enter a number: "))
        saved_numbers.append(input_number)

    while True:
        print("1. Delete a number")
        print("2. Change a number")
        print("3. Undo/Revert last action")
        print("4. Exit")
        usr_action = int(input("> "))

        print()

        if usr_action == 1:
            print("Choose an index")
            print_list_index(saved_numbers)
            usr_sel = int(input("> "))

            last_actions.append([usr_action, saved_numbers[usr_sel], usr_sel])

            delete_number(usr_sel, saved_numbers)

        elif usr_action == 2:
            print("Choose an index")
            print_list_index(saved_numbers)
            usr_sel = int(input("> "))

            new_number = int(input("Enter the new number: "))

            last_actions.append([usr_action, saved_numbers[usr_sel], usr_sel])

            update_number(usr_sel, new_number, saved_numbers)
        elif usr_action == 3:
            action = last_actions[len(last_actions) - 1]

            if action[0] == 1:
                print(f"Undoing a remove, index {action[2]}, number {action[1]}")
                saved_numbers.insert(action[2], action[1])
            elif action[0] == 2:
                print(f"Undoing a change, index {action[2]}, number {action[1]}")
                update_number(action[2], action[1], saved_numbers)

            del last_actions[len(last_actions) - 1]
        elif usr_action == 4:
            break
        
        print(saved_numbers)
        print(last_actions)
        
        print()
    
if __name__ == "__main__":
    main()