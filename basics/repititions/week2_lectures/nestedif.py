#Ask the use if it is sunny and breezy
print("Is it sunny?")
is_sunny = input().lower()

print("Is there a breeze?")
is_breeze = input().lower()

if is_sunny == "yes":
    if is_breeze == "yes":
        print("Clothes are Dry")
    else:
        print("Clothes are drying slowly")
else:
    print("Clothes are not dry")