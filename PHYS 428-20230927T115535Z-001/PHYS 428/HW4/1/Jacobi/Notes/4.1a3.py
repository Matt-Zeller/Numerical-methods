import numpy as np
from numpy import linalg as LA

def jacobi(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Jacobi iteration with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    
    #initialize xk once...
    #this is also the first geuss
    xk0 = np.zeros((3,1))
    #do jacobi iteration until convergence tolerance is met
    vectErr = 1.
    while vectErr > 1e-7:
        #initialize vector xk+1 and clear its values after each iteration
        xk1 = np.zeros((3,1))   
        #crudely solve for xk at the kth iteration
        xk1[0,0]=((1/A[0,0]) * (b[0,0] - (A[0,1] * xk0[1,0]) - (A[0,2]*xk0[2,0])))
        xk1[1,0]=((1/A[1,1]) * (b[1,0] - (A[1,0] * xk0[0,0]) - (A[1,2]*xk0[2,0])))
        xk1[2,0]=((1/A[2,2]) * (b[2,0] - (A[2,0] * xk0[0,0]) - (A[2,1]*xk0[1,0])))
        #compute the error between iterations as the vector component with the greatest error
        vectErr = LA.norm((xk1-xk0),(np.inf))
        #set xk for the next iteration
        xk0 = xk1
    return xk1

def gssSdl(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Jacobi iteration with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    
    #initialize xk once...
    #this is also the first geuss
    xk0 = np.zeros((3,1))
    #do jacobi iteration until convergence tolerance is met
    vectErr = 1.
    while vectErr > 1e-7:
        #initialize vector xk+1 and clear its values after each iteration
        xk1 = np.zeros((3,1))
        #crudely solve for xk at the kth iteration
        xk1[0,0]=((1/A[0,0]) * (b[0,0] - (A[0,1] * xk0[1,0]) - (A[0,2]*xk0[2,0])))
        #the next two lines are different from Jacobi
        xk1[1,0]=((1/A[1,1]) * (b[1,0] - (A[1,0] * xk1[0,0])  - (A[1,2]*xk0[2,0])))
        xk1[2,0]=((1/A[2,2]) * (b[2,0] - (A[2,0] * xk1[0,0])  - (A[2,1]*xk1[1,0])))
        #compute the error between iterations as the vector component with the greatest error
        vectErr = LA.norm((xk1-xk0),(np.inf))
        #set xk for the next iteration
        xk0 = xk1
    return xk1

A = np.array([[ 4.,-1., 0.],
              [-1., 4.,-1.],
              [ 0.,-1., 4.]])

b = np.array([[2. ],
              [4. ],
              [10.]])
    
print('The solution x from the Jacobi iterative method is approximately...')
print(jacobi(A,b))

print('The solution x from the Gauss-Seidel iterative method is approximately...')
print(gssSdl(A,b))




