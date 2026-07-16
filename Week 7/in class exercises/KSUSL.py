class team:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def win(self):
        self.points += 3
    
    def draw(self):
        self.points += 1
    
    def get_name(self):
        return self.name
    
    def get_points(self):
        return self.points
    
def print_table(teams):
    teams = list(teams.values())
    teams = sort_table(teams)
    print("Name\tPts.")
    print("--------------")
    for team in teams:
        print(f"{team.name}\t {team.points}")

def sort_table(teams):
    for x in range(len(teams)):
        for index in range(len(teams) - x - 1):
            if teams[index].points < teams[index + 1].points:
                #swap
                temp = teams[index]
                teams[index] = teams[index + 1]
                teams[index + 1] = temp

    return teams

    # teams = teams.sort(key=lambda x: x.points, reverse=True)

    
def main():
    teams = {1: team("Team 1"), 2: team("Team 2"), 3: team("Team 3"), 4: team("Team 4")}

    games = [
        [(1, 2), (3, 4)],
        [(1, 3), (2, 4)],
        [(1, 4), (2, 3)],
        [(2, 1), (4, 3)],
        [(3, 1), (4, 2)],
        [(4, 1), (3, 2)]
    ]

    print_table(teams)

    print()

    for week in games:
        for game in week:
            print(f"[Home]{teams[game[0]].name} vs [Away]{teams[game[1]].name}")
            was_draw = input("Was this game a draw? (Y/N): ") == "Y"

            if was_draw == True:
                teams[game[0]].draw()
                teams[game[1]].draw()
            else:
                winner = input("Which team won? (Home or Away): ")

                if winner == "Home":
                    teams[game[0]].win()
                elif winner == "Away":
                    teams[game[1]].win()
            print()
        
        print_table(teams)
        print()


if __name__ == "__main__":
    main()
