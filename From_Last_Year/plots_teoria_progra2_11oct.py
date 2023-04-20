import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)

print(x)

plt.plot(x, x**2, "r", x, x, "b", x, x*np.log2(x), "g", np.log2(x), "--")
plt.show()
