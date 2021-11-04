def observed():
    observations = []
    for count in range(5):
        observations.append(input("Please enter an observation: "))
    return observations

def remove_observations(observations):
    print("Would you like to remove a observation yes/no")
    remove = input().lower()
    if remove == "yes":
        print("Please enter an observation you would like to remove")
        observation_removed = input()
        observations.remove(observation_removed)
        return observation_removed

def run():
    seen_observations = observed()
    remove_observations(seen_observations)
    print("Observations:")
    for city in seen_observations:
        print(f"{city} observed: {seen_observations.count(city)} times")

if __name__ == "__main__":
    run()







