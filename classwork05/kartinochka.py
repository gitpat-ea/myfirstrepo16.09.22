import numpy as np
from matplotlib import pyplot as plt

# np.random.seed(42)
znach = np.random.randint(256, size=30000)

arr = znach.reshape(100, 100, 3)
cs = plt.matshow(arr)
plt.colorbar(cs)
plt.show()
