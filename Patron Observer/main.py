import tkinter as tk
from colorradio import ColorRadio
from colorframe import ColorFrame
from colorlist import ColorList



def main():
    # Crear la ventana principal
    root = tk.Tk()
    colr = ColorRadio(root)
    cframe = ColorFrame(None)
    clist = ColorList(root)
    
    root.iconbitmap('almuerzo-cohete.ico')
    clist.iconbitmap('almuerzo-cohete.ico')    #tener cuidado, puede dar error si no se tiene el icono
    cframe.iconbitmap('almuerzo-cohete.ico')


    colr.registerInterest(cframe)
    colr.registerInterest(clist)    

    # Ejecutar el bucle principal de la aplicación
    root.mainloop()


main()
