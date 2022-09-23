# Сделайте логарифмический масштаб по оси ординат.
# Отразите этот факт в подписи к оси
import numpy as np
import matplotlib.pyplot as plt

plt.xscale('log')
plt.yscale('log')
x = np.linspace(10, 100, 10000)
y = np.exp(x*np.sin(x))
plt.ylabel("This's axis Y\n log scale")
plt.xlabel("This's axis X\n log scale")
plt.minorticks_on()
plt.grid(which='major', axis='both', alpha=1)
plt.grid(which='minor', axis='both', alpha=0.5)
plt.plot(x, y)
plt.show()
