import matplotlib.pyplot as plt
import numpy as np

#Number of intervals N = 10000
N = 10000
x = np.linspace(0, 10, 10000 + 1)
y = np.sin(x) * np.exp(-x/10)
fig, ax= plt.subplots(2,1)
ax[0].plot(x, y)

#Calculate mean, and standard deviation, limiting the y array with logic
print(np.mean(y[(x>=4)*(x<=7)]))
print(np.std(y[(x>=4)*(x<=7)]))

#Calculate the percentile > 80
print(np.percentile(y[(x>=4)*(x<=7)], 80))

#Ploting the derivative
ax[1].plot(x, np.gradient(y,x))
plt.show()

#Finding Zeros
dydx = np.gradient(y,x)
#Compare the adjecent values for dydx, it's only < 0 when dydx = 0
print(x[1:][dydx[1:] * dydx[:-1] < 0])
