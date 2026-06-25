import game_logic as gl
import player_option as po
import generate_option as go

# Whenever your import a file
# whatever executable code you have
# inside that file, will be execute as
# as soon as the file is imported
import test #will print "Hello World"

def main():
    player_1 = po.player_option()
    player_2 = go.generate_option()
    gl.game_logic(player_1, player_2)

if __name__ == "__main__":
    main()