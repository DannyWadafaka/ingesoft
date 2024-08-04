from observer import Observer
import tkinter as tk

class ColorList(tk.Toplevel, Observer):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("200x100")
        self.title("Color list")
        self.list = tk.Listbox(self)
        self.list.pack()

    def sendNotify(self, color: str):
        self.list.insert(tk.END, color.capitalize())
