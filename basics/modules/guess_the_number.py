import random

print("Please enter the minimum value")
min_value = int(input())
print("Please enter the maximum value")
max_value = int(input())

random_number = random.randrange(min_value,max_value,1)

print(f"I am thinking of a number between{min_value} and {max_value} .Can you guess what it is? where {min_value} and "
      f"{min_value} and {max_value} are the minimum and maximum values specified by the user.")

is_looping = True
while is_looping == True:
    guess = int(input())
    if guess < random_number:
        print("Your guess is too low")
        print()
        print("Try again")
    elif guess > random_number:
        print("Your guess is to high")
        print()
        print("Try again")
    elif guess == random_number:
        print("Congratulations! You guessed my number!")
        is_looping = False






