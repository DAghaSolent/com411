# ask the user for the age
print("Please enter your age")

# Read the user's response
age = int(input())

# Check if the user is an adult and display an appropriate message
if age >= 18:
    print("You are an adult")
    print("Because you are 18 years old or greater")

elif age >= 13:
    print("You are a teenager")
    print("Because you are 13 or above")

else:
    print("You are a child.")
    print("Because you are below the age of 18")

print("End of Program")
