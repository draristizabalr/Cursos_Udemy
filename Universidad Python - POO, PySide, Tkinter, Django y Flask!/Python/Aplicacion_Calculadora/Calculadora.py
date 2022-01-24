import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0, 0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        # Atributos de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor de input
        self.entrada_texto = tk.StringVar()
        # Método para crear nuestros componentes
        self._creacion_componentes()

    # Método de creación de componentes
    def _creacion_componentes(self):
        # Crear primer frame de la ventana
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)
        # Caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'),
                           textvariable=self.entrada_texto, width=30, justify=tk.RIGHT,
                           state='readonly')
        entrada.grid(row=0, column=0, ipady=10)

        # Crear segundo frame de la ventana
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()
        # Creamos los botones de la calculadora

        # Primer renglón de botones
        # Botón borrar
        boton_c = tk.Button(botones_frame, text='C', justify=tk.CENTER,
                            width=32, height=3, bd=0, bg='#eee', cursor='hand2', command=self._borrar)
        boton_c.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        # Botón división
        boton_dividir = tk.Button(botones_frame, text='/', justify=tk.CENTER,
                                  width=10, height=3, cursor='hand2', bg='#eee', bd=0,
                                  command=lambda: self._evento_click('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)

        # Segundo renglón de botones
        # Botón 7
        boton_7 = tk.Button(botones_frame, text='7', justify=tk.CENTER,
                            width=10, height=3,bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('7'))
        boton_7.grid(row=1, column=0, padx=1, pady=1)
        # Botón 8
        boton_8 = tk.Button(botones_frame, text='8', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('8'))
        boton_8.grid(row=1, column=1, padx=1, pady=1)
        # Botón 9
        boton_9 = tk.Button(botones_frame, text='9', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('9'))
        boton_9.grid(row=1, column=2, padx=1, pady=1)
        # Botón multiplicar
        boton_multiplicar = tk.Button(botones_frame, text='*', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                                      command=lambda: self._evento_click('*'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)

        # Tercer renglón de botones
        # Botón 4
        boton_4 = tk.Button(botones_frame, text='4', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('4'))
        boton_4.grid(row=2, column=0, padx=1, pady=1)
        # Botón 5
        boton_5 = tk.Button(botones_frame, text='5', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('5'))
        boton_5.grid(row=2, column=1, padx=1, pady=1)
        # Botón 6
        boton_6 = tk.Button(botones_frame, text='6', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('6'))
        boton_6.grid(row=2, column=2, padx=1, pady=1)
        # Botón restar
        boton_restar = tk.Button(botones_frame, text='-', justify=tk.CENTER,
                                 width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                                 command=lambda: self._evento_click('-'))
        boton_restar.grid(row=2, column=3, padx=1, pady=1)

        # Cuarto renglón de botones
        # Botón 1
        boton_1 = tk.Button(botones_frame, text='1', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('1'))
        boton_1.grid(row=3, column=0, padx=1, pady=1)
        # Botón 2
        boton_2 = tk.Button(botones_frame, text='2', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('2'))
        boton_2.grid(row=3, column=1, padx=1, pady=1)
        # Botón 3
        boton_3 = tk.Button(botones_frame, text='3', justify=tk.CENTER,
                            width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('3'))
        boton_3.grid(row=3, column=2, padx=1, pady=1)
        # Botón sumar
        boton_sumar = tk.Button(botones_frame, text='+', justify=tk.CENTER,
                                width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                                command=lambda: self._evento_click('+'))
        boton_sumar.grid(row=3, column=3, padx=1, pady=1)

        # Quinto renglón de botones
        # Botón 0
        boton_0 = tk.Button(botones_frame, text='0', justify=tk.CENTER,
                            width=21, height=3, bg='#eee', cursor='hand2', bd=0,
                            command=lambda: self._evento_click('0'))
        boton_0.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        # Botón punto decimal
        boton_punto = tk.Button(botones_frame, text='.', justify=tk.CENTER,
                                width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                                command=lambda: self._evento_click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)
        # Botón igual
        boton_igual = tk.Button(botones_frame, text='=', justify=tk.CENTER,
                                width=10, height=3, bg='#eee', cursor='hand2', bd=0,
                                command=lambda: self._metodo_resultado())
        boton_igual.grid(row=4, column=3, padx=1, pady=1)



    def _borrar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento con la nueva expresión ya existente
        if elemento.isnumeric():
            self.expresion = f'{self.expresion}{elemento}'
            self.entrada_texto.set(self.expresion)
        elif elemento == '.':
            if self.expresion[-1].isnumeric():
                self.expresion = f'{self.expresion}{elemento}'
                self.entrada_texto.set(self.expresion)
        else:
            if self.expresion == '' and elemento == '-':
                self.expresion = f'{self.expresion}{elemento}'
                self.entrada_texto.set(self.expresion)
            elif self.expresion == '':
                self.expresion = ''
            elif self.expresion[-1].isnumeric():
                self.expresion = f'{self.expresion}{elemento}'
                self.entrada_texto.set(self.expresion)
            else:
                self.expresion = self.expresion[:-1]
                self.expresion = f'{self.expresion}{elemento}'
                self.entrada_texto.set(self.expresion)

    def _metodo_resultado(self):
        # eval evalúa una expresión str como una expresión aritmetica
        try:
            if self.expresion:
                self.expresion = str(eval(self.expresion))
                self.entrada_texto.set(self.expresion)
        except Exception as e:
            messagebox.showerror('ERROR', f'Ha ocurrido un error: {e}')
if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()