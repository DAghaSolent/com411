import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def read_data():
    print("Loading Data....", end="")
    with open('titanic.csv') as file:
        file = csv.reader(file)
        headings = next(file)
        titanic_dictionary = {'survived': [], 'sex': [], 'age': [], 'fare': []}

        for line in file:
            if (line[1] != "") and (line[14] != "") and (line[4].strip() != "") and (line[8].strip() != ""):
                titanic_dictionary['survived'].append(int(line[1].strip()))
                titanic_dictionary['sex'].append(int(line[14].strip()))
                titanic_dictionary['age'].append(float(line[4].strip()))
                titanic_dictionary['fare'].append(round(float(line[8].strip()), 2))
    return titanic_dictionary

def survived_vs_sex():
    data = read_data()
    sex = {'male': 0, 'female': 0}
    print(data)
    for line in data:
        if line[1] == 1:
            if line[14] == '0':
                sex['male'] += 1
            elif line[14] == '1':
                sex['female'] += 1
    return sex


def run():
    data = read_data()
    fig, axes = plt.subplots(2, 2)
    axes[0, 0].bar(data['survived'], data['sex'])
    axes[0, 1].bar(data['survived'], data['age'])
    axes[1, 0].plot(data['survived'], data['fare'])
    axes[1, 1].plot(data['age'], data['fare'])
    plt.tight_layout()
    plt.show()

print(survived_vs_sex())

if __name__ == "__main__":
    run()

