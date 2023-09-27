
from numpy import *
from scipy import linalg as LA

def myLU(A):
    #Runs LU decomposition for a given 3x3 matrix array
    #returns modified matrix A and permutation matrix p
    
    #initialize modified matrix A, as 'PA'
    PA  = zeros((3,3))
    
    #Initialize permutation matrix P, as 'P'
    P   = zeros((3,3))
    
    #Run LU decomposition
    for i in range(3):
        #Check if greatest magnitude is in diagonal position
        if abs(A[i,0]) < abs(A[i+1,0]) and i<2:
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
    #Matrix b
    
    #Solution matrix x, intermediate solution matrix y
    x = zeros((3,1))
    y = zeros((3,1))
    
    #Generalize below set of computations into a for loop over m rows and n columns
    #of the matrix A
    for i in range(3):
        x[i,0] = (b[i,0] - L[i,1]*x[1,0] - L[i,0]*x[0,0]) / L[i,i]
    
    for i in range(3):
        y[i,0] = (b[i,0] - U[0,2]*y[2,0] - U[0,1]*y[1,0]) / U[i,i]
    return x

def hilbertBProduce(i):
    #gives an array(matrix) B which is the vector b of size n in Hx=b if x = [1,...,1]^(transpose)
    for n in range(i):
        H=array(LA.hilbert(i))
        B=zeros((i,1))
        for j in range(i):
            B[j,0]=sum(H[j])
    return(H,B)


(H,B)=hilbertBProduce(3)

linalg.cond(B)

print('Sadly I did not have time to make generalize myLU.py and LUsolve.py')
print('so that they could handle large Hilbert matricess.')
print('Here I at least solved for x in Hx=b for a 3x3 Hilbert matrix')


