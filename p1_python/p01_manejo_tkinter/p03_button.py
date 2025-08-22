import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

ven = tk.Tk()
ven.geometry('500x300')
ven.title('Button')
ven.configure(background = '#188888')

def saludar():
    print ('Hola Individuo...')
    showinfo(title = 'Mensaje', message = 'Te obsevo!')

btn1 = tk.Button(ven, text = 'Hi', command = saludar)	# Crea Boton en ven
btn1.pack()				# Muestra el boton

ven.mainloop()
