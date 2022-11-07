import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7])
a4 = np.random.random(10)
a6 = np.linspace(0,10, 100)
a7 = np.arange(0, 10, 0.02)

#Plot multiple graphs in a dashboard
fig, ax = plt.subplots(2,2)
ax[0, 0].plot(a6, a6**2)
ax[0, 1].plot(a1, a1**3)
ax[1, 0].hist(a4)
ax[1, 1].plot(a7, a7**2 + 6)
plt.show()

#Return a list for y, property of numpy
def f(x):
    return x**2 * np.sin(x) / np.exp(-x)
x = np.linspace(0, 10, 100)
y = f(x)
plt.plot(x,y)
plt.show()

#Statistic with numpy
a1 = 2*np.random.randn(10000) + 10
print(np.mean(a1))
print(np.std(a1))
print(np.percentile(a1, 80))

#Calculus with numpy
x = np.linspace(1, 10, 100)
y = 1/x**2 * np.sin(x)
dydx = np.gradient(y, x)
y_int = np.cumsum(y) * (x[1] - x[0])
plt.plot(x,y)
plt.plot(x , dydx)
plt.plot(x, y_int)
plt.show()

#Print meshgrid for z = y^2 + x^2
x = np.linspace(0, 10, 1000)
y = np.linspace(0, 10, 1000)
xv, yv = np.meshgrid(x, y)
zv = xv**2 + yv**2
plt.contourf(xv, yv, zv, levels=100)
plt.colorbar()
plt.show()