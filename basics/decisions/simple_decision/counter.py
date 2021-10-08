print("Please enter the first whole number")
first_num = int(input())

print("Please enter the second whole number")
second_num = int(input())

print("Please enter the third whole number")
third_num = int(input())

even_count = 0
odd_count = 0

if first_num % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if second_num % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if third_num % 2 == 0:
    even_count += 1
else:
    odd_count += 1

print(f"The program has been completed.There are {even_count} even numbers found and {odd_count} odd numbers found")