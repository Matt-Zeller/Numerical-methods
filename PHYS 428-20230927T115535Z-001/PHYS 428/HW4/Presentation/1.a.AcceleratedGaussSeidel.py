import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def gssSdlAccel(A,b,x0,w):
    #takes 3x3 matrix A, 3x1 b, and 3x1 x0 (first geuss) in Ax=b, returns solution vector X by Jacobi iteration ...
    #...with convergence tolerance of 1e-7.
    
    #will fill with approximate vector 'solutions' at each iteration
    X=[(np.array([[0.],
                  [0.],
                  [0.]]))]
    #stores error at each iteration
    errs = np.zeros(18)
    #will store asymptotic error constant approximations at each iteration
    c = np.zeros((100,1))
    #initialize convergence tolerance and iteration count
    convTol = 1.
    i = 0
    while convTol > 1e-7:
        #initialize  x(k+1) and clear its values after each iteration
        x1 = np.zeros((3,1))
        #crudely solve for xk at the kth iteration
        x1[0,0]= x0[0,0] - (w/A[0,0]) * (A[0,0]*x0[0,0] + A[0,1]*x0[1,0] + A[0,2]*x0[2,0] - b[0,0])
        x1[1,0]= x0[1,0] - (w/A[1,1]) * (A[0,1]*x1[0,0] + A[1,1]*x0[1,0] + A[1,2]*x0[2,0] - b[1,0])
        x1[2,0]= x0[2,0] - (w/A[2,2]) * (A[0,2]*x1[0,0] + A[1,2]*x1[1,0] + A[2,2]*x0[2,0] - b[2,0])
        #store 'solution'
        X.append(x1)
        #compute vector errors
        convTol = LA.norm((x1-x0),(np.inf))
        err     = LA.norm((x1-np.array([[1.],
                                        [2.],
                                        [3.]])),(np.inf))
        #compute asymptotic error constant
        if 2 <= i <= 100:
            c[i-2,0] =  ((LA.norm((X[i] - X[i-1]),(np.inf))) / (LA.norm((X[i-1] - X[i-2]),(np.inf))))
        #store error for current iteration in array of all errors at all iterations to be plotted later
        errs[i+1]=err
        #set xk for the next iteration
        x0 = x1
        #increase iteration count
        i = i+1
    #show solution
    print('After',i,'iterations the approximate solution X is...',)
    print(X[i]),    
    #give array of errors
    return errs

A=np.array([[ 4.,-1., 0.],
            [-1., 4.,-1.],
            [ 0.,-1., 4.]])
b=np.array([[2. ],
            [4. ],
            [10.]])
x0=np.array([[0.],
             [0.],
             [0.]])

w = 2. / (1. + np.sqrt(7/8))

plt.figure(1)
plt.subplot(211)
plt.plot(gssSdlAccel(A,b,x0,w), 'bo')

plt.title('True Error for Jacobi Iterative Method')
plt.xlabel('iteration')
plt.ylabel('error')
plt.yscale('log')
#plt.axis([1, 18, 0, 1])
plt.show()