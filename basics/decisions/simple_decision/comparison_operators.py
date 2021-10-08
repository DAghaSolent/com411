print("User please enter first number?")
first_num = int(input())

print("User please enter second number?")
second_num = int(input())

if first_num < second_num:
    print("The first number is the smallest!")
elif second_num < first_num:
    print("The second number is the smallest")
else:
    print("Both numbers are equal")

print("End of program.")

