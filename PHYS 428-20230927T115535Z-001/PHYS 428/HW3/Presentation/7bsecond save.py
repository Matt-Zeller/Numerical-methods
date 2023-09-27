#*various
#MATT ZELLER
#PHYS 492
#07/28/2017


from numpy import *
from scipy import *
from scipy import linalg as LA
from numpy import linalg as nLA

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
        if i<2 and abs(A[i,0]) < abs(A[i+1,0]):
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
        #Build M2, compute M2 * M1A
        if j == 1:
            for i in range(1):
                if A[i+2, j]>1e-5:
                    #Build M2
                    M2[i+2,j]=-(A[i+2,j]/A[j,j])
            #take cross product of lower triangular annihilation matrices to build M
            M=dot(M,M2)
            A=dot(M2,A)
        #Build M1, compute M1A
        else:
            for i in range(2):
                if A[i+1,j]>1e-5:
                    #Build M1
                    M1[i+1,j]=-(A[i+1,j]/A[0,0])
            #take cross product of lower triangular annihilation matrices
            M=dot(M,M1)
            #Set matrix A to be the dot product MA
            A=dot(M1,A)
    return(A,M,M1,M2)

def solver(U,M,b):
    #Takes upper and lower triangular 3x3's and b in PAx=M(inverse)Ux=Pb from Ax=b...
    #input U and M should already be completely pivoted
    #b should be pivoted correspondingly
    
    #Solution matrix x, intermediate solution matrix y
    #as in Ly=Pb then Ux=y...
    #...these computations are redundant here however,
    #x and y are....?
    L=LA.inv(M)
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
#true solution x = [1,...,1](transpose)
x = ones((3,1))
M1,M2 = identity(3),identity(3)
(H,B)=hilbertBProduce(3)
print('Here is my Hilbert 3x3...')
print(H)
print('...and the b produced by assuming in Hx=b x=[1,...,1](transpose)')
print('in other words the row sum of H...')
print(B)
print('Here is the output from partial pivoting H...')
print(H)
H,P=myLU(H)
print('...as expected it is unchanged.')
print('')
print('Next gaussian elimination is run on H producing the following MH,M,M1,M2 respectively:')
H,M,M1,M2=annhilation(H)
print(H)
print('')
print(M)
print('')
print(M1)
print('')
print(M2)
print('Lastly MH and M are taken as U and L, and b as b, in LU=PAx=Pb, (P is identity in this case)')
X=solver(H,M,B)
print('x=')
print(X)
#error, true solution x, approximate solution X
e = x-X
#residual
r = B - dot(H,x)
#relative error
relE=LA.norm(e,inf)/LA.norm(x,inf)
#relative residual
relR=LA.norm(r,inf)/LA.norm(x,inf)
#condition number of H
K=nLA.cond(H)
print('the relative error, relative residual, and condition number for')
print('are respectively,')
print(relE)
print(relR)
print(K)
print('H is poorly conditioned, the condition number is relatively large')
print('Sadly I did not have time to make generalize myLU.py and LUsolve.py')
print('so that they could handle large Hilbert matricess.')
print('Here I at least solved for x in Hx=b for a 3x3 Hilbert matrix')


