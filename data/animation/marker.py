import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
    global ax
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)
    ax.plot(frame, frame, "ro")


fig, ax = plt.subplots()

def run():
    global fig
    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000, repeat=False)
    plt.show()

if __name__ == "__main__":
    run()

