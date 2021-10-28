import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...")

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)
        for line in csv_reader:
            records.append(line)
    print("Done!")

def display_menu():
    print("Please Select one of the following options:")
    print("[1] Display the names of all passengers")
    print("[2] Display the number of passengers that survived")
    print("[3] Display the number of passengers per age group")

    diplay_input = int(input())
    if display_input == 1:



def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

if __name__ == "__main__":
    run()


