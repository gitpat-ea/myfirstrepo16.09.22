import numpy as np
array = np.array([i for i in range(1,100)])
matrix = array.reshape(33,3)
summa = np.array([np.sum(i) for i in matrix])
summa = summa.reshape(11,3)
summa = summa.T
vector = np.array([i-11 for i in range(11)])
vector = vector.reshape(11,1)
#print(vector)
proizv = summa @ vector
#print(summa)
print(proizv)