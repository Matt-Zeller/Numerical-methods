import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def jacobi(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Jacobi iteration with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    
    #initialize xk once...
    #this is also the first geuss
    xk0 = np.zeros((3,1))
    x   = np.zeros((3,1000))
    #initialize matrices of one and two iterations before the current, to be used later(not sure if these are necessary)
#    xkNeg1  = np.zeros((3,1))
#    xkNeg2  = np.zeros((3,1))
    #initialize array to store arrays of x values at each iteration, to be plotted later
    #size 18 leads to best visualization of error per iteration...
    #...to be compared to other iterative methods later on
#    x1AtK = np.zeros(18)
#    x2AtK = np.zeros(18)
#    x3AtK = np.zeros(18)
    erArray = np.zeros(18)
    cArray  = np.zeros(18)
    cPlotArray = np.zeros(18)
    #no idea what this is for, i forgot
    #xAtK = np.zeros(18,0)
    
    #initialize convergence tolerance and error
    convTol = 1.
    er = 1.
    C = 1.
    #initialize iteration count
    i = 0
    while convTol > 1e-7:
        #initialize vector xk+1 and clear its values after each iteration
        xk1 = np.zeros((3,1))
        
        cArray[i] = xk1 
        #crudely solve for xk at the kth iteration
        xk1[0,0]=((1/A[0,0]) * (b[0,0] - (A[0,1] * xk0[1,0]) - (A[0,2]*xk0[2,0])))
        xk1[1,0]=((1/A[1,1]) * (b[1,0] - (A[1,0] * xk0[0,0]) - (A[1,2]*xk0[2,0])))
        xk1[2,0]=((1/A[2,2]) * (b[2,0] - (A[2,0] * xk0[0,0]) - (A[2,1]*xk0[1,0])))
        #store for this iteration the array of x values
        x1AtK[i+1]=(xk1[0,0])
        x2AtK[i+1]=(xk1[1,0])
        x3AtK[i+1]=(xk1[2,0])
        #I cant remember why i put this here
        #xAtK[i+1,0] =()
        #compute the error between iterations as the vector component with the greatest error
        convTol = LA.norm((xk1-xk0),(np.inf))
        er = LA.norm((xk1-np.array([[1.],
                                    [2.],
                                    [3.]])),(np.inf))
        if 2 < i < 18:
            C = ((LA.norm(cArray[i-1,0] - cArray[i,0])) /
                 (LA.norm(cArray[i-1,0] - cArray[i-2,0])))
        #store error for current iteration in array of all errors at all iterations to be plotted later
        erArray[i+1]=er
        cPlotArray [i+1]=C
        #set xk for the next iteration
        xk0 = xk1
        #record iteration count
        i = i+1
        
        #give up array of values at k iterations to be plotted
    return x1AtK,x2AtK,x3AtK,erArray,cArray

import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

#tell numpy to print all array values when called
np.set_printoptions(threshold=np.nan)

def gssSdl(A,b,x0):
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
        #initialize vector xk+1 and clear its values after each iteration
        x1 = np.zeros((3,1))
        #crudely solve for xk at the kth iteration
        x1[0,0]=((1/A[0,0]) * (b[0,0] - (A[0,1] * x0[1,0]) - (A[0,2]*x0[2,0])))
        x1[1,0]=((1/A[1,1]) * (b[1,0] - (A[1,0] * x1[0,0]) - (A[1,2]*x0[2,0])))
        x1[2,0]=((1/A[2,2]) * (b[2,0] - (A[2,0] * x1[0,0]) - (A[2,1]*x1[1,0])))
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

plt.figure(1)
plt.subplot(211)
plt.plot(gssSdl(A,b,x0), 'ro')

plt.title('True Error for Jacobi Iterative Method')
plt.xlabel('iteration')
plt.ylabel('error')
plt.yscale('log')
#plt.axis([1, 18, 0, 1])
plt.show()


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

plt.figure(1)
plt.subplot(211)
plt.plot(jacobi(A,b,x0), 'bo',)

plt.title('True Error for Relevant Iterative Methods')
plt.xlabel('iteration')
plt.ylabel('error')
plt.yscale('log')
plt.axis([1, 18, 0, 1])
plt.show()

