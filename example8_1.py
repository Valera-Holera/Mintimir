# example8_1
import numpy as np
import run_kut4
import linInterp
import printSoln


def initCond(u):
    # Начальные значения [y,y’] на левой границе;
    # u используется для обозначения
    # предполагаемого граничного условия для y'(a)
    return np.array([0.0, u])


def r(u):
    # Вводим r(u) как функцию расхождения полученного значения на правой
    # границе и требуемого значения β = y(b)
    # r(u) = θ(u) - β => 0
    X, Y = run_kut4.integrate(F, xStart, initCond(u), xStop, h)
    y = Y[len(Y) - 1]
    r = y[0] - 1.0
    return r


def F(x, y):
    # ОДУ 1 порядка для y'' + 3*y*y' = 0, y(0) = 0, y(2) = 1
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -3.0*y[0]*y[1]
    return F


xStart = 0.0  # Start of integration
xStop = 2.0   # End of integration
u1 = 1.0      # 1st trial value of unknown init. cond.
u2 = 2.0      # 2nd trial value of unknown init. cond.
h = 0.1       # Step size
freq = 1      # Printout frequency
# Вычисляем где функция ошибки будет равна 0
u = linInterp.linInterp(r, u1, u2)
X, Y = run_kut4.integrate(F, xStart, initCond(u), xStop, h)
printSoln.printSoln(X, Y, freq)
