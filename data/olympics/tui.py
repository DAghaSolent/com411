def started(msg=""):
    for dash in range(86):
        print("-",end="")
    print(f"\nOperation Started: {msg}...")

started("Reading data from athlete_events.csv")

def completed():
    print("Operation Completed")
    for dash in range(86):
        print("-",end="")

def error(msg):
    print(f"Error! {msg}")

error("Invalid Selection!")

def menu():
    print("Please select one of the following options:\n\n"
          "[years] List unique years\n"
          "[tally] Tally up medals\n"
          "[team] Tally up medals for each team\n"
          "[exit] Exit the program\n")

    print(f"Your selection: ")

def display_medal_tally(tally):
    print("Displaying Medal Tally:\n")
    medal_tally = {"Gold":10,"Silver":5,"Bronze":2}
    print(medal_tally)

display_medal_tally()

def display_team_medal_tally(tally):
    print("Display Team medal tally:\n")
    team_medal_tally = {
                        "Denmark/Sweden":{"Gold":6,"Silver":0,"Bronze":2},
                        "Finland":{"Gold":198,"Silver":263,"Bronze":415},
                        "Norway":{"Gold":299,"Silver":330,"Bronze":281},
                        "Satchmo":{"Gold":1, "Silver":0, "Bronze":0},
                        "Tonga":{"Gold":0, "Silver":1, "Bronze":0},
                        "Digby":{"Gold":0, "Silver":0, "Bronze":1},
                        }
    print(team_medal_tally)

display_team_medal_tally()

def display_years(years):
    sorted_years = sorted(years,reverse=True)
    for year in sorted_years:
        print(year)