#g(x)
#MATTHEW ZELLER
#06/19/17
#PHYS 428

import matplotlib.pyplot as plt

def g(x):
    A = []
    for n in range(10):
        x = 2*x*(1-x)
        e = abs((0.5)-x)
        A.append(e)
        print(e)
    plt.xlabel('Iteration')
    plt.ylabel('|p - xn|')
    plt.title('Order of Convergence for g(x) = 2x(x-1)')
    plt.plot(A)
    plt.show()
g(0.9)
print('For iterations 1-3-ish the convergence is clearly linear')