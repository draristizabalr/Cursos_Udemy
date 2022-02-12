import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# width es la cantidad de caracteres que ocupa nuestra caja
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
# state=tk.DISABLED hace que se deshabilite la caja de texto y no se pueda usar más
entrada_var1 = tk.StringVar(value='')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.LEFT, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

etiqueta1 = tk.Label(text='')
etiqueta1.grid(row=1, column=0, columnspan=2)

# insert agrega texto
entrada1.insert(0, 'Introduce un nombre')
# Vamos a configurar para que no se pueda modificar la cadena dentro de la caja de texto
# entrada1.config(state='readonly')

# Método
def enviar():
    etiqueta1.config(text=f'Hola {entrada_var1.get()}')
    entrada1.select_range(0, tk.END)
    entrada1.focus()

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()