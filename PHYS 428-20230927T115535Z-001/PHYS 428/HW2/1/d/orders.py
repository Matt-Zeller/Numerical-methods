# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:17:30 2017

@author: Matt
"""
from math import *
from numpy import *
import matplotlib.pyplot as plt

def f():
    
    
    A = zeros(400)
    B = arange( -2, 2, .01)
    
    
    for n in range(400):
        fatx = cos(pi*(B[n])/2)
        A[n]=(fatx)
    
    return(B, A)

def poly(x, deg):
    
    c = 2/pi
    f = 0
    
    for n in range(deg):
        
        g = (((-1)**(n))*(c**(4*n))*(x**(2*n)))/factorial(2*n)
        
        f = f + g

    return f

def points(deg):
    A = zeros(400)
    B = arange( -2, 2, .01)
    
    for n in range(400):
        fatx = poly(B[n], deg)
        A[n]=(fatx)
        
    return(B, A)

B, A = f()
C, D = points(7)
E, F = points(5)
G, H = points(3)
I, J = points(1)


    
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Actual function')
plt.axis([-2, 2, -1, 2])
plt.plot(B, A)
plt.show()

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('7th Order')
plt.axis([-2, 2, -1, 2])
plt.plot(C, D)
plt.show()

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('5th Order')
plt.axis([-2, 2, -1, 2])
plt.plot(E, F)
plt.show()

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('3rd Order')
plt.axis([-2, 2, -1, 2])
plt.plot(G, H)
plt.show()

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('1st Order')
plt.axis([-2, 2, -1, 2])
plt.plot(I, J)
plt.show()

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Actual Function and All Orders')
plt.axis([-2, 2, -1, 2])
plt.plot(B, A, C, D , E, F, G, H, I, J)
plt.show()