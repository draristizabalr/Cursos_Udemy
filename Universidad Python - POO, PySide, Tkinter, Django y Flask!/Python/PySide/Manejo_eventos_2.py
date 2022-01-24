# Signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Botón
        self.boton = QPushButton('Click aquí')
        # Asociar la señal de click al slot evento_click
        self.boton.clicked.connect(self._evento_click)
        # Vamos a conectar a la señal de cambio de título
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        # Publicación del botón
        self.setCentralWidget(self.boton)

    def _evento_click(self):
        # Cambiar el texto del botón y el título de la ventana
        self.boton.setText('Nuevo texto botón')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo Título Aplicación')
        print('Evento click')

    def cambio_titulo_aplicacion(self, nuevo_titulo):
        print(f'Nuevo título de la aplicación: {nuevo_titulo}')


if __name__ == '__main__':
    # Creamos un objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
