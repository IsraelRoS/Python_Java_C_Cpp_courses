import tkinter as tk
from tkinter import ttk

ven = tk.Tk()
ven.geometry('500x200')
ven.resizable(0,0)
ven.configure(background = '#155552')
ven.title('Grid')

#Configurar Grid
#- Columnas
ven.columnconfigure(0, weight = 1)
ven.columnconfigure(1, weight = 2)
ven.columnconfigure(2, weight = 1)
#- Filas
ven.rowconfigure(0, weight = 1)
ven.rowconfigure(1, weight = 2)
ven.rowconfigure(2, weight = 1)

#Posicionamiento Grid en botones
btn1 = ttk.Button(ven, text = 'Boton1')
btn2 = ttk.Button(ven, text = 'Boton2')
btn3 = ttk.Button(ven, text = 'Boton3')

btn1.grid (row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)		# sticky posiciona el botton en el lado izquierdo dentro de la fila y  la columna
btn2.grid (row = 1, column = 1, ipadx = 10, ipady = 10)
btn3.grid (row = 2, column = 2, sticky = tk.S)

ven.mainloop()

