import numpy as np
np.random.seed(1)
r1 = np.random.rand(120)
mean = r1.mean()
summa = r1.sum()
srkv = r1.std()
# print(r1)
r1 = r1.reshape(12, 10)
print("r1.meanx() = ", r1.mean(axis=1))
print("r1.meany() = ", r1.mean(axis=0))
print("r1.stdx() = ", r1.std(axis=1))
print("r1.stdy() = ", r1.std(axis=0))
print("r1.sumx() = ", r1.sum(axis=1))
print("r1.sumy() = ", r1.sum(axis=0))
print("minstolb = ", r1.min(axis=0))
print("maxstolb = ", r1.max(axis=0))
print("znachminstr = ", r1.argmin(axis=1))
print("znachmaxstr = ", r1.argmax(axis=1))

