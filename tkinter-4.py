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
for i in range(b):
    T1[int(a / 2 - b / 2) + i] = 600

for i in range(b):
    T2[int(a / 2 - b / 2) + i] = 600

ovals = [0] * a

for i in range(a):
    ovals[i] = canvas.create_oval((w - a * 5) / 2 + i * 5, hh + qh - 2.5 - T1[i] / 3, (w - a * 5) / 2 + 5 + i * 5,
                                  hh + qh + 2.5 - T1[i] / 3, fill="lightgrey", outline="black")


def moving():
    for k in range(1, a - 1):
        c[k] = 0.6 / (1 + 2 * 0.6 - 0.6 * c[k - 1])
        f[k] = (T1[k] + 0.6 * f[k - 1]) / (1 + 2 * 0.6 - 0.6 * c[k - 1])
        T2[k] = c[k] * T2[k + 1] + f[k]
    for k in range(a):
        canvas.move(ovals[k], 0, -(T2[k] - T1[k]) / 3)
        T1[k] = T2[k]

    canvas.after(100, moving)


def eventtreatment(self):
    moving()


root.bind("<Return>", eventtreatment)

canvas.pack()
root.mainloop()
