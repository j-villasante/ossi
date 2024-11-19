import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

# style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xs = np.linspace(0, 2500, num=2500)

def animate(i):
    buffer = open('current','rb').read()
    ys = np.frombuffer(buffer, dtype=np.short)
    
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()