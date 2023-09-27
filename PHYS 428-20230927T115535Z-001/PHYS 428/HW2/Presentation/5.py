# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


    
import numpy as n

#tell numpy to print array completely so that all 'table' values are displayed
n.set_printoptions(threshold=n.nan)

def f(x):
    f = (x**3) + (2*(x**2)) - (3*x) -1
    return(f)

def secant(x0,x1,r):
    #finds root of f(x) by bisection with starting interval [a,b], for r iterations
    
    #initialize table for output as a numpy array
    t = n.zeros((10, 4))
    
    for i in range(r):
        xn = x1 - ((f(x1)*(x1 - x0)) / (f(x1)-f(x0)))
        #store results in table
        t[i][0] = x0
        t[i][1] = x1
        t[i][2] = xn
        t[i][3] = f(xn)
        
        x0 = x1
        x1 = xn
    
    print('[[        x0                x1               xn           f(xn)         ]]')
    print(t)
    
    
#x0 is p0, x1 is p1, r is number of iterations
#divide by zero error if you enter r too high
secant(-2.0001, -3, 3)