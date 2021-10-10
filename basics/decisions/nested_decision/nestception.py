#Ask user for place
print("Where should I look")
look = input().lower()

#Check the bedroom
if look == "in the bedroom":
    print("Where in the bedroom should I look?")
    bedroom_look = input().lower()
    if bedroom_look == "under the bed":
        print("Found some shoes but no battery.")
    else:
        print("Found some mess but no battery")
#Check the bathroom
elif look == "in the bathroom":
    print("Where in the bathroom should I look?")
    bathroom_look = input().lower()
    if bathroom_look == "in the bathtub":
        print("Found a rubber ducky but no battery")
    else:
        print("Found a wet surface but no battery")
#Check the lab
elif look == "in the lab":
    print("Where in the lab should I look?")
    lab_look = input().lower()
    if lab_look == "on the table":
        print ("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")
#Handle unkowwn place
else:
    print("I do not know where that is but I will keep looking")

print("\n")
print("End of Program")









