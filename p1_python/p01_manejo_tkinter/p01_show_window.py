import tkinter

# Crear una ventana
vent = tkinter.Tk()

# Definir dimension
vent. geometry('900x600')
vent.resizable(0, 0) 			# No se redimensiona la ventana

vent.configure(backgroun = '#268f92')	# Azul extraño en ventana
vent.title('1ra Ventana')

# Hacer visible
vent.mainloop()
