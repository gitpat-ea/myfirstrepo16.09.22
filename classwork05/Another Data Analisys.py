import numpy as np
from matplotlib import pyplot as plt

np.random.seed(42)
data = np.random.normal(10, 1, size=1000000)

# fig, axs = plt.subplots(1, 1, figsize=(6, 4.6))

# axs.hist(data, "auto", label="fine hist")

# axs.set_title("Interesting Data")
# axs.set_ylabel("Events")
# axs.set_xlabel("value")
# axs.legend()

x = data[500000:]
y = data[:500000]
xedges = np.linspace(8, 12, 39)
yedges = np.linspace(8, 12, 39)
distribution, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))

cs = plt.matshow(distribution)
plt.colorbar(cs)

# plt.tight_layout()
plt.show()

