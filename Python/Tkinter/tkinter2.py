import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Configuración Grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    boton2.config(text='Botón 2 presionado')

def evento3():
    boton3.config(text='Botón 3 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')
    # Las personalizaciones de los botones solo se pueden hacer cuando se crea el botón con tk y no con ttk

# Definimos los botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=20, ipadx=20, ipady=50, columnspan=2, rowspan=2)
# pad: es para generar una margen a los bordes de la celda x=horizontal y=vertical
# ipad: es para generar una margen del texto con los bordes del botón x=horizontal y=vertical
# span: es para combinar celdas para un objeto row=filas y columns=columnas


# N (arriba), E (Derecha), S (abajo), W (Izquierda)
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
boton2.grid(row=1, column=0, sticky='NSWE')


boton3 = ttk.Button(ventana, text='Botón 3', command=evento3)
boton3.grid(row=0, column=1, sticky='NSWE')

boton4 = tk.Button(ventana, text='Botón 4', command=evento4)
boton4.grid(row=1, column=1, sticky='NSWE')


# Lanzamos la ventana con todas las configuraciones descritas
ventana.mainloop()
