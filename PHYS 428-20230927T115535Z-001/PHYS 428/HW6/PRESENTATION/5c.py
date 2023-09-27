#invIterForEig
#Matt Zeller
#Phys 428
#2 august 2017
import numpy as np
from numpy import linalg as nLA

def invIterForEig(A,v0):
    #Takes 3x3 matrix A, initial geuss vector v0,
    #does inverse iteration method to approximate 
    #eigenvectors/values with convergence tolerance
    #of 1e-5
    k=0
    value1=0
    changeval = 1.
    changevec = 1.
    while abs(changevec)>1e-5 and k<20:
    #loop until differnece between approx's is less than
    #1e-5
        k=k+1
        vtv=np.dot(v0.T,v0)
        #compute (A-uI)w = v(k-1)
        u=np.dot(v0.T,(np.dot(A,v0)))/vtv
        w=np.dot(nLA.inv(A-u[0,0]*np.identity(3)),v0)
    
        v1 = w/nLA.norm(w, 2)
        
        print('k= ',k,'____________________________________')
        print('Eigenvector at kth iteration:')
        print(v1)
        
        value2 = np.dot(v1.T,(np.dot(A,v1)))
        print('Eigenvalue at kth iteration:')
        print(value2)
        
        #difference between eigenvalues between iterations
        changeval = value2-value1
        changevec = v1[0,0]-v0[0,0]
        
        print('Change in eigenvalue and leading entry of eigenvector, respectively:')
        print(changeval[0,0])
        print(changevec)
        #set v0 to v(k-1)
        v0=v1
        value1=value2

A = np.array([[1.,4.,5.],
              [4.,3.,0.],
              [5.,0.,7.]])

v0=(1/np.sqrt(3))*np.ones((3,1))

invIterForEig(A,v0)

