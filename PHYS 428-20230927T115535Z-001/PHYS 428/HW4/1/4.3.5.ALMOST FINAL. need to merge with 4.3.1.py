# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 18:40:56 2017

@author: Matt
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:01:58 2017

@author: Matt
"""
import numpy as np
from numpy import linalg as LA

def jacobi(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Jacobi iteration with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    
    #initialize x(k)
    #this is also the first geuss
    x0 = np.zeros((3,1))
    #this stores error at each iteration
    errs = np.zeros(18)
    #initialize a list to be filled with numpy arrays representing 'solution' matrices at each iteration
    X=[(np.array([[0.],
                  [0.],
                  [0.]]))]
    #initialize array to store asymptotic error constant approximation at each iteration
    c = np.zeros((100,1))
    #initialize convergence tolerance and iteration count necessary for following while loop
    convTol = 1.
    i = 0
    while convTol > 1e-7:
        #initialize  x(k+1) and clear its values after each iteration
        x1 = np.zeros((3,1))
        #crudely solve for xk at the kth iteration
        x1[0,0]=((1/A[0,0]) * (b[0,0] - (A[0,1] * x0[1,0]) - (A[0,2]*x0[2,0])))
        x1[1,0]=((1/A[1,1]) * (b[1,0] - (A[1,0] * x0[0,0]) - (A[1,2]*x0[2,0])))
        x1[2,0]=((1/A[2,2]) * (b[2,0] - (A[2,0] * x0[0,0]) - (A[2,1]*x0[1,0])))
        #Store x matrix
        X.append(x1)
        #compute the error between iterations as the vector component with the greatest error
        convTol = LA.norm((x1-x0),(np.inf))
        err = LA.norm((x1-np.array([[1.],
                                    [2.],
                                    [3.]])),(np.inf))
        if 2 <= i < 100:
            c[i-2,0] =  (LA.norm((X[i] - X[i-1]),(np.inf))) / (LA.norm((X[i-1] - X[i-2]),(np.inf)))
        #store error for current iteration in array of all errors at all iterations to be plotted later
        errs[i+1]=err
        #set xk for the next iteration
        x0 = x1
        #increase iteration count
        i = i+1
    #give up array of values at k iterations to be plotted
    return X,errs,c

A = np.array([[ 4.,-1., 0.],
              [-1., 4.,-1.],
              [ 0.,-1., 4.]])

b = np.array([[2. ],
              [4. ],
              [10.]])

w = 2. / (1. + np.sqrt(7/8))

X,errs,c  = jacobi(A,b)  
np.set_printoptions(threshold=np.nan)
