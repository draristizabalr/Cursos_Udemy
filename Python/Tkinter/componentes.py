import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

class VentanasTabuladores(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('650x400+605+340')
        self.title('Componentes')
        self.iconbitmap('icono.ico')

        self.crear_tabs()

    def crear_componentes_tabulador1(self, tabulador):
        # Agregar una etiqueta y un componente de entrada
        self.entrada1 = tk.Entry(tabulador, width=30)
        self.entrada1.grid(row=0, column=1, padx=5, pady=5)
        self.etiqueta1 = tk.Label(tabulador, text='Nombre:')
        self.etiqueta1.grid(row=0, column=0, sticky='E')
        self.boton1 = ttk.Button(tabulador, text='Enviar', command=self.enviar)
        self.boton1.grid(row=1, column=0, columnspan=2)

    def enviar(self):
        messagebox.showinfo('Mensaje', f'Nombre: {self.entrada1.get()}')



    def crear_componentes_tabulador2(self, tabulador):
        self.contenido = 'Este es mi texto con el contenido'
        # Creamos el componente de scroll
        self.scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        self.scroll.insert(tk.INSERT, self.contenido)
        # Mostramos componente
        self.scroll.grid(row=0, column=0)

    def crear_componentes_tabulador3(self, tabulador):
        # Creamos una lista usando una list_comprehension
        self.datos = [f'{x+1}' for x in range(10)]
        self.combobox = ttk.Combobox(tabulador, width=15, values=self.datos, state='readonly')
        self.combobox.grid(row=0, column=0, padx=10, pady=10)
        # Seleccionamos un elemento por default
        self.combobox.current(5-1)
        self.boton1 = ttk.Button(tabulador, text='Mostrar valor seleccionado', command=self.mostrar_valor)
        self.boton1.grid(row=0, column=1)

    # Agregar un botón para saber que opción seleccionó el usuario
    def mostrar_valor(self):
        messagebox.showinfo('Valor Seleccionado', f'Valor seleccionado: {self.combobox.get()}')



    def crear_componentes_tabulador4(self, tabulador):
        self.imagen = tk.PhotoImage(file='imagen.png')
        self.boton_imagen = ttk.Button(tabulador, image=self.imagen, command=self.mostrar_titulo)
        self.boton_imagen.grid(row=0, column=0)

    def mostrar_titulo(self):
        messagebox.showinfo('Información', f'Nombre de la imagen: {self.imagen.cget("file")}')


    def crear_componentes_tabulador5(self, tabulador):
        # Creamos el componente de barra de progreso
        self.barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
        self.barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        # Agregar los botones para controlar nuestra barra de progreso
        self.boton_inicio = ttk.Button(tabulador, text='Ejecutar Barra de Progreso', command=self.ejecutar_barra)
        self.boton_inicio.grid(row=1, column=0)
        self.boton_ciclo = ttk.Button(tabulador, text='Ejecutar ciclo', command=self.ejecutar_ciclo)
        self.boton_ciclo.grid(row=1, column=1)
        self.boton_detener = ttk.Button(tabulador, text='Detener ejecución', command=self.detener)
        self.boton_detener.grid(row=1, column=2)
        self.boton_despues = ttk.Button(tabulador, text='Detener Ejecución después', command=self.detener_despues)
        self.boton_despues.grid(row=1, column=3)

    def ejecutar_barra(self):
        self.barra_progreso['maximum'] = 100
        for valor in range(101):
            # Mandamos a esperar un poco antes de continuar con la ejecución de la barra
            sleep(0.01)
            # Incrementamos nuestra barra de progreso
            self.barra_progreso['value'] = valor
            # Actualizamos nuestra barra de progreso
            self.barra_progreso.update()
        messagebox.showinfo('Final Exitoso', 'Se ha completado la barra de progreso exitosamente')

    def ejecutar_ciclo(self):
        self.barra_progreso.start()

    def detener(self):
        self.barra_progreso.stop()

    def detener_despues(self):
        self.esperar_ms = 1000
        self.after(self.esperar_ms, self.barra_progreso.stop)




    def crear_tabs(self):
        # Creamos un tab control, para ello también usamos la clase Notebook
        control_tabulador = ttk.Notebook(self)

        # Agregamos un marco (frame) para agregar dentro del tab y organizar
        tabulador1 = ttk.Frame(control_tabulador)
        # Agregamos el tabulador al contexto de tabuladores
        control_tabulador.add(tabulador1, text='Tabulador 1')
        # Mostramos el tabulador
        control_tabulador.pack(fill='both')
        # Creamos los componentes del tabulador1
        self.crear_componentes_tabulador1(tabulador1)

        # Creamos un segundo tabulador
        tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido')
        control_tabulador.add(tabulador2, text='Tabulador 2')
        # Creamos los componentes para el segundo tabulador
        self.crear_componentes_tabulador2(tabulador2)

        # Crear un tercer tabulador
        tabulador3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador3, text='Tabulador 3')
        # Creamos los componentes del tercer tabulador
        self.crear_componentes_tabulador3(tabulador3)

        # Crear cuarto tabulador
        tabulador4 = ttk.LabelFrame(control_tabulador)
        control_tabulador.add(tabulador4, text='Tabulador 4')
        # Creamos los componentes del cuarto tabulador
        self.crear_componentes_tabulador4(tabulador4)

        # Creamos un quinto tabulador
        tabulador5 = tk.LabelFrame(control_tabulador, text='Progress Bar')
        control_tabulador.add(tabulador5, text='Tabulador 5')
        # Creamos los componentes del tabulador 5
        self.crear_componentes_tabulador5(tabulador5)

if __name__ == '__main__':
    ventana_tabuladores = VentanasTabuladores()
    ventana_tabuladores.mainloop()

