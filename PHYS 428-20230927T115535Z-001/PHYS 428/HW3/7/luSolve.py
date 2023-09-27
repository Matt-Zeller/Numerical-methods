# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:10:11 2017

@author: Matt
"""
from math import *
import numpy as n

def myLU(A):
    #Runs LU decomposition for a given 3x3 matrix array
    #returns modified matrix A and permutation matrix p
    
    #initialize modified matrix A, as 'PA'
    PA  = n.zeros((3,3))
    
    #Initialize permutation matrix P, as 'P'
    P   = n.zeros((3,3))
    
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

    #Print what is what for user
    print('Modified A, PA, is...')
    print(PA)
    print('')
    print('Permutation matrix is...')
    print(P)

#this is how one would use the function, you must enter your 3x3 matrix for each case, then call the function myLU    
A = n.array([[-5., 2.,-1.],
             [ 1., 0., 3.],
             [ 3., 1., 6.]])

myLU(A)