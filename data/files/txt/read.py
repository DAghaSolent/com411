def display_chars(file_path,num_chars):
    with open(file_path) as txt_file:
        text = txt_file.read(5)
        print("The first 5 characters are:")
        print(text)
        print()
def display_line(file_path):
    with open(file_path) as txt_file:
        print("The first line is:")
        text = txt_file.readline()
        print(text)
def display_text(file_path):
    with open(file_path) as txt_file:
        text = txt_file.read()
        print(text)
def run():
    display_chars("library.txt",5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()








