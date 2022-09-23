#Добавьте сетку и описание осей для предыдущего графика
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10,100, 10000)
y = np.exp(-x*np.sin(x))
plt.ylabel("This's axis Y")
plt.xlabel("This's axis X")
plt.grid(which='major', axis='both', alpha=1)
plt.plot(x, y)
plt.show()