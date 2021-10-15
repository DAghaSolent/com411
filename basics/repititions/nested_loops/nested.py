print("How many rows should I have?")
rows = int(input())
print()
print("How many columns should I have?")
columns = int(input())
print()

for count in range(rows):
    for index in range(columns):
        print(":-)", end=" ")
    print()
