import numpy as n

#Matrix A
L = n.array([[1., 0., 0.],
             [2., 1., 0.],
             [3., 4., 1.]])

U = n.array([[1., 2.,-1.],
             [0., 3.,-1.],
             [0., 0., 2.]])
#Matrix b
b = n.array([[-1.],
             [ 0.],
             [ 1.]])

#Solution matrix x
x = n.zeros((3,1))
y = n.zeros((3,1))

#Generalize below set of computations into a for loop over m rows and n columns
#of the matrix A
for n in range(3):
    x[n,0] = (b[n,0] - L[n,1]*x[1,0] - L[n,0]*x[0,0]) / L[n,n]

x[0,0] =  b[0,0]                                    / L[0,0]
x[1,0] = (b[1,0] - A[1,0]*x[0,0]                )   / L[1,1]
x[2,0] = (b[2,0] - A[2,1]*x[1,0] - A[2,0]*x[0,0])   / L[2,2]

for n in range(3):
    y[n,0] = (b[n,0] - U[0,2]*y[2,0] - U[0,1]*y[1,0]) / U[n,n]
    
y[2,0] = b[2,0] / U[2,2]
y[1,0] = (b[1,0] - U[1,2]*y[2,0]) / U[1,1]
y[0,0] = (b[0,0] - U[0,2]*y[2,0] - U[0,1]*y[1,0]) / U[0,0]
