print("What phrase do you see?")
phrase = input()

print("Reversing... \n")
print("The phrase is:", end ="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)
print()
print("End of program")