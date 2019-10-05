from matplotlib import pyplot as plt
import numpy as np
def pl():
    x=np.arange(0, 3*np.pi, 0.1)
    print(x)
    y=np.sin(x)
    print(y)
    plt.plot(x, y)
    plt.show()
pl()