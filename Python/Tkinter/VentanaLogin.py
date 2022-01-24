# Ejercicio: Desarrollar una ventana de login
import tkinter as tk
from tkinter import ttk, messagebox

class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        # Damos las primeras configuraciones a nuestra ventana
        # Dimensiones de la ventana
        self.geometry('300x130')
        # Titulo
        self.title('Login')
        # Proporciones de las filas y columnas internas de la ventana
        self.rowconfigure(0, weight=1)       # Proporción de la primera fila
        self.rowconfigure(1, weight=1)       # Proporción de la segunda fila
        self.rowconfigure(2, weight=2)       # Proporción de la tercera fila
        self.columnconfigure(0, weight=1)    # Proporción de la primera columna
        self.columnconfigure(1, weight=10)    # Proporción de la segunda columna

        self._crear_componentes()

    def _crear_componentes(self):
        # Comenzamos a agregar objetos (widgets) a la ventana
        # Etiquetas
        etiqueta_usuario = tk.Label(self, text='Usuario:')
        etiqueta_usuario.grid(row=0, column=0, sticky='E')
        etiqueta_password = tk.Label(self, text='Password:')
        etiqueta_password.grid(row=1, column=0, sticky='E')
        # Cajas de texto
        self.entrada_usuario_var = tk.StringVar(value='')
        entrada_usuario = tk.Entry(self, width=35, textvariable=self.entrada_usuario_var)
        entrada_usuario.grid(row=0, column=1)
        self.entrada_password_var = tk.StringVar(value='')
        entrada_password = tk.Entry(self, width=35, show='*', textvariable=self.entrada_password_var)
        entrada_password.grid(row=1, column=1)
        # Boton
        boton_loggin = ttk.Button(self, text='Login', command=self._informacion)
        boton_loggin.grid(row=2, column=0, columnspan=2)


    def _informacion(self):
        # Método del Boton
        messagebox.showinfo('Información Login', f'Usuario: {self.entrada_usuario_var.get()}\n'
                                                 f'Password: {self.entrada_password_var.get()}')

if __name__ == '__main__':
    ventana_login = VentanaLogin()
    ventana_login.mainloop()