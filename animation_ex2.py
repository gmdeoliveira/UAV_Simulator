import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

i = 1 # Test variable

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'bo')

def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(-1,100)
    return ln,

def update(frame):
    i = 1 # Test variable
    xdata.append(0.5+frame) #+ i)
    ydata.append(frame)
    ln.set_data(xdata, ydata)
    return ln,

anim = FuncAnimation(fig, update, frames=np.linspace(0, 100, 100), init_func=init, blit=True)

plt.show()
