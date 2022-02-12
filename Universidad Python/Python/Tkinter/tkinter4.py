import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')

# Definimos una variable podremos modificar posteriormente (set), leer (get)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.LEFT, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

# insert agrega texto
# entrada1.insert(0, 'Introduce un nombre')
# entrada1.insert(tk.END, '.')


# Método
def enviar():
    # Recuperamos la información a partir de la variable asociada con la caja de texto
    # Modificación utilizamos la variable de texto y el metodo set
    # Recuperar información ya modificada
    print(entrada_var1.get())
    print(entrada1.get())
    # Modificamos el texto del label
    etiqueta1.config(text=entrada_var1.get())

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()