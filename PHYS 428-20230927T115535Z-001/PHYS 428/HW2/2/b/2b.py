# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:45:40 2017

@author: Matt
"""
from math import *
import matplotlib.pyplot as plt
import numpy as np

def f2(x):
    
    f = (2./3.)*x + 1./(x**2.)
    return f
    
def f3(x):
    
    f = 12./(1+x)
    return f

def converge(xn, a, f):
    A = np.zeros(25)
    x0 = 0.
    for n in range(25):
        print('                                                          ',n)
        xn = f(xn)
        print('x')
        print(xn)
        print('')
        print('     |a - xn|')
        print('    ', abs(xn-a))
        print('')
        print('          r')
        print('            ', (log(abs(xn-a)))/(log(abs(x0-a))))
        print('')
        print('')
        print('')
        A[n] = abs(xn-a)
        x0 = xn
    print('_______________________________________________')
    
    plt.xlabel('n')
    plt.ylabel('|a - xn|')
    plt.title('convergence')
    plt.plot(A)
    plt.show()
    return