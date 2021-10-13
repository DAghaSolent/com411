#Ask the use if it is sunny and breezy
print("Is it sunny?")
is_sunny = input().lower()

print("Is there a breeze?")
is_breeze = input().lower()

if is_sunny == "yes" and is_breeze == "yes":
    print("Clothes are Dry")
elif is_sunny == "yes" and is_breeze == "no":
    print("Clothes are drying slowly")
else:
    print("Clothes are not dry")