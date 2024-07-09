###just testing my python skills on random projects"

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,4,5,6,5])
y = np.array([2,4,5,2,5,6])
plt.title("sales")
plt.grid(axis='x')
plt.xlim()
plt.ylim()
plt.plot(x,y,"*--")
plt.show()

