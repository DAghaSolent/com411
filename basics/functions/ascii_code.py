print("Program started: \n")
print("Please enter a standard character:")
character = input()

if len(character) <= 1:
    ascii = (ord(character))
    print(f"The ASCII code for {character} is {ascii}.")
else:
    print("The character you have inputted is more than 1 character long please re run the program and enter 1 "
          "character only")
print()
print("Program Ended!")
