import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('POO con PySide')
        # self.resize(600, 400)
        # Forma de colocar el tamaño de la ventana fija
        self.setFixedSize(QSize(600,400))
        # Llamar el método para crear componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregamos un menú
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # Agregamos algunas opciones al menú
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        # Agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        # Agregamos un mensaje a nuestra barra de estado
        self.statusBar().showMessage('Información de la barra de estado')
        # Agregamos un componente de botón
        boton = QPushButton('Nuevo Botón')
        # Publicamos el botón en la ventana
        self.setCentralWidget(boton)
        boton.setStatusTip('Acción del botón en construcción'.center(50,'⚠'))

if __name__ == '__main__':
    app = QApplication([])
    # Creamos un objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos nuestra ventana
    sys.exit(app.exec())