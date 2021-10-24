def export(file_name,num):
    print("Exporting...")
    with open(file_name,'a') as file:
        for value in range(num):
            print("Please enter the id of the bot")
            bot_id = int(input())
            print("Please enter the name of the bot")
            bot_name = input()
            print("Please enter the paint colour for the bot")
            bot_paint = input()
            print()
            data = (f"{bot_id},{bot_name},{bot_paint}\n")
            file.write(data)
    print("Done")

def run():
    export("exported_bots.csv",2)

if __name__ == "__main__":
    run()