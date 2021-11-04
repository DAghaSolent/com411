def pattern():
    data = {"Short Sequence": 3,
            "Medium Sequence": 2,
            "Long Sequence": 1
            }
    return data

print("Dictionary:")
print(f"{pattern()}\n")

def display_keys(data):
    print("Keys:")
    for value in data:
        print(value)
    print()

def display_values(data):
    print("Values:")
    for value in data:
        print(data[value])
    print()

def display_items(data):
    print("Pairs:")
    for value in data.items():
        print(f"{value[0]}: {value[1]}")

def run():
    data = pattern()
    display_keys(data)
    display_values(data)
    display_items(data)

if __name__ == "__main__":
    run()


