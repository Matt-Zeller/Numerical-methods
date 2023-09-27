import numpy as np

def jacobi(A,b):
    #takes 3x3 matrix A and b in Ax=b, solves x by Jacobi iteration with initial geuss x = 0
    #returns solution x as a numpy array
    
    #initialize solution vector xk+1 and xk respectively
    xk1=np.zeros((3,1))
    xk0=xk1
    
    #create variable for iteration number of following while loop
    k=0
    
    #do jacobi iteration until convergence tolerance is met
    while vectErr < 10e-7:
        
        #at the kth iteration, compute xk+1 1,xk+1 2,xk+1 3 from xk1,xk2,xk3
        for j in range(2):
            for i in range(3):
                x[i,0]=(b[i,0] - A[i,])

xk1[0,0]=(1/A[0,0]) * (b[0,0] - (A[0,1] * xk0[1,0]) - (A[0,2]*xk0[2,0]))

xk1[1,0]=(1/A[1,1]) * (b[1,0] - (A[1,0] * xk0[0,0]) - (A[1,2]*xk0[2,0]))

xk1[2,0]=(1/A[2,2]) * (b[2,0] - (A[2,0] * xk0[0,0]) - (A[2,1]*xk0[1,0]))



