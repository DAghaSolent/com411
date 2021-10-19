print("Program started \n")
print("Please enter an ASCII Code")

ascii_code = int(input())

if ascii_code in range(32,127):
    print(f"The character represented by the ASCII code {ascii_code} is {chr(ascii_code)}.Where {ascii_code} is the "
          f"number entered by the user and {chr(ascii_code)} is the ASCII character represented by the number.")
else:
    print("The character you have inputted is more than 1 character long please re run the program and enter 1 "
          "character only")
print()
print("Program Ended")




