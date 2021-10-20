def display_in_a_box(phrase):
    print("-" * 4)
    print(f"{phrase}")
    print("-" * 4)
    print()

def display_in_lower_case(phrase):
    print(f"{phrase.lower()}")
    print()

def display_upper_case(phrase):
    print(f"{phrase.upper()}")
    print()

def display_mirrored(phrase):
    for index in range(len(phrase)-1,-1,-1):
        print(phrase[index], end="")
    print()

def repeat_word(phrase):
    print("How many times would you like to repeat your phrase")
    repeat = int(input())
    count = 0
    while count < repeat:
        count += 1
        print(f"{phrase.lower()}")
        print(f"{phrase.upper()}")
        print()

def run():

    while(True):
        print("Please enter a phrase")
        phrase = input()
        print("Read the following options and input a number between 1-5 to display your phrase in a different way")
        print()
        print("Press 1 to display your phrase in an ascii art box")
        print("Press 2 to display your phrase in lower case")
        print("Press 3 to display your phrase in upper case")
        print("Press 4 to display your phrase in reverse")
        print("Press 5 to repeat your phrase")
        print("Press 6 to quit the program")
        command = input()

        if command == "1":
            display_in_a_box(phrase)
        elif command == "2":
            display_in_lower_case(phrase)
        elif command == "3":
            display_upper_case(phrase)
        elif command == "4":
            display_mirrored(phrase)
        elif command == "5":
            repeat_word(phrase)
        elif command == "6":
            print("Program Terminated")
            break
        else:
            print("Unknown Option")
            print()

run()