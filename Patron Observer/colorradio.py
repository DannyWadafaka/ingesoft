from subject import Subject
import tkinter as tk
from choicebutton import ChoiceButton

class ColorRadio(Subject):
    def __init__(self, root):
        super().__init__()
        root.geometry("300x100")
        root.title("Subject (Data)")
        self.var = tk.IntVar()
        self.colors = ["Red", "Green", "Blue"]


        ChoiceButton(root, 'Red', 0, self.var, self.colrChange)
        ChoiceButton(root, 'Green', 1, self.var,  self.colrChange)
        ChoiceButton(root, 'Blue', 2, self.var,  self.colrChange)
        self.var.set(None)

    def colrChange(self):
        cindex = self.var.get()
        if cindex is not None:
            color = self.colors[cindex]
            self.notifyObservers(color)
         




 


