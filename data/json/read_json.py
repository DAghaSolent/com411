import json

def read(file_path):
    with open(file_path) as file:
        data = json.load(file)

        city_name = data["city"]
        print(f"City Name: {city_name} \n")
        size = data["population"]
        print(f"Population size: {size} \n")

        for bot in data["bots"]:
            bot_name = bot["name"]
            bot_stats = bot["stats"]
            print(f"{bot_name} has the following stats:{bot_stats}")

def run():
    read("robocity.json")

if __name__ == "__main__":
    run()

