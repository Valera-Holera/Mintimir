from tkinter import Tk, Canvas
import tkinter as tk

root = Tk()

w = 1000
h = 500

hh = h / 2
hw = w / 2

qh = h / 4
qw = w / 4

canvas = Canvas(root, width=w, height=h, bg="lightgrey")
canvas.pack()
canvas.create_line(0, hh, w, hh, fill='blue', arrow=tk.LAST)
canvas.create_line(hw, h, hw, 0, fill='red', arrow=tk.LAST)

canvas.create_oval(qw - 20, qh - 20, qw + 20, qh + 20)
canvas.create_rectangle(qw + hw - 20, qh - 20, qw + hw + 20, qh + 20)
points = [qw, qh + hh - 30, qw - 30, qh + hh + 30, qw + 30, qh + hh + 30]
canvas.create_polygon(points, fill="lightgrey", outline="black")

canvas.pack()
root.mainloop()
