import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

# Creacion de ventana
ven = tk.Tk()
ven.geometry('600x300')
ven.resizable(0,0)
ven.title('Table')
ven.configure(background = '#188888')

#configurar columnas de ventana principal
ven.columnconfigure(0, weight = 1)
ven.columnconfigure(1, weight = 0)

# Crear Estilo
estilo = ttk.Style()
estilo.theme_use('clam') 			# Tema Oscuro
estilo.configure('Treeview', background = 'black', foreground = 'white', fieldbackground = 'black', rowheight = 30)  # rowheight dimencion del renglon
estilo.map('Treeview', background = [('selected', '#550088')])			# Cambia el color del elemento seleccionado

# Definir columnas
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ven, columns = columnas, show = 'headings')

# Formato de columna
tabla.column('Id', width = 60, anchor = tk.CENTER)
tabla.column('Nombre', width = 120, anchor = tk.CENTER)
tabla.column('Edad', width = 60, anchor = tk.CENTER)

# Cabecera de tabla
tabla.heading('Id', text = 'Id') #, anchor = tk.CENTER ) # posiciona la cabecera
tabla.heading('Nombre', text = 'Name')
tabla.heading('Edad', text = 'Age')

# Carga datos
datos = ((1, 'Basy', 7),(2, 'Matias', 32))
print(type(datos))
for pet in datos:
    tabla.insert(parent = '', index = tk.END, values = pet)

tabla.grid(row = 0, column = 0, sticky = tk.NSEW)

# Crear scrollbar
scrollbar = ttk.Scrollbar(ven, orient = tk.VERTICAL, command = tabla.yview)
tabla.configure(yscroll = scrollbar.set)
scrollbar.grid(row = 0, column = 1, sticky = tk.NS)

def mostrar_seleccion(event):
    print('hi')
    elemento_seleccionado = tabla.selection()[0] # item seleccionado
    elemento = tabla.item(elemento_seleccionado) # item
    mascota = elemento['values'] 		 # tupla de mascota
    print(mascota)
    showinfo(title = 'Pet', message = f'{mascota[1]}')

# Asocia el evento del mouse en la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_seleccion)


ven.mainloop()

