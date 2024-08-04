from observer import Observer
import tkinter as tk

class ColorFrame(tk.Toplevel, Observer):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("200x100")
        self.title("Color frame")

    def sendNotify(self, color: str):
        self.configure(bg=color)
