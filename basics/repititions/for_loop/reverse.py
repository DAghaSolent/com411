print("What phrase do you see?")
phrase = input()

print("Reversing... \n")
print("The phrase is:", end= " ")

for index in range(len(phrase)-1,-1,-1):
    print(phrase[index], end="")
print()
