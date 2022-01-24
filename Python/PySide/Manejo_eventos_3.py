# Signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400, 200)
        # Definimos los elementos de etiqueta y linea de edición
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el widget de entrada de texto con la etiqueta
        # La señal es textChenged y el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        layout = QVBoxLayout()
        layout.addWidget(self.entrada_texto)
        layout.addWidget(self.etiqueta)
        # Contenedor para publicar el layout
        contenedor = QWidget()
        contenedor.setLayout(layout)
        # Publicar el contenedor, que incluye el resto de elementos
        self.setCentralWidget(contenedor)



if __name__ == '__main__':
    # Creamos un objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
