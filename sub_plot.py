from matplotlib import pyplot as plt
import numpy as np
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)


plt.subplot(211) #2 indicates o/p has two graphs ,1 indicates the o/p has one graph horizontally ,1 indicates this is the first graph to be disaplyed on screen
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(212)#2 indicates o/p has two graphs ,1 indicates the o/p has one graph horizontally ,2 indicates this is the second graph to be dispalyed on screen
plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()
