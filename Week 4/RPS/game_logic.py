import translate as tr

def game_logic(player_1, player_2):
    print(f"Player 1 chose: {tr.translate(player_1)}")
    print(f"Player 2 chose: {tr.translate(player_2)}")

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