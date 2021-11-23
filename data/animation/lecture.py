import matplotlib.pyplot as plt
import matplotlib.animation as animation

# user-defined function
def animate(frame):
  x = [1, 2, 3, 4, 5]
  y = [2, 4, 6, 8, 10]
  ax.plot(x, y)

# our figure
fig, ax = plt.subplots(1, 1)

# Create an animation using FuncAnimation
some_animation = animation.FuncAnimation(fig, animate, frames=5, interval=2000)

plt.show()
