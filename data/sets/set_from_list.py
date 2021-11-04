def observed():
    observations = []
    for index in range(3):
        observations.append(input("Please enter a observation:"))
    return observations

def run():
    print("Counting observations....")
    captured_observations = observed()
    empty_set = set()
    for value in captured_observations:
        empty_set.add((value,captured_observations.count(value)))

    for city in empty_set:
        print(f"{city[0]} observed{city[1]}")

if __name__ == "__main__":
    run()



