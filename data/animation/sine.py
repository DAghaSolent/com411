import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


def animate(frame):
    global ax
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)

    x = range(0, frame)
    y = []

    for degrees in x:
        y.append(math.sin(math.radians(degrees)))

    ax.plot(x, y)


fig, ax = plt.subplots()


def run():
    global fig
    some_animation = animation.FuncAnimation(fig, animate, frames=720, interval=10, repeat=False)
    plt.show()


if __name__ == "__main__":
    run()

