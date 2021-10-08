print("Towards which direction should I paint(up,down,left or right)?")

direction = input().lower()

if direction == "up":
    print("I am paining in the upward direction!")
elif direction == "down":
    print("I am paining in the downward direction!")
elif direction == "right":
    print("I am paining in the right direction!")
elif direction == "left":
    print("I am paining in the left direction!")
else:
    print("You are not going in any direction please restart the program.")


