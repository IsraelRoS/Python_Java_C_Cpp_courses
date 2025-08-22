import tkinter as tk

# Configuracion de ventana
ven = tk.Tk()
ven.geometry('900x600')
ven.title('Label')
ven.configure(background = '#188888')

# Etiquetas
lbl1 = tk.Label(ven, text = 'Hi..')

lbl1.configure(text = 'metodo 2 para cambiar el text')
lbl1['text'] = 'metodo 3 para cambio de texto'
lbl1.pack(pady = 20)

ven.mainloop()
