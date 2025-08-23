import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

ven = tk.Tk()
ven.geometry('300x250')
ven.resizable(0,0)
ven.title('Login')
ven.configure(background = '#888888')

ven.columnconfigure(0, weight = 1)
ven.rowconfigure(0, weight = 1)

# Creacion Un Estilo
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure(ven, background = "#288888", foreground = 'white', fieldbackground = 'black')


# Funcion
def enviar(event):
    v_user = txbox_user.get()
    v_pass = txbox_pass.get()
    # User -> Basy
    # Password -> Loca_Number_1
    if v_user == 'Basy' and v_pass == 'Loca_Number_1':
        showinfo(title = 'Login', message = 'Correct Start!')
    else:
        showwarning(title = 'Error', message = 'Data Invalid!')
    print ( 'Hi')

# Crear, configura y agrega Frame
frame = ttk.Frame(ven)
frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 3)


# Labels
lbl1_login = ttk.Label(frame, text = 'Login', font = ('Arial', 15))
lbl1_login.grid(row = 0, column = 0, columnspan = 2)

lbl2_user = ttk.Label(frame, text = 'User:', font = ('Arial', 10))
lbl2_user.grid(row = 1, column = 0,sticky = tk.W, padx = 5, pady = 5)

lbl3_pass = ttk.Label(frame, text = 'Password:', font = ('Arial', 10))
lbl3_pass.grid(row = 2, column = 0, sticky = tk.W, padx = 5, pady = 5)

# Text Box
txbox_user = ttk.Entry(frame)
txbox_user.grid(row = 1, column = 1, padx = 5, pady = 5)

txbox_pass = ttk.Entry(frame, show = '*')
txbox_pass.grid(row = 2, column = 1, padx = 5, pady = 5)

#Button
btn1_send = ttk.Button(frame, text = 'Send')
btn1_send.grid(row = 3, column = 0, columnspan = 2, pady = 5)

# Eventos de Boton
btn1_send.bind('<Return>', enviar)		# Precina Enter
btn1_send.bind('<Button-1>', enviar)		# Click Izquierdo

frame.grid(row = 0, column = 0)

ven.mainloop()
