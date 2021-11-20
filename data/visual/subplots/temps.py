import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import csv

temperatures = []
day = []


def read_data(file_path):
    print("Loading Data....", end="")

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)
        for line in csv_reader:
            temperatures.append(int(line[0].strip()))
            day.append(int(line[1].strip()))

    return temperatures


def run():
    data = read_data('temps.csv')
    fig, axes = plt.subplots(1, 2)
    y = day
    x = temperatures
    axes[0].plot(x, y)
    axes[0].xaxis.set_major_locator(MultipleLocator(1))
    axes[1].bar(x, y)
    axes[1].xaxis.set_major_locator(MultipleLocator(1))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()
