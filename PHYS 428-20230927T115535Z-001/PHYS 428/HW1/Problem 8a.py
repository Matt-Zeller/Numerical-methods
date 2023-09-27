#bisect
#MATT ZELLER
#JUNE 19 2017
#PHYS 428

import numpy as n
from math import copysign, sqrt
from decimal import *
from decimal import Decimal as D

#tell numpy to print array completely so that all 'table' values are displayed
n.set_printoptions(threshold=n.nan)

#tell numpy to print 'table' values with 15 decimal points
float_formatter = lambda x: "%.15f" % x
n.set_printoptions(formatter={'float_kind':float_formatter})

def f(x):
    #computes f(x)
    
    f = D(x) ** D(2.) - D(5.)
    
    return f

def bisect(a, b, r):
    #finds root of f(x) by bisection with starting interval [a,b]
    
    #initialize table for output as a numpy array
    t = n.zeros((10, 4))
    
    #all computations computed with precision of 15
    getcontext().prec = 15
    
    for i in range(r):
        #loop over r steps to find root
        
        #compute midpoint m between a and b
        m = D(a) + D(0.5) * (D(b) - D(a))
        
        #check if midpoint has passed root
        if copysign(1.0, f(a)) == copysign(1.0, f(m)):
           
            a = m
        
        else:
            
            b = m   
        
        #store results in table
        t[i][0] = i+1
        t[i][1] = m
        t[i][2] = f(m)
        t[i][3] = abs((D(sqrt(5.)) - m))
    
    print('[[        n                xn               f(xn)           |p-xn|         ]]')
    print(t)
    
bisect(2., 3., 10)
print('These values show bisection method converges much more slowly than fixed-point Newton\'s method')
