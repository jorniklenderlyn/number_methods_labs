import matplotlib.pyplot as plt
import numpy as np 

f = lambda x: -2 + np.sin(x) + np.cos(x)**2 + np.log(x)

a, b = 4.2, 7
x = np.arange(a, b, 0.1)
y = f(x)

plt.plot(x, y)
plt.plot([a, b], [0, 0])
plt.show()
