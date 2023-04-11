import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.cos(x)


h = 0.1
x = np.arange(0, 3 + h, h)
y0 = 0

y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h * f(x[i] + h / 2, y[i] + h / 2 * f(x[i], y[i]))

plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo--', label='Approximate')
plt.plot(x, np.sin(x), 'g', label='Exact')
plt.title('Approximate and Exact solution for simple ODE')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend(loc='upper right')
plt.show()
