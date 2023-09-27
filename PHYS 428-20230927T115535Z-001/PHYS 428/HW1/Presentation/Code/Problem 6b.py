#CntrDiff
#MATTHEW ZELLER
#06/19/17
#PHYS 428

#Problem 6b

import numpy as np
import math as m
import cmath as cm
import matplotlib.pyplot as p

def CntrDiff(x):
#Initialize arrays
    A = np.zeros((6, 6))
    H = np.zeros(6)
    E = np.zeros(6)
    
#Loop over n step size's
    for n in range(6):
    
    #Store h at [n][1]
        h = 2 ** (-(n+1))
        A[n][0] = h
        H[n]    = np.real(cm.log10(h))
        
    #Compute Df
        Df = (m.sin(x + h) - m.sin(x - h)) / 2*h
    
    #Compute error...
        e = (m.cos(x) - Df)
        
    #...and error per step size
        a = e / h
        b = a / h
        c = b / h
        
    #Store values
        A[n][1] = Df
        A[n][2] = e
        A[n][3] = a
        A[n][4] = b
        A[n][5] = c
        
        E[n] = np.real(cm.log10(e))
    
    return (A, H, E)


#Call above function and print table
(A, H, E) = CntrDiff(m.pi/4)
print('( Values listed as [[    h, Df+, error (e), e/h, e/h**2, e/h**2   ]] )')
print(' ')
print(A)

#Plot error as a function of step size
p.plot(H,E)
p.title('Central Difference')
p.xlabel('log h')
p.ylabel('log e(h)')
p.show()

print(' ')
print('Forward difference is more accurate because it makes only one approximation per computation of f(x)')