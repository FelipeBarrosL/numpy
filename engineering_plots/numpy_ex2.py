import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)
r = 1 + 3/4 * np.sin(3*theta)
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x, y)

#Integral
A = 1/2 * sum(r**2) * (theta[1]-theta[0])

#Archlengh 
L = sum(np.sqrt((r**2) + np.gradient(r, theta)**2) * (theta[1]-theta[0]))
print(A)
print(L)
plt.show()