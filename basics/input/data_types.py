#To get users name
print("What is your name human?")
name = input()

#To get how old they are
print("How old are you (in years)?")
age = int(input())

#To get how tall they are
print("How tall are you(in metres)?")
height = float(input())

#To get their weight
print("How much do you weigh (in kilograms)?")
weight = int(input())

#To calculate BMI(Body Mass Index)
bmi = round(float(weight / (height ** 2)),2)


#Final code that displays result
print(f"{name} you are {age} years old and your bmi is {bmi}")



