from tkinter import *
import tkinter as tk

root = Tk()

w = 1000
h = 500

hh = h / 2
hw = w / 2

qh = h / 4
qw = w / 4


canvas = Canvas(root, width=w, height=h, bg="white")
canvas.pack()
canvas.create_line(0, hh + qh, w, hh + qh, fill='blue', arrow=tk.LAST)
canvas.create_line(hw, h, hw, 0, fill='red', arrow=tk.LAST)

a = 100
T1 = [300] * a
T2 = [300] * a
b = 10
c = [0] * a
f = [300] * a
T1[0] = 600
h = 4 * 10 ** (-7)
t = 0.000000001
x = 162
C = 703
r = 2330
A = x / (C * r)
L = A * t / (h ** 2)
check = 1
print(L)
ovals = [0] * a
Time = 0

for i in range(a):
    ovals[i] = canvas.create_oval((w - a * 5) / 2 + i * 5, hh + qh - 2.5 - T1[i] / 3, (w - a * 5) / 2 + 5 + i * 5,
                                  hh + qh + 2.5 - T1[i] / 3, fill="lightgrey", outline="black")


# print (c)


def moving():
    for k in range(0, a - 1):
        c[k] = L / (1 + 2 * L - L * c[k - 1])
        f[k] = (T1[k] + L * f[k - 1]) / (1 + 2 * L - L * c[k - 1])
        T2[k] = c[k] * T2[k + 1] + f[k]
        T2[a - 1] = T2[a - 2]
        if T2[50] < 450:
            global check
            if check == 1:
                global Time
                Time += t
            else:
                print(Time)
                check = 0
    for k in range(a):
        T2[0] = 600
        canvas.move(ovals[k], 0, -(T2[k] - T1[k]) / 3)
        T1[k] = T2[k]
    canvas.after(1, moving)


def eventtreatment(self):
    moving()


root.bind("<Return>", eventtreatment)

canvas.pack()
root.mainloop()
