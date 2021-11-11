import matplotlib.pyplot as plt

def displaY(x,y):
    plt.plot(x,y)
    plt.show()

def run():
    print("Running")
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]
    displaY(x_values,y_values)

if __name__ == "__main__":
    run()






