import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')

# Definimos una variable podremos modificar posteriormente (set), leer (get)
entrada1 = ttk.Entry(ventana, width=30, justify=tk.LEFT)
entrada1.grid(row=0, column=0)

# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

# insert agrega texto
# entrada1.insert(0, 'Introduce un nombre')
# entrada1.insert(tk.END, '.')


# Método
def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()

def enviar():
    print(entrada1.get())
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')

def crear_menu():
    # Vamos a configurar el menu principal
    menu_principal = Menu(ventana)
    # tearoff = False, para que no se separe de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=False)
    # Agregamos una nueva opción al menu de archivo
    submenu_archivo.add_command(label='Nuevo')
    submenu_archivo.add_separator()
    submenu_archivo.add_command(label='Salir', command=salir)
    # creamos el submenu de 'Ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    submenu_ayuda.add_command(label='Acerca de')
    # Agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    # Mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()

ventana.mainloop()