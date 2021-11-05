import csv
import process
import tui

def read_data(file_path):
    with open(file_path) as csv_file:
        csv_reader  = csv.reader(csv_file)
        headings = next(csv_reader)
        data = []
        for line in csv_reader:
            data.append(line)
        return data
def run():
    pass
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu().lower
        if selection == "years":
            pass
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection")

if __name__ == "__main__":
    run()

