

import matplotlib.pyplot as plt
import numpy as np

#plots a function

x=0.

p3=np.zeros((300,1))
for i in range(300):
    
    #type function of x here... right now it is set to plot 
    #for x=[0,3] at increments of 0.01
    p3[i,0]=4*(x**3)-18*(x**2)+22*x-6
    x=x+0.01

x=np.arange(0., 3., 0.01)

plt.plot(x,p3)


