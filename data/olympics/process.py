import tui

COL_MEDAL = 14
COL_TEAM = 6
COL_YEAR = 9

def tally_medals(data):
    tui.started("Displaying Medal Tally")
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for medal in data:
        medal = medal[COL_MEDAL]
        if medal in ("Gold","Silver","Bronze"):
            medals[medal] += 1
    tui.display_medal_tally(medals)
    tui.completed()

def tally_team_medals(data):
    tui.started("Display Team medal tally:")
    team_medals = {}
    for record in data:
        team = record[COL_TEAM]
        collection_medals = record[COL_MEDAL]
        if collection_medals not in("Gold","Silver","Bronze"):
            continue
        if team in team_medals:
            team_medals[team][collection_medals] += 1
        else:
            team_medals[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            team_medals[team][collection_medals] += 1

    tui.display_team_medal_tally(team_medals)
    tui.completed()

def list_years(data):
    tui.started("Listing Years")
    olympic_years = set()
    for record in data:
        olympic_years.add(record[COL_YEAR])
    tui.display_years(olympic_years)
    tui.completed()






