import random
def player_option():
    while True:
        option = input("Enter R, P, or S: ")

        if option != 'R' and option != 'P' and option != 'S':
            print("Please only enter R, P, or S. Try again!")
        else:
            # Return statement resolves the function call
            # into a value
            return option

def translate(letter):
    if letter == 'R':
        return "Rock"
    elif letter == 'P':
        return "Paper"
    elif letter == "S":
        return "Scissors"

# This function randomly returns either "R", "P", "S"
def generate_option():
    return random.choice(["R", "P", "S"])    

def game_logic(player_1, player_2):
    print(f"Player 1 chose: {translate(player_1)}")
    print(f"Player 2 chose: {translate(player_2)}")

    match player_1:
        case 'R':
            match player_2:
                case 'R':
                    print("Draw")
                case 'P':
                    print("Player 2 won!")
                case 'S':
                    print("Player 1 won!")
        case 'P':
            match player_2:
                case 'R':
                    print("Player 1 won!")
                case 'P':
                    print("Draw")
                case 'S':
                    print("Player 2 won!")
        case 'S':
            match player_2:
                case 'R':
                    print("Player 2 won!")
                case 'P':
                    print("Player 1 won!")
                case 'S':
                    print("Draw")
        
def main():
    player_1 = player_option()
    player_2 = player_option()
    game_logic(player_1, player_2)

if __name__ == "__main__":
    main()