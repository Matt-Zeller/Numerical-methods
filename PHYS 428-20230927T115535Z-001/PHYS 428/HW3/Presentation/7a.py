# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:35:31 2017

@author: Matt
"""
from math import *
import numpy as n
from scipy import *



A=array([[-5.,  2., -1.],
         [ 3.,  1.,  6.],
         [ 1.,  0.,  3.]])
def annhilation(A):
    M =identity(3)
    M1=identity(3)
    M2=identity(3)
    for j in range(2):
        print(j)
        #Build M2, make A = M2 M1 A
        if j == 1:
            for i in range(1):
                print('        ',i+2)
                if A[i+2, j]>0.:
                    M2[i+2,j]=-(A[i+2,j]/A[j,j])
            M=dot(M,M2)
            A=dot(M2,A)
            print("M2",M2)
            print("M2M1A",A)
        #Build M1, make A = M1 A
        else:
            for i in range(2):
                print('        ',i+1)
                if A[i+1,j]>0.:
                    M1[i+1,j]=-(A[i+1,j]/A[0,0])
            #take cross product of lower triangular annihilation matrices
            M=dot(M,M1)
            #Set matrix A to be the dot product MA
            A=dot(M1,A)
            print("M1",M1)
            print("M1A",A)
    #Set M again to an identity matrix so it can be filled in the next iteration as M2
