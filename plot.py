import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,20,30,40,50)
y = x **2 + x*2 +8
plt.plot(x, y)
plt.show()