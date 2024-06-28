import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,2,4,6,8,10])
y = np.array([0,3,5,7,9,11])

plt.plot(x,y)

plt.xlabel(input("x axix :"))
plt.ylabel(input("y axix :"))

plt.show()