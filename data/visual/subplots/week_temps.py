import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def read_data(file_path):
    print("Loading Data....", end="")
    temps = {}

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)
        temps = {'week1': [], 'week2': []}

        for line in csv_reader:
            temps['week1'].append(float(line[0].strip()))
            temps['week2'].append(float(line[1].strip()))
    return temps


def run():
    data = read_data('temps2.csv')
    fig, axes = plt.subplots(1, 2)
    x = list(range(1, 8))
    axes[0].plot(x, data['week1'])
    axes[0].xaxis.set_major_locator(MultipleLocator(1))
    axes[1].plot(x, data['week2'])
    axes[1].xaxis.set_major_locator(MultipleLocator(1))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()
