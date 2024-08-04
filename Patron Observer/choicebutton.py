import tkinter as tk

class ChoiceButton(tk.Radiobutton):

    def __init__(self, rt, color, index, gvar, command):
        super().__init__(rt, text=color, padx=20, variable=gvar, value=index, command=command)
        self.pack(anchor=tk.W)
