# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:10:11 2017

@author: Matt
"""
from math import *
import numpy as n



A = n.array([[-5., 2.,-1.],
             [
def myLU(A)
    PA  = n.zeros((3,3))

    P   = n.zeros((3,3))

    M = n.identity(3)
    for i in range(2):
        if abs(A[i,0]) < abs(A[i+1,0]):
        #then partial pivot, bitch
            PA[i] = A[i+1]
            PA[i+1]=A[i]
        
        #if one fuck-ass has partial pivoted, P had better get a 1 in the entry correspongding...
        #which fucking entry corresponds?
        #well your fucking dumb code looks at, just the next entry
        #and this is always i+1
        #so if there is a partial pivot...
        #god damnit
        #entry at 
        #P[curent fuck bass]
            P[i,i+1] = 1
            P[i+1,i] = 1

        else:
            PA[i]  = A[i]
            P[i,i] = 1.

    if abs(PA[2,0]) > 1e-10:
        M[j,0] = -(PA[j+1,0] / PA[j,0])

    print('Modified A, PA, is...')
    print(PA)
    print('')
    print('Permutation matrix is...')
    print(P)
    
A = n.array([[-5., 2.,-1.],
             [ 1., 0., 3.],
             [ 3., 1., 6.]])

myLU(A)