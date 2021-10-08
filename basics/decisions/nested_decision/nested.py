print("What type of cover does the book have?")
book_cover = input().lower()

if book_cover == "soft":
    print("Is the soft cover perfect bound?")
    perfect_bound = input().lower()
    if perfect_bound == "yes":
        print("Soft cover,perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif book_cover == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("You have not inputted a book cover please re run the program and input a 'hard' or 'soft' copy into the program")




