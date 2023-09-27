#problem 8
#MATTHEW ZELLER
#07/12/2017
#PHYS 428

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

#Do forward and back substition
for n in range(3):
    x[n,0] = (b[n,0] - L[n,1]*x[1,0] - L[n,0]*x[0,0]) / L[n,n]


for n in range(3):
    y[n,0] = (b[n,0] - U[0,2]*y[2,0] - U[0,1]*y[1,0]) / U[n,n]

print("Solution x is...")
print(x)
print("")
print("Solution y is...")
print(y)
    