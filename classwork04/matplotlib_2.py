#Добавьте сетку и описание осей для предыдущего графика
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100, 10)
y = np.sin(x)*x**2
plt.ylabel(r"This's axis Y")
plt.xlabel(r"This's axis X")
#plt.minorticks_on()
plt.grid(which='major', axis='both', alpha=1)
#plt.grid(which='minor', axis='both', alpha=0.25)
plt.plot(x, y)
plt.show()