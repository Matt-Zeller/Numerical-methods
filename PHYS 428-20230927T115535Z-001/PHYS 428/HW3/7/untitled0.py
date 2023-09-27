# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:17:46 2017

@author: Matt
"""

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