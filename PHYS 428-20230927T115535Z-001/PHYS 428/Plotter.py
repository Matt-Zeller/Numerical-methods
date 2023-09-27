
import matplotlib.pyplot as plt
import numpy as np

#function to be plotted
def f1(x):
    f=(x**4)-6*(x**3)+11*(x**2)-6*x
    return f

def f2(x):
    f=4*(x**3)-18*(x**2)+22*x-6
    return f

def f3(x):
    f=np.exp(x)
    return f

def p3(x):
    f=0.8455*(x**3)-1.060*(x**2)+1.933*x+1.
    return f

def plotter(f,a,b,h):
#takes function of variable 'x',lower bound and upper bound a,b, step h
#then plots it

    #first point function f is eval'd at
    x=a
    #array size
    arSize=np.int(np.abs((a-b)/h))
    #init array of function values
    F=np.zeros((arSize,1))
    #fill array of func values at all x in a,b
    for i in range(arSize):
        F[i,0]=f(x)
        x=x+h
    #make x axis array, plot f(x)
    X=np.arange(a,b,h)
    plt.plot(X,F)

#type function of x here... right now it is set to plot 
#for x=[0,3] at increments of 0.01


plotter(f1,0.,3.,0.01)
plotter(f2,0.,3.,0.01)
plotter(f3,0.,3.,0.01)
plotter(p3,0.,3.,0.01)

