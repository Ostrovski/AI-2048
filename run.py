import tkinter as tk

from gui import Application
from problem import Problem

root = tk.Tk()
app = Application(root, Problem())
app.mainloop()