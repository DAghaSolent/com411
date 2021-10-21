import basics.output.simple_message as simple_message
import basics.output.multiline_message as multi_line_message

def run_block_a():
    print("Which program in 'Block A: Basics' Do you wish to run?")
    response = input().lower()
    if response == "simple message":
        simple_message.run()
    elif response == "multi message":
        multi_line_message.run()
    else:
        print("Unknown response please re run the program again")
        print()

def run():
    while(True):
        print("What would you like to do?")
        print("[A] Run 'Block A: Basics' programs")
        print("[Q] Quit")
        response = input().lower()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid Option! Please try again.")
run()



