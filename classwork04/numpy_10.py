import numpy as np
def matrixexp(n = 1,raz =1, matrix = np.array([1])):
    edenich = np.array([0 for i in range(raz**2)])
    edenich = edenich.reshape(raz,raz)
    print(edenich)
    for i in range(1,n+1):
        ifact = np.prod(np.array([i for i in range(1,i+1)]))
        print(ifact)
        imat = matrix.reshape(raz,raz)
        for j in range(1,i):
            imat = imat @ matrix.reshape(raz,raz)
        edenich = edenich + 1/(ifact)*imat
    return(edenich)
mat = np.array([1 for i in range(5**2)])
print(mat)
print(matrixexp(5,5,mat))