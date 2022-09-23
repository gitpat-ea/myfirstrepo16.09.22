import numpy as np
array = np.array([i for i in range(1,100)])
matrix = array.reshape(33,3)
summa = np.array([np.sum(i) for i in matrix])
summa = summa.reshape(11,3)
print(summa)