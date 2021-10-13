# Ask user for number
print("How many numbers should I sum up?")
initial_num = int(input())

# Declare a control variable
count = 1

# Sum Numbers
total = 0

while count <= initial_num:
    print(f"Please enter number {count} of {initial_num}:")
    number = int(input())
    total = total + number
    count += 1

print(f"The answer is {total}")






