print("What level of brightness is required?")
brightness = int(input())

print("Adjusting Brightness... \n")

for brightness in range(2,brightness +1,2):
    print(f"Beep's Brightness level: {'*' * brightness}")
    print(f"Bop's Brightness levelL {'*' * brightness} \n")

print("Adjustments complete!")


