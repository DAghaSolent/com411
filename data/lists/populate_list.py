def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    path = directions()
    for index in range(len(path)):
        print(f"{index}: {path[index]}")
    print()
    chosen_path = int(input())
    return path[chosen_path]

def run():
    route = []
    print("Working out escape route...")
    for index in range(5):
        route.append(menu())
    print(f"Escape route {route}")

if __name__ == "__main__":
    run()


