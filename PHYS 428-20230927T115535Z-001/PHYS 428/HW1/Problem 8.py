from math import copysign
from decimal import *
from decimal import Decimal as D

def f(x):
    #computes f(x)
    
    f = D(x) ** D(2.) - D(5.)
    
    return f

def bisect(a, b, r):
    #finds root of f(x)
    
    #all computations computed with precision of 15
    getcontext().prec = 15
    
    for i in range(r):
        
        m = D(a) + D(0.5) * (D(b) - D(a))
        
        if copysign(1.0, f(a)) == copysign(1.0, f(m)):
           
            a = m
        
        else:
            
            b = m   
              
    print('The function has a root at x = ', '{0:.15f}'.format(m))
    
bisect(2., 3., 10)
