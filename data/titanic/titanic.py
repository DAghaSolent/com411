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
    elif display_input == 2:
        display_num_survivors()
    elif display_input == 3:
        display_passengers_per_gender()
    elif display_input == 4:
        display_passengers_per_age_group()
    else:
        print("Error! Option not recognised!")

    return display_input

def display_passenger_names():
    print("The names of the passengers are.....")
    for passenger in records:
        passenger_name = passenger[3]
        print(passenger_name)

def display_num_survivors():
    num_survived = 0
    for passenger in records:
        survival_status = int(passenger[1])
        if survival_status == 1:
            num_survived += 1
    print(f"{num_survived} passengers survived")

def display_passengers_per_gender():
    females = 0
    males = 0
    for passenger in records:
        gender = passenger[4]
        if gender == "male":
            males += 1
        else:
            females += 1
    print(f"Females: {females}, Males: {males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for passenger in records:
        if passenger[5] != (""):
            age = float(passenger[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1

    print(f"Children: {children}, Adults: {adults}, Elderly: {elderly}")


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")
    print()
    display_menu()

if __name__ == "__main__":
    run()


