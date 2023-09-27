import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def gssSdl(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Gauss-Seidel method with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    
    #initialize xk once...
    #this is also the first geuss
    xk0 = np.zeros((3,1))
    #initialize array to store arrays of x values at each iteration, to be plotted later
    x1AtK = np.zeros(18)
    x2AtK = np.zeros(18)
    x3AtK = np.zeros(18)    
    #do jacobi iteration until convergence tolerance is met
    vectErr = 1.
    #initialize iteration count
    i = 0    
    while vectErr > 1e-7:
        #initialize vector xk+1 and clear its values after each iteration
        xk1 = np.zeros((3,1))
        #crudely solve for xk at the kth iteration
        xk1[0,0]=((1/A[0,0]) * (b[0,0] - (A[0,1] * xk0[1,0]) - (A[0,2]*xk0[2,0])))
        xk1[1,0]=((1/A[1,1]) * (b[1,0] - (A[1,0] * xk1[0,0])  - (A[1,2]*xk0[2,0])))
        xk1[2,0]=((1/A[2,2]) * (b[2,0] - (A[2,0] * xk1[0,0])  - (A[2,1]*xk1[1,0])))
        #compute the error between iterations as the vector component with the greatest error
        vectErr = LA.norm((xk1-xk0),(np.inf))
        #store for this iteration the array of x values
        x1AtK[i]=(xk1[0,0])
        x2AtK[i]=(xk1[1,0])
        x3AtK[i]=(xk1[2,0])
        #set xk for the next iteration
        xk0 = xk1
        #record iteration count
        i = i+1
    #give up array of values at all iterations to be plotted
    return x1AtK,x2AtK,x3AtK

A = np.array([[ 4.,-1., 0.],
              [-1., 4.,-1.],
              [ 0.,-1., 4.]])

b = np.array([[2. ],
              [4. ],
              [10.]])

x1AtK,x2AtK,x3AtK = gssSdl(A,b)   
#plt.plot(jacobi(A,b))
plt.plot(x1AtK,'ro', x2AtK, 'yo', x3AtK, 'bo')
plt.title('Rate of Convergence for Jacobi, Gauss-Seidel, and SOR Iterative Methods' )
plt.xlabel('iteration')
plt.ylabel('solution values')
plt.yscale('log')