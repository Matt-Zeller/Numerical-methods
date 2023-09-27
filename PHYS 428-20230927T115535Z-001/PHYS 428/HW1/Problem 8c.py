#newt
#MATT ZELLER
#JUNE 19 2017
#PHYS 428

import numpy as n
from math import copysign, sqrt
from decimal import *
from decimal import Decimal as D

#tell numpy to print array completely so that all 'table' values are displayed
n.set_printoptions(threshold=n.nan)

#tell numpy to print 'table' values with 15 digits
float_formatter = lambda x: "%.15f" % x
n.set_printoptions(formatter={'float_kind':float_formatter})
#   *I couldn't get this to work quite right

def f(x):
    #computes f(x)
    
    f = D(x) ** D(2.) - D(5.)
    
    return f

def df(x):
    #computes the analytical derivative of f(x)
    
    df = D(2.) * D(x)
    
    return df

def newt(x, r):
    #finds root of f(x) by Newton's Method with starting point x
    
    #initialize table for output as a numpy array
    t = n.zeros((10, 4))
    
    #all computations computed with precision of 15
    getcontext().prec = 15

    for i in range(r):
        #loop over r steps to find root
        
        #compute xn
        x = D(x) - (f(x) / df(x))
        
        #store results in table
        t[i][0] = i+1
        t[i][1] = x
        t[i][2] = f(x)
        t[i][3] = abs((D(sqrt(5.)) - x))
    
    print('[[        n                xn               f(xn)           |p-xn|         ]]')
    print(t)
    
newt(2.5, 10)
print('These values show bisection method converges much more slowly than fixed-point Newton\'s method')
