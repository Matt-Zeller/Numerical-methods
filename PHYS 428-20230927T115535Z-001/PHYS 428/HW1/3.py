# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:17:30 2017

@author: Matt
"""
from math import *
from numpy import *

def f():
    
    
    A = zeros(200)
    B = arange( -1, 1, .01)
    
    
    for n in range(200):
        fatx = cos(pi*(B[n])/2)
        A[n]=(fatx)
        print(fatx)
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Approximating with Taylor Polynomials')
    plt.plot(B, A)
    plt.show()