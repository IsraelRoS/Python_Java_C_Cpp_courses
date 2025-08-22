import tkinter as tk
from tkinter import ttk

ven = tk.Tk()
ven.geometry('500x350')
ven.title('TextBox')
ven.configure(background = '#155555')

def enviar():
    text_got = txbox1.get()
    print ('The Nudes were sent')
    lbl1['text'] = text_got

txbox1 = ttk.Entry(ven, font = ('Arial', 15)) # Caja de entrada de texto
txbox1.pack(pady = 15)

btn1 = ttk.Button(ven, text = 'Send Nudes', command = enviar)
btn1.pack(pady = 10)

lbl1 = ttk.Label(ven, text = "Just Do It!!")
lbl1.pack(pady = 10)

ven.mainloop()
