import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def jacobi(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Jacobi iteration with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    
    #initialize xk once...
    #this is also the first geuss
    xk0 = np.zeros((3,1))
    #initialize array to store arrays of x values at each iteration, to be plotted later
    #size 18 leads to best visualization of error per iteration...
    #...to be compared to other iterative methods later on
    x1AtK = np.zeros(18)
    x2AtK = np.zeros(18)
    x3AtK = np.zeros(18)
    erArray = np.zeros(18)
    #initialize convergence tolerance and error
    convTol = 1.
    er = 1.
    #initialize iteration count
    i = 0
    while convTol > 1e-7:
        #initialize vector xk+1 and clear its values after each iteration
        xk1 = np.zeros((3,1))
        #crudely solve for xk at the kth iteration
        xk1[0,0]=((1/A[0,0]) * (b[0,0] - (A[0,1] * xk0[1,0]) - (A[0,2]*xk0[2,0])))
        xk1[1,0]=((1/A[1,1]) * (b[1,0] - (A[1,0] * xk0[0,0]) - (A[1,2]*xk0[2,0])))
        xk1[2,0]=((1/A[2,2]) * (b[2,0] - (A[2,0] * xk0[0,0]) - (A[2,1]*xk0[1,0])))
        #store for this iteration the array of x values
        x1AtK[i+1]=(xk1[0,0])
        x2AtK[i+1]=(xk1[1,0])
        x3AtK[i+1]=(xk1[2,0])
        #compute the error between iterations as the vector component with the greatest error
        convTol = LA.norm((xk1-xk0),(np.inf))
        er = LA.norm((xk1-np.array([[1.],
                                    [2.],
                                    [3.]])),(np.inf))
        #store error for current iteration in array of all errors at all iterations to be plotted later
        erArray[i+1]=er
        #set xk for the next iteration
        xk0 = xk1
        #record iteration count
        i = i+1
        
        #give up array of values at k iterations to be plotted
    return x1AtK,x2AtK,x3AtK,erArray

def gssSdl(A,b):
    #takes 3x3 matrix A and 3x1 b (as numpy arrays) in Ax=b, solves x by Gauss-Seidel method with initial geuss x = 0
    #and convergence tolerance of 1e-7. Returns solution x as a numpy array
    #initialize xk once...
    #this is also the first geuss
    xk0 = np.zeros((3,1))
    #initialize array to store arrays of x values at each iteration, to be plotted later
    x1AtK = np.zeros(18)
    x2AtK = np.zeros(18)
    x3AtK = np.zeros(18)
    erArray = np.zeros(18)
    #initialize convergence tolerance and error
    convTol = 1.
    er = 1.
    #initialize iteration count
    i = 0
    while convTol > 1e-7:
        #initialize vector xk+1 and clear its values after each iteration
        xk1 = np.zeros((3,1))
        #crudely solve for xk at the kth iteration
        xk1[0,0]=((1/A[0,0]) * (b[0,0] - (A[0,1] * xk0[1,0]) - (A[0,2]*xk0[2,0])))
        xk1[1,0]=((1/A[1,1]) * (b[1,0] - (A[1,0] * xk1[0,0])  - (A[1,2]*xk0[2,0])))
        xk1[2,0]=((1/A[2,2]) * (b[2,0] - (A[2,0] * xk1[0,0])  - (A[2,1]*xk1[1,0])))
        #compute the error between iterations as the vector component with the greatest error
        convTol = LA.norm((xk1-xk0),(np.inf))
        er = LA.norm((xk1-np.array([[1.],
                                    [2.],
                                    [3.]])),(np.inf))
        #store error for current iteration in array of all errors at all iterations to be plotted later
        erArray[i+1]=er        
        #store for this iteration the array of x values
        x1AtK[i+1]=(xk1[0,0])
        x2AtK[i+1]=(xk1[1,0])
        x3AtK[i+1]=(xk1[2,0])
        #set xk for the next iteration
        xk0 = xk1
        #record iteration count
        i = i+1
    #give up array of values at all iterations to be plotted
    return x1AtK,x2AtK,x3AtK,erArray

def gssSdlAccel(A,b,w):
    #takes 3x3 matrix A, 3x1 b (as numpy arrays) in Ax=b, and acceleration parameter w 
    #solves x by accelerated Gauss-Seidel method with initial geuss x = 0...
    #...and convergence tolerance of 1e-7. Returns solution x as a numpy array
    #initialize xk once...
    #this is also the first geuss
    xk0 = np.zeros((3,1))
    #initialize array to store arrays of x values at each iteration, to be plotted later
    x1AtK = np.zeros(18)
    x2AtK = np.zeros(18)
    x3AtK = np.zeros(18) 
    erArray = np.zeros(18)
    #initialize convergence tolerance and error
    convTol = 1.
    er = 1.
    #initialize iteration count
    i = 0
    while convTol > 1e-7:
        #initialize vector xk+1 and clear its values after each iteration
        xk1 = np.zeros((3,1))
        #crudely solve for xk at the kth iteration
        xk1[0,0]= xk0[0,0] - (w/A[0,0]) * (A[0,0]*xk0[0,0] + A[0,1]*xk0[1,0] + A[0,2]*xk0[2,0] - b[0,0])
        xk1[1,0]= xk0[1,0] - (w/A[1,1]) * (A[0,1]*xk1[0,0] + A[1,1]*xk0[1,0] + A[1,2]*xk0[2,0] - b[1,0])
        xk1[2,0]= xk0[2,0] - (w/A[2,2]) * (A[0,2]*xk1[0,0] + A[1,2]*xk1[1,0] + A[2,2]*xk0[2,0] - b[2,0])
        #compute the error between iterations as the vector component with the greatest error
        convTol = LA.norm((xk1-xk0),(np.inf))
        er = LA.norm((xk1-np.array([[1.],
                                    [2.],
                                    [3.]])),(np.inf))
        #store error for current iteration in array of all errors at all iterations to be plotted later
        erArray[i+1]=er        
        #store for this iteration the array of x values
        x1AtK[i+1]=(xk1[0,0])
        x2AtK[i+1]=(xk1[1,0])
        x3AtK[i+1]=(xk1[2,0])
        #set xk for the next iteration
        xk0 = xk1
        #record iteration count
        i = i+1
    #give up array of values at all iterations to be plotted
    return x1AtK,x2AtK,x3AtK,erArray

A = np.array([[ 4.,-1., 0.],
              [-1., 4.,-1.],
              [ 0.,-1., 4.]])

b = np.array([[2. ],
              [4. ],
              [10.]])

w = 2. / (1. + np.sqrt(7/8))

x1AtK,x2AtK,x3AtK,erArray        = jacobi(A,b)  
x1AtKg,x2AtKg,x3AtKg,erArrayg    = gssSdl(A,b) 
x1AtKw,x2AtKw,x3AtKw,erArrayw    = gssSdlAccel(A,b,w)
#plt.plot(jacobi(A,b))
plt.plot(x1AtK,'r-',x2AtK,'r-',x3AtK,'r-',
         x1AtKg,'y-',x2AtKg,'y-',x3AtKg,'y-',
         x1AtKw,'b-',x2AtKw,'b-',x3AtKw, 'b-')

#plt.figure(1)
#plt.subplot(211)
#plt.plot(x1AtK,'r-',x2AtK,'r-',x3AtK,'r-',
#         x1AtKg,'y-',x2AtKg,'y-',x3AtKg,'y-',
#         x1AtKw,'b-',x2AtKw,'b-',x3AtKw, 'b-')
#plt.title('Convergence for Jacobi, Gauss-Seidel, and SOR Iterative Methods')
#plt.xlabel('iteration')
#plt.ylabel('log scale solution values')
#plt.yscale('log')
#plt.axis([1, 18, 0, 4])

plt.subplot(212)
plt.plot(erArray,'r-',erArrayg,'y-',erArrayw, 'b-')
plt.title('Convergence for Jacobi, Gauss-Seidel, and SOR Iterative Methods')
plt.xlabel('iteration')
plt.ylabel('log scale error values')
plt.yscale('log')
plt.axis([1, 18, 0, 4])
plt.show()
