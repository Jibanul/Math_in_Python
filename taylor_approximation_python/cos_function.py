import time
import pylab as pl
from IPython import display
import numpy as np

def taylor_approx(n):
    x = np.linspace(np.pi*(-3), np.pi*(3),100)                          # values of x from -3*pi to 3*pi 
    approx = np.zeros(len(x), dtype=np.dtype('O'))
    for i in range(n):
        approx += ((-1)**i) * (x**(2*i)/np.math.factorial(2*i))         # taylor series of cos(x)
        pl.plot(x, np.cos(x))
        pl.plot(x, approx)
        pl.ylim(-1.7,1.7)
        pl.legend(('cos() function', 'Taylor Approximation'), loc = 'upper right')
        pl.text(x = -8, y = 1.25, s = "n = " + str(i), fontsize=15)
        display.clear_output(wait=True)
        display.display(pl.gcf())
        pl.clf()
        time.sleep(1.0)        # pause 1 sec before ploting the next curve

# call the function
taylor_approx(n = 13)
