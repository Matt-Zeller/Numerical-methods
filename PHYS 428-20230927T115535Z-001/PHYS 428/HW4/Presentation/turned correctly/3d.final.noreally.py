#problem 3d
#Matt Zeller
#PHYS 428
#7 August 2017

import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

#plots |f(x) - P3(x)| to show the maximum value for x=[0,3]

#initialize x
x=0.

#initialize error arrays to be plotted
error=np.zeros((300,1))
derror=np.zeros((300,1))

#compute error at 300 points, step size 0.01
for i in range(300):
    
    #|f(x) - P3(x)|
    error[i,0]=(1./24.)*np.abs(np.exp(3)*((x**4)-6*(x**3)+11*(x**2)-6*x))
    #d/dx [error]
    derror[i,0]=(1./24.)*np.abs(np.exp(3)*(4*(x**3)-18*(x**2)+22*x-6))

    #step
    x=x+0.01


#build array of x for matplotlib to plot
x=np.arange(0., 3., 0.01)

#plot error and derror
plt.figure(1)
plt.subplot(211)
plt.plot(x,error)
plt.axis([0,3,0,1])
plt.grid(True)
plt.ylabel('|f(x) - P3(x)|  =  E')
plt.title('Error for Third Degree Interpolating Polynomial P3(x) About the Function exp(x)')
plt.show()

#print out the max value of array error
print('The maximum error bound is approximately...', LA.norm(error,np.inf))


##plots derivative of error function if desired
#plt.subplot(212)
#plt.plot(x,derror)
#plt.axis([0,3,0,0.5])
#plt.grid(True)
#plt.xlabel('x')
#plt.ylabel('d/dx (E)')




