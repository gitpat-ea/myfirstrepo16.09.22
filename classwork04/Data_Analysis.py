import matplotlib
from matplotlib import pyplot as plt
import numpy as np

matplotlib.rcParams.update(matplotlib.rcParamsDefault)


def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3


def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    import numpy as np
    np.random.seed(seed)
    data = np.random.randint(vmin, vmax, size=20)
    mean = data.mean()
    std = data.std()
    noise = np.random.normal(loc=mean, scale=std ** .5, size=size)
    fake_x = np.array([-5 + i * 20 / size for i in range(size)])

    linear = lambda x, k=(.5 - np.random.rand()) * 15, b=np.random.rand() * 10: k * x + b
    linear_data = linear(fake_x)
    fake_y = linear_data + noise
    return fake_x, fake_y
#print(get_numbers(9))
#print(fake_data_generator(9, 6, 22, 57))
x, y = fake_data_generator(9, 6, 22, 57)
#print(x, y, sep='\n\n')
plt.plot(x, y)
#print(len(x))
xxerr = np.array([abs(x[i+2]-x[i])/2 for i in range(0, len(x)-2)])
xxerr = np.append(xxerr, (x[56]-x[54])/2)
xxerr = np.append(xxerr, (x[56]-x[54])/2)
srxy = sum(x*y)/len(x)
srx = sum(x)/len(x)
sry = sum(y)/len(y)
srx2 = sum(x*x)/len(x)
b = (srxy-srx*sry)/(srx2 - srx*srx)
a = sry - b*srx
plt.plot(np.array([-5, 15]), np.array([a + b*(-5), a + 15*b]), "k--", label="fit")

plt.grid(which='major', axis='both', alpha=1)
plt.errorbar(x, y, xerr = xxerr, yerr = y**0.5, fmt='.', label='Cross')

midlex = np.array([sum(x)/len(x), sum(x)/len(x)])
linex = np.array([-10,50])

midley = np.array([sum(y)/len(y), sum(y)/len(y)])
liney = np.array([-5,15])

plt.ylabel(r"$\rho, mm^{-3}$")
plt.xlabel(r"$\xi, cm$")

plt.plot(midlex, linex, "b--", label='mean x = 4.8245614')
plt.plot(liney, midley, "r--", label='mean y = 10.39131121')
plt.legend()
plt.show()
print(midley)
#print(len(xxerr))
