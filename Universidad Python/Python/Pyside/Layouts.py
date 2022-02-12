from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, \
    QPushButton


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana')
        # Creamos nuestros layouts
        layout_botones = QHBoxLayout()
        layout_vertical = QVBoxLayout()
        self.layout_dinamico = QStackedLayout()
        # Creamos los botones
        boton_amarillo = QPushButton('Amarillo')
        boton_amarillo.pressed.connect(lambda: self.cambiar_color(0))
        boton_azul = QPushButton('Azul')
        boton_azul.pressed.connect(lambda: self.cambiar_color(1))
        boton_rojo = QPushButton('Rojo')
        boton_rojo.pressed.connect(lambda: self.cambiar_color(2))
        # Agregamos los botones al primer layout
        layout_botones.addWidget(boton_amarillo)
        layout_botones.addWidget(boton_azul)
        layout_botones.addWidget(boton_rojo)
        layout_botones.setSpacing(15)
        # Agregamos los colores al QStackedLayout (es muy importante el orden en el que se agregan los colores)
        self.layout_dinamico.addWidget(Color('yellow'))     # Indice: 0
        self.layout_dinamico.addWidget(Color('blue'))       # Indice: 1
        self.layout_dinamico.addWidget(Color('red'))        # Indice: 2
        # Agregamos los anteriores layouts al layout vertical para darle la forma a nuestra ventana
        layout_vertical.addLayout(layout_botones)
        layout_vertical.addLayout(self.layout_dinamico)
        # Creamos un componente genérico para publicar
        componente = QWidget()
        componente.setLayout(layout_vertical)
        # Publicamos el componente
        self.setCentralWidget(componente)

    def cambiar_color(self, indice):
        self.layout_dinamico.setCurrentIndex(indice)


        # # Layout QStackedLayout
        # layout = QStackedLayout()
        # # Por default solo se visualiza el primer widget agregago
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('yellow'))
        # layout.setCurrentIndex(2)
        # # Creamos un componente genérico para publicar el layout
        # componente = QWidget()
        # componente.setLayout(layout)


        # # Layout tipo Grid
        # layout = QGridLayout()
        # # Agregamos componentes a nuestro layout
        # layout.addWidget(Color('red'), 0, 0)
        # layout.addWidget(Color('blue'), 1, 1)
        # layout.addWidget(Color('green'), 0, 2)
        # layout.addWidget(Color('yellow'), 1, 0)
        # layout.addWidget(Color('purple'), 1, 2)
        # # Creamos un componente genérico para publicar el layout
        # componente = QWidget()
        # componente.setLayout(layout)


        # # Anidar layouts (layout dentro de otro layout)
        # # Creamos en primer lugar un layout horizontal y después uno vertical
        # layout_horizontal = QHBoxLayout()
        # layout_vertical = QVBoxLayout()
        # # Agregamos un espacio a nuestro layout_vertical
        # layout_vertical.setContentsMargins(5, 10, 5, 10)
        # # Agregamos un espacio entre cada elemento del layout_vertical
        # layout_vertical.setSpacing(20)
        # # Agregamos una margen para nuestro layout_horizontal
        # layout_horizontal.setContentsMargins(10,20,10,20)
        # # Agregamos espacios entre los elementos del layout_horizontal
        # layout_horizontal.setSpacing(30)
        # # Agregamos algunos widgets al layout_vertical
        # layout_vertical.addWidget(Color('red'))
        # layout_vertical.addWidget(Color('green'))
        # layout_vertical.addWidget(Color('blue'))
        # # Agregamos el layout_vertical dentro del layout_horizontal
        # # Es decir, un layout anidado (un layout dentro de otro)
        # layout_horizontal.addLayout(layout_vertical)
        # # Agregamos más elementos al layout horizontal
        # layout_horizontal.addWidget(Color('yellow'))
        # layout_horizontal.addWidget(Color('orange'))
        # # Creamos un componente genérico para publicar el layout
        # componente = QWidget()
        # componente.setLayout(layout_horizontal)

        # # Layout horizontal
        # layout = QHBoxLayout()
        # # Agregamos un nuevo componente de color
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
        # # Creamos un componente genérico para publicar el layout
        # componente = QWidget()
        # componente.setLayout(layout)


        # # Layout Vertical
        # layout = QVBoxLayout()
        # # Agregamos un nuevo componente de color
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
        # # Creamos un componente genérico para publicar el layout
        # componente = QWidget()
        # componente.setLayout(layout)


        # # Publicamos el componente
        # self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
