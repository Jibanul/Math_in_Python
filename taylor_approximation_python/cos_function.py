import time
import pylab as pl
from IPython import display
import numpy as np

def taylor_approx(n):
    x = np.linspace(np.pi*(-3), np.pi*(3),100)
    approx = np.zeros(len(x), dtype=np.dtype('O'))
    for i in range(n):
        
        # print("results", ((-1)**i * (x**(2*i)/np.math.factorial(2*i))).shape)
        # print(np.dtype(((-1)**i) * (x**(2*i)/np.math.factorial(2*i))))
        approx += ((-1)**i) * (x**(2*i)/np.math.factorial(2*i))
        pl.plot(x, np.cos(x))
        pl.plot(x, approx)
        pl.ylim(-1.7,1.7)
        # pl.xlim(-12,12)
        pl.legend(('cos() function', 'Taylor Approximation'), loc = 'upper right')
        plt.text(x = -8, y = 1.25, s = "n = " + str(i), fontsize=15)
        # pl.xlim(-1,1)
        display.clear_output(wait=True)
        display.display(pl.gcf())
        
        plt.clf()
        time.sleep(1.0)        
        # print(i)

taylor_approx(15)