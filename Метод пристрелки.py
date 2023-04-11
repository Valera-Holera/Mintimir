import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy import optimize

plt.style.use('default')

g = 9.8
y0 = 0
tf = 10


def f(t, r):
    y, v = r
    dy_dt = v  # velocity
    d2y_dt2 = -g  # acceleration
    return dy_dt, d2y_dt2


@np.vectorize
def shooting_eval(v0):
    sol = solve_ivp(f, (t[0], t[-1]), (y0, v0), t_eval=t)
    y_num, v = sol.y
    return y_num[-1]


v0 = 60  # guess
t = np.linspace(0, tf, 51)

fig, ax = plt.subplots()
# v0 = np.linspace(0, 100, 100)

v0 = optimize.newton(shooting_eval, 50)
sol = solve_ivp(f, (0, tf), (y0, v0), t_eval=t)
y, v = sol.y
print(v0)
plt.plot(t[0], y0, 'ro', label=f'Solution: {v0:.1f}')
plt.plot(t[-1], 0, 'ro', label=f'Solution: {v0:.1f}')
plt.plot(t, y, ".")
plt.grid(True)
ax.set_xlabel('t')
ax.set_ylabel('y')
plt.show()
