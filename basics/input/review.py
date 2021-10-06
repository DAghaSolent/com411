#Asks user their name and welcomes them to the program
print("Welcome to the simple calculator program. May I ask you what is your name?")
name = input()

#Asks user favourite number
print("What is your favourite number")
favourite_num = int(input())

#Asks user least favourite number
print(f"What is your least favourite number")
least_favourite_num = int(input())

#Favourite Number minus Least favourite number
#answer = favourite_num - least_favourite_num
#We could put a variable like this above to basically do the calculation we want. But we would be repeating it. So it would be wise to do the operatin in the print below.

print(f"Hello their {name}. Your favourite number is {favourite_num} and your least favourite number is {least_favourite_num}")
print(f"Your favourite number {favourite_num} minus {least_favourite_num} = {favourite_num - least_favourite_num}")






