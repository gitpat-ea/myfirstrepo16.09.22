# 4. Добавьте мелкую сетку для предыдущего
# графика (опция `plt.minorticks_on()`
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10, 100, 10000)
y = np.exp(x*np.sin(x))
plt.ylabel("This's axis Y")
plt.xlabel("This's axis X")
plt.minorticks_on()
plt.grid(which='major', axis='both', alpha=1)
plt.grid(which='minor', axis='both', alpha=0.5)
plt.plot(x, y)
plt.show()
