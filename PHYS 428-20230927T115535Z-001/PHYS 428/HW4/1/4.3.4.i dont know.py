# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:01:58 2017

@author: Matt
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def jacobi(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Jacobi iteration with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    
    #initialize x(k)
    #this is also the first geuss
    x0 = np.zeros((3,1))
    #this will store 'solution' at each iteration
    X = np.zeros((3,1000))
    #this stores error at each iteration
    errs = np.zeros(18)
    #this stores 'C' at each iteration
    cArray  = np.zeros(18)
    #this stores the above in a form plottable my matplotlib###(why aren't this and the above identical and one?)
    cPlotArray = np.zeros(18)
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
        X[0,i+2] =(x1[0,0])
        X[1,i+2] =(x1[1,0])
        X[2,i+2] =(x1[2,0])
        #compute the error between iterations as the vector component with the greatest error
        convTol = LA.norm((x1-x0),(np.inf))
        err = LA.norm((x1-np.array([[1.],
                                   [2.],
                                   [3.]])),(np.inf))
        if 2 < i < 18:
            C = ((LA.norm(cArray[i-1,0] - cArray[i,0])) /
                 (LA.norm(cArray[i-1,0] - cArray[i-2,0])))
        #store error for current iteration in array of all errors at all iterations to be plotted later
        errs[i+1]=err
        cPlotArray [i+1]=C
        #set xk for the next iteration
        x0 = x1
        #increase iteration count
        i = i+1
    #give up array of values at k iterations to be plotted
    return x1AtK,x2AtK,x3AtK,errs,cArray

A = np.array([[ 4.,-1., 0.],
              [-1., 4.,-1.],
              [ 0.,-1., 4.]])

b = np.array([[2. ],
              [4. ],
              [10.]])

w = 2. / (1. + np.sqrt(7/8))

x1AtK,x2AtK,x3AtK,errs,cArray  = jacobi(A,b)  