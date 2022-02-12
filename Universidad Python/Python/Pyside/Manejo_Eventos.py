# Signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Botón
        boton = QPushButton('Click aquí')
        # Conectamos el evento checado (por default es False) (cambia el color al accionarlo)
        boton.setCheckable(True)
        # Conectamos otro slot al evento checar
        boton.clicked.connect(self._evento_checar)
        # Conectamos el evento (Signal) click con el slot (evento_click)
        boton.clicked.connect(self._evento_click)
        # Publicación del botón
        self.setCentralWidget(boton)

    def _evento_click(self):
        print('Has hecho click')
        # Accedemos al estado del botón (checado)
        print(f'Botón cheado desde evento click: {self.boton_checado}')

    def _evento_checar(self, checar):
        self.boton_checado = checar
        print(f'Checado? {self.boton_checado}')


if __name__ == '__main__':
    # Creamos un objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
    