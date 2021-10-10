print("Welcome to Sprinkles Gelato, What would you like a waffle or a crepe desert")
dessert = input().lower()

if dessert == "waffle":
    print("So you would like a waffle would you like that with ice cream or whipped cream")
    side = input().lower()
    if (dessert == "waffle") and (side == "ice cream"):
        print("Your final order is a Waffle with a side of Ice cream")
    elif (dessert == "waffle") and (side == "whipped cream"):
        print("Your final order is a Waffle with a side of whipped cream")
    else:
        print("We only serve whipped cream or ice cream with our desserts as a side please re run the order again and "
              "pick either Ice cream or whipped cream")

elif dessert == "crepe":
    print("so you would like a crepe, would you like that with ice cream or whipped cream?")
    side = input().lower()
    if (dessert == "crepe") and (side == "ice cream"):
        print("Your final order is a Crepe with a side of Ice cream")
    elif (dessert == "crepe") and (side == "whipped cream"):
        print("Your final order is a Crepe with a side of whipped cream")
    else:
        print("We only serve whipped cream or ice cream with our desserts as a side please re run the order again")
else:
    print("We only serve waffles and crepes here at sprinkles, please re run the program and choose either a waffle"
          " or a crepe")

print()
print("End of program")