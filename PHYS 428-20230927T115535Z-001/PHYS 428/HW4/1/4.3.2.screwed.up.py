# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:50:20 2017

@author: Matt
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def jacobi(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Jacobi iteration with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    
    #initialize xk once...
    #this is also the first geuss
    xk     = np.zeros((3,1000))
    #initialize array to store arrays of x values at each iteration, to be plotted later
    #size 18 leads to best visualization of error per iteration...
    #...to be compared to other iterative methods later on
#    x1AtK = np.zeros(18)
#    x2AtK = np.zeros(18)
#    x3AtK = np.zeros(18)
    erArray = np.zeros(18)
    cTable  = np.zeros(18)
    #initialize convergence tolerance and error
    convTol = 1.
    er = 1.
    #initialize iteration count
    i = 1
    while convTol > 1e-7:
        #initialize vector xk+1 and clear its values after each iteration
        #xk1 = np.zeros((3,1000))
        #crudely solve for xk at the kth iteration
        xk[0,i]=((1/A[0,0]) * (b[0,0] - (A[0,1] * xk[1,i-1]) - (A[0,2]*xk[2,i-1])))
        xk[1,i]=((1/A[1,1]) * (b[1,0] - (A[1,0] * xk[0,i-1]) - (A[1,2]*xk[2,i-1])))
        xk[2,i]=((1/A[2,2]) * (b[2,0] - (A[2,0] * xk[0,i-1]) - (A[2,1]*xk[1,i-1])))
        #store for this iteration the array of x values
#        x1AtK[i+1]=(xk1[0,0])
#        x2AtK[i+1]=(xk1[1,0])
#        x3AtK[i+1]=(xk1[2,0])
        #I cant remember why i put this here
        #xAtK[i+1,0] =()
        #compute the error between iterations as the vector component with the greatest error
        convTol = LA.norm((xk[-xk0),(np.inf))
        er = LA.norm((xk1-np.array([[1.],
                                    [2.],
                                    [3.]])),(np.inf))

        #store error for current iteration in array of all errors at all iterations to be plotted later
        erArray[i+1]=er
        if 2 < i < 18:
            cTable[i] = ((LA.norm(erArray[i-1] - erArray[i])) / (LA.norm(erArray[i-1] - erArray[i-2])))   
        #set xk for the next iteration
        xk0 = xk1
        #record iteration count
        i = i+1
        
        #give up array of values at k iterations to be plotted
    return x1AtK,x2AtK,x3AtK,erArray,cTable

A = np.array([[ 4.,-1., 0.],
              [-1., 4.,-1.],
              [ 0.,-1., 4.]])

b = np.array([[2. ],
              [4. ],
              [10.]])

x1AtK,x2AtK,x3AtK,erArray,cTable  = jacobi(A,b)
np.set_printoptions(threshold=np.nan)
print(cTable)