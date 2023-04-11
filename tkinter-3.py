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
canvas.create_line(0, hh, w, hh, fill='blue', arrow=tk.LAST)
canvas.create_line(hw, h, hw, 0, fill='red', arrow=tk.LAST)

a = 100
ovals = [0] * a
for i in range(a):
    ovals[i] = canvas.create_oval((w - a * 5) / 2 + i * 5, hh - 2.5, (w - a * 5) / 2 + 5 + i * 5, hh + 2.5,
                                  fill="lightgrey", outline="black")


def moving():
    for k in range(a):
        canvas.move(ovals[k], 0, 1)
    canvas.after(100, moving)


def eventtreatment(self):
    moving()


root.bind("<Return>", eventtreatment)


canvas.pack()
root.mainloop()
