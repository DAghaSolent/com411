#Ask user for number of bars
print("How many bars should be charged")
bars = int(input())
#Declare a control variable
bars_count = 0

print()

#Display bars
while bars_count < bars:
    bars_count += 1
    print(f"Charging:{'█ ' * bars_count}")

print()
print("The battery is fully charged.")
print()
print("End of Program")