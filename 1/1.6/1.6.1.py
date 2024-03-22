import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
print(type(x))
print(x)
y = np.sin(x)

plt.plot(x, y)
plt.show()