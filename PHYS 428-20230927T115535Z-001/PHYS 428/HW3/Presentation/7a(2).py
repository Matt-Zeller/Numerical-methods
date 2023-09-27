#luSolve
#MATTHEW ZELLER
#O7/27/2017
#PHYS 428

from math import *
import numpy as n
from scipy import *

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
    
    return(PA,P)

def annhilation(A):
    #Initialize annhilation matrices
    M =identity(3)
    M1=identity(3)
    M2=identity(3)
    
    #Compute U since P has been determined and the input matrix A=PA is given as the input
    for j in range(2):
        print(j)
        #Build M2, compute M2 * M1A
        if j == 1:
            for i in range(1):
                print('        ',i+2)
                if A[i+2, j]>0.:
                    #Build M2
                    M2[i+2,j]=-(A[i+2,j]/A[j,j])
            #take cross product of lower triangular annihilation matrices to build M
            M=dot(M,M2)
            A=dot(M2,A)
            print("M2",M2)
            print("M2M1A",A)
        #Build M1, compute M1A
        else:
            for i in range(2):
                print('        ',i+1)
                if A[i+1,j]>0.:
                    #Build M1
                    M1[i+1,j]=-(A[i+1,j]/A[0,0])
            #take cross product of lower triangular annihilation matrices
            M=dot(M,M1)
            #Set matrix A to be the dot product MA
            A=dot(M1,A)
            print("M1",M1)
            print("M1A",A)
    return(A,M)


def solver(U,L,b):
    #SOLVES FOR X IN Ax=b given upper triangular and lower triangle matrices, b
    
    #Solution matrix x, intermediate solution matrix y
    x = n.zeros((3,1))
    y = n.zeros((3,1))
    
    #Generalize below set of computations into a for loop over i columns
    #of the matrix A
    for i in range(3):
        x[i,0] = (b[i,0] - L[i,1]*x[1,0] - L[i,0]*x[0,0]) / L[i,i]
    
    for i in range(3):
        y[i,0] = (b[i,0] - U[0,2]*y[2,0] - U[0,1]*y[1,0]) / U[i,i]
    return x



#this is how one would use the function, you must enter your 3x3 matrix and vector b for each case, then call the functions 
A = n.array([[-5., 2.,-1.],
             [ 1., 0., 3.],
             [ 3., 1., 6.]])

b = n.array([[-1.],
             [ 0.],
             [ 1.]])    
    
A,P=myLU(A)
A,M = annhilation(A)
x=solver(A,M,b)
#now one must call for A(Which is now just the upper triangular part of PA=LU), or M, or P, or x, as in [>>x] to call x
x
