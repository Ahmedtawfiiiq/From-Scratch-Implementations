import matplotlib.pyplot as plt
import numpy as np


x = [i for i in range(1, 9)]
y = [1, 2, 4, 8, 9, 10, 1, 2]


# scatter plot and generate a trend line
plt.scatter(x, y, color="red")
# from 0 to 4 make exponential trend line
z = np.polyfit(x[0:4], y[0:4], 2)
p = np.poly1d(z)
plt.plot(x[0:4], p(x[0:4]), "r--")
# from 4 to 6 make linear trend line
z = np.polyfit(x[3:6], y[3:6], 1)
p = np.poly1d(z)
plt.plot(x[3:6], p(x[3:6]), "r--")
# from 5 to 8 make exponential trend line
z = np.polyfit(x[5:8], y[5:8], 2)
p = np.poly1d(z)
plt.plot(x[5:8], p(x[5:8]), "r--")

plt.show()
