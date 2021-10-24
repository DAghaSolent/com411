def search(file_name):
    print("Searching....",end= "")
    sections = ""
    books = "Books:\n"

    with open(file_name) as file:
        for reading in file:
            if reading.startswith("Section"):
                sections += reading
            else:
                books += reading
    print("Done")
    return (f"{sections}\n\n{books}")

def save(file_name, stored):
    print("Saving....", end= "")
    with open(file_name,'w') as file:
        file.write(stored)
    print("Done!")


def run():
    stored = search("books.txt")
    save("books_example.txt",stored)

if __name__ == "__main__":
    run()





