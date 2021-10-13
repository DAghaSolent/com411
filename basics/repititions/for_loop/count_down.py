# Ask user for distance
print("How far are we from the cave?")
count_down = int(input())

# Display count down
print()

for count_down in range(count_down,0,-1):
    print(f"{count_down} steps remaining")

print()
print("We have reached the cave!")

