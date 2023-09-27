# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:10:11 2017

@author: Matt
"""
from math import *
import numpy as n

def luSolve(A):
    #Runs LU decomposition for a given 3x3 matrix array
    #returns modified matrix A and permutation matrix p
    
    #initialize modified matrix A, as 'PA'
    PA  = n.zeros((3,3))
    
    #Initialize permutation matrix P, as 'P'
    P   = n.zeros((3,3))
    
    #initialize solution vector x
    x   = n.zeros((3,1))
    
    #initialize manipulation matrix M
    M   = n.zeros((3,3))
    
    #Run LU decomposition
    for i in range(2):
        #Check if greatest magnitude is in diagonal position
        if abs(A[i,0]) < abs(A[i+1,0]):
            #partial pivot
            PA[i] = A[i+1]
            PA[i+1]=A[i]
        
            #Fill permutation matrix accordingly
            P[i,i+1] = 1
            P[i+1,i] = 1

        else:
            #preserve matrix structure
            PA[i]  = A[i]
            #preserve permutation matrix, keep value 1 in diagonal
            P[i,i] = 1.
             
             
    ##############################
#####################################
#####################################
        #Build upper and lower triangular systems
    for i in range(2):
        #build for i columns
        for j in range(2):
            #build for j rows in the ith column
            
            #fill your M matrix
            M[j+1, i] = -(PA[j+1,i]/PA[0,0])
    
    
    
    #initialize lower triangular matrix which is equal to the multiplier matrix
    L = n.zeros((3,3))

    #initialize upper triangular matrix which is equal to the cross product of multiplier matrix before A
    U = n.zeros((3,3))
    
    L[0,0]
             
             
             
             
             
             
             
             
             
             
             
             
    ##############################################
    ############################################3#
    #forward and back substitution section
    #compute x as in Lx = b
    for i in range(3):
        x[i,0] = (b[i,0] - L[i,1]*x[1,0] - L[i,0]*x[0,0]) / L[i,i]

    #now compute y as in U...?
    for i in range(3):
        y[i,0] = (b[i,0] - U[0,2]*y[2,0] - U[0,1]*y[1,0]) / U[i,i]
        
    #Print what is what for user
    print('x is...')
    print(x)
    print('y is...)

#this is how one would use the function, you must enter your 3x3 matrix for each case, then call the function myLU    
A = n.array([[-5., 2.,-1.],
             [ 1., 0., 3.],
             [ 3., 1., 6.]])

b = n.array([[ 2.],
             [-2.],
             [ 1.]])

myLU(A)