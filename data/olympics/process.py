import tui

def list_years(data):
    olympic_years = set()
    for year in data:
        years = data[9]
        olympic_years.add(years)
    return olympic_years

def tally_medals(data):
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for medal


