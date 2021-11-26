import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

boxes = []


def init():
    boxes.append({'x': [3, 3, 4, 4, 3], 'y': [3, 4, 4, 3, 3]})
    boxes.append({'x': [2, 2, 5, 5, 2], 'y': [2, 5, 5, 2, 2]})
    boxes.append({'x': [1, 1, 6, 6, 1], 'y': [1, 6, 6, 1, 1]})


def animate(frame):
    global ax
    print(frame)
    ax.plot(boxes[frame]['x'], boxes[frame]['y'])


def run():
    global fig
    init()
    some_animation = animation.FuncAnimation(fig, animate, frames=3, interval=1000)
    plt.show()


if __name__ == "__main__":
    run()