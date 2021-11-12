import matplotlib.pyplot as plt
import random as rnd

def data():
    paths = {}

    print("Please enter a type of line you would like to create: (:, -- or -)")
    line = input()

    print("Please enter what colour you would like the type of line to be: (r, g or b)")
    colour = input()

    print("Please enter what style of marker you would like to use: ( o, s or ^)")
    marker = input()

    paths['line_style'] = line
    paths['colour'] = colour
    paths['marker'] = marker

    return paths

def generate():
    print("How many lines would you like to display?")
    user_lines = int(input())


    for lines in range(user_lines):

        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)

        format = f"{values['colour']}{values['line_style']}{values['marker']}"
        plt.plot(x, y, format)

    plt.show()

def run():
    print("Running......")
    generate()
    print("Done!")

run()