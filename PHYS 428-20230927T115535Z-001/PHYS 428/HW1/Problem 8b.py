#fixed
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
##>>float_formatter = lambda x: "%15f" % x
##>>n.set_printoptions(formatter={'float_kind':float_formatter})
#
#   *I couldn't get this to work

def f(x):
    #computes f(x)
    
    f = D(x) ** D(2.) - D(5.)
    
    return f

def g1(x):
    #computes g1(x)
    
    g = D(5.) / D(x) 
    
    return(g)

def g2(x):
    #computes g1(x)
    
    g = D(x) + (D(f(x)) / D(3.)) 
    
    return(g)

def fixed(x0, r, g):
    #finds root of f(x) by fixed-point method with starting point x0 and selected function g
    
    #initialize table for output as a numpy array
    t = n.zeros((10, 4))
    
    #all computations computed with precision of 15
    getcontext().prec = 15
    
    x = x0
    
    for i in range(r):
        #loop over r steps to find root
        
        #compute g(x)
        x = g(x)
        
        #store results in table
        t[i][0] = i+1
        t[i][1] = x
        t[i][2] = f(x)
        t[i][3] = abs((D(sqrt(5.)) - x))
    
    print('[[        n                xn               f(xn)           |p-xn|         ]]')
    print(t)

print('')
print('__________g1(x)_____________________________')
print('')
    
fixed(2.5, 10, g1)
print('Divergence is expected as |g\'(x)| = 1, where x is root. Convergence requires |g\'(x)| < 1 for all x in [a, b], where [a, b] is the interval containing a fixed point')

print('')
print('__________g2(x)_____________________________')
print('')
    
fixed(2.5, 10, g2)
print('Again, |g\'(x)| is not less than 1 for all x in [a, b] so divergence is expected')
print('')
print('For both g1 and g2, the above statements hold even if the discontinuities are excluded from [a, b]')
