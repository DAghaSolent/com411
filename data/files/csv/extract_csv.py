import csv

def extract(file_path):
    print("Extracting.....",end = "" )
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""

        print("Done!\nThe extracted names are as follow:")
        for values in csv_reader:
            print(values[1])
            values += names

def run():
    extract("bots.csv")

if __name__ == "__main__":
    run()