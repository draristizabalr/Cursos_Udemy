# GUI - Graphical User Interface
# Tkinter - TK Interface
# Importamos el modulo de tkinter
import tkinter as tk
# Importamos el modulo del tema de Tkinter
from tkinter import ttk

# Creamos un objeto usando la clase tk
ventana = tk.Tk()

# Modificamos el tamaño  de la ventana (pixeles)
ventana.geometry('600x400')

# Cambiar el nombre de la ventana
ventana.title('Nueva Ventana')

# Configuración de ícono
ventana.iconbitmap('icono.ico')

# Creamos el método
def evento_click():
    boton1.config(text='Botón presionado')
    print('Ejecución del evento_click')

    # Creamos un nuevo botón y lo mostramos
    boton2 = ttk.Button(ventana, text='Salir')
    boton2.pack()

# Creamos un botón (también conocido como widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)
# Utilizar el pack layout manager para mostrar el botón de la ventana
boton1.pack()
# Iniciamos la ventana (esta línea se ejecuta al final)
# Si se ejecuta antes, no se muestran los cambios
ventana.mainloop()
