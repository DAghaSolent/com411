# definition of function
def get_name():
    print("Please enter your name")
    name = input()
    return name

def display_name():
    print(f"***{get_name()}***")



print()

print("Please enter your weight")
weight = float(input())

print("Please enter your height")
height = float(input())

bmi = weight / (height ** 2)
print(f"{name}your bmi is {bmi}")
