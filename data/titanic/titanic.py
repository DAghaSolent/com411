import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...", end="")

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
    print("[4] Display the number of passengers per age group")

    display_input = int(input())
    print(f"You have selected option: {display_input}")

    if display_input == 1:
        display_passenger_names()
    else:
        print("Error! Option not recognised!")

    return display_input

def display_passenger_names():
    print("The names of the passengers are.....")
    for passenger in records:
        passenger_name = passenger[3]
        print(passenger_name)

def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")
    print()
    display_menu()

if __name__ == "__main__":
    run()


