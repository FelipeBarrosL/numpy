import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)
xv, yv = np.meshgrid(x, y)
zv = np.exp(-(xv**2 + yv**2)) * np.sin(xv)
plt.contourf(xv, yv, zv, levels=100)
plt.colorbar()

#Find volume
vol = np.abs(zv.ravel()).sum() * np.diff(x)[0] * np.diff(y)[0]
print(vol)
vol2 = np.abs(zv[np.sqrt(xv**2 + yv**2) > 0.5].ravel()).sum() * np.diff(x)[0] * np.diff(y)[0]
print(vol2)
plt.show()


