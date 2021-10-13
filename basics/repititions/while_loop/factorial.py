print("Please enter a number.")
number = int(input())

# Declare a control Variable
count = 0

# total sum after factoring
total = 1

while count < number:
    count += 1
    total = total * count

print(f"The factorial of {number} is {total}")



