import tkinter as tk

# Configuracion de ventana
ven = tk.Tk()
ven.geometry('900x600')
ven.title('Label')
ven.configure(background = '#188888')

# Etiquetas
lbl1 = tk.Label(ven, text = 'Hi..')
lbl1.pack()

ven.mainloop()
