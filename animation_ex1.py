import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.plot()
xdata, ydata = [], []
ln, = plt.plot([], [], 'bo')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1,1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

anim = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 63), init_func=init, blit=True)

plt.show()
