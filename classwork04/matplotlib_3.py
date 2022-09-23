#Нарисуйте непрерывной прямой график  𝑒−𝑥sin(𝑥)
# для x со значениямиот 10 до 100
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10,100, 10000)
y = np.exp(-x*np.sin(x))
plt.ylim(0,10)
plt.plot(x, y)
plt.show()