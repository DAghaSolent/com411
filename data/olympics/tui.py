def started(msg=""):
    for dash in range(86):
        print("-", end="")
    print(f"\nOperation Started: {msg}...")

def completed():
    print("Operation Completed")
    for dash in range(86):
        print("-", end="")

def error(msg):
    print(f"Error! {msg}")

def menu():
    print(f"""Please select one of the following options:
         {"[years]":< 10} List unique years
         {"[tally]":< 10} Tally up medals
         {"[team]":<10} Tally up medals for each team
         {"[exit]":<10} Exit the program
    """"")
    menu_selection = input().lower()
    print(f"Your selection:{menu_selection}")

def display_medal_tally(tally):
    print("Displaying Medal Tally:\n")
    print(f"|{'Gold':< 10}|{tally['Gold']:< 10}|")
    print(f"|{'Silver':< 10}|{tally['Silver']:< 10}|")
    print(f"|{'Bronze':< 10}|{tally['Bronze']:< 10}|")

def display_team_medal_tally(team_tally):
    print("Display Team medal tally:\n")
    for team,tally in team_tally.items():
        print(f"{team}")
        print(f"\tGold:{tally['Gold']},Silver:{tally['Silver']},Bronze:{tally['Bronze']}")

def display_years(years):
    sorted_years = sorted(years,reverse=True)
    for year in sorted_years:
        print(year)