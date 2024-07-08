###just testing my python skills on random projects"
import matplotlib.pyplot as plt
import numpy as np
import Django as d
x = np.array([0,1,2,3,4,5])
y = np.array([1,0,3,8,5,6])

plt.subplot(2,1,1)
plt.plot(x,y)

x = np.array([0,1,2,3,4,5])
y = np.array([1,0,3,8,5,6])
plt.title("purchases")

plt.subplot(2,1,2)
plt.plot(x,y)
plt.title("sales")

plt.suptitle("Monthly reports")
plt.show()

