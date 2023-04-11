import tkinter as tk
from tkinter import *

root = Tk()

w = 1000
h = 500

hh = h / 2
hw = w / 2

canvas = Canvas(root, width=w, height=h, bg="lightgrey")
canvas.create_line(0, hh, w, hh, fill='blue', arrow=tk.LAST)
canvas.create_line(hw, h, hw, 0, fill='red', arrow=tk.LAST)

canvas.pack()
root.mainloop()
