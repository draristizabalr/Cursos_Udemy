from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget, QLineEdit, \
    QSpinBox, QDoubleSpinBox, QSlider, QDial


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # QDial es una rueda similar al slider, utilizado para aplicaciones de audio
        componente = QDial()
        componente.setMinimum(500)
        componente.setMaximum(50000000)
        componente.setRange(500, 50000000)

        # Conectamos a las señales
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_valor)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)

        # Publicamos el QSlider
        self.setCentralWidget(componente)

    def cambio_valor(self, nuevo_valor):
        print(f'Valor seleccionado: ${nuevo_valor}')

    def slider_cambio_valor(self, nuevo_valor):
        print(f'Valor nuevo: {nuevo_valor}')

    def slider_presionado(self):
        print('El dial fué presionado')

    def slider_liberado(self):
        print('El dial se ha soltado')

        # # QSlider es para valores numéricos enteros en un slider (barra deslizadora)
        # componente = QSlider(Qt.Horizontal)
        # componente.setMinimum(500)
        # componente.setMaximum(50000000)
        # componente.setRange(500, 50000000)
        #
        # # Conectamos a las señales
        # componente.valueChanged.connect(self.cambio_valor)
        # componente.sliderMoved.connect(self.slider_cambio_valor)
        # componente.sliderPressed.connect(self.slider_presionado)
        # componente.sliderReleased.connect(self.slider_liberado)

        # # Publicamos el QSlider
        # self.setCentralWidget(componente)

    # def cambio_valor(self, nuevo_valor):
    #     print(f'Valor seleccionado: ${nuevo_valor}')
    #
    # def slider_cambio_valor(self, nuevo_valor):
    #     print(f'Valor nuevo: {nuevo_valor}')
    #
    # def slider_presionado(self):
    #     print('El slider fué presionado')
    #
    # def slider_liberado(self):
    #     print('El slider se ha soltado')


    #     # QSpinBox es para valores enteros
    #     numero = QSpinBox()
    #     # QDoubleSpinBox es para valores flotantes
    #     numero = QDoubleSpinBox()
    #     # Establecer un rango de valores
    #     numero.setMinimum(500)
    #     numero.setMaximum(50000000)
    #     numero.setRange(500, 50000000)
    #     # Establecer prefijos y sufijos al valor
    #     numero.setPrefix('$')
    #     numero.setSuffix(' pesos colombianos')
    #     # Establecer el salto (step)
    #     numero.setSingleStep(10)
    #     # Los eventos a los cuales nos podemos conectar son: cambio de valor y cambio de texto
    #     # Evento cambio de valor
    #     numero.valueChanged.connect(self.cambio_valor)
    #     # Evento cambio texto
    #     numero.textChanged.connect(self.cambio_texto)
    #
    #
    #     # Publicamos QSpinBox
    #     self.setCentralWidget(numero)
    #
    # def cambio_valor(self, nuevo_valor):
    #     print(f'Nuevo valor: {nuevo_valor}')
    #
    # def cambio_texto(self, nuevo_texto):
    #     print(f'Nuevo texto: {nuevo_texto}')

    #     self.linea_texto = QLineEdit()
    #     # Establecemos el máximo de caracteres a capturar
    #     self.linea_texto.setMaxLength(15)
    #     # Establecemos un texto de ayuda
    #     self.linea_texto.setPlaceholderText('Introduce número de celular')
    #     # Modo solo lectura
    #     # self.linea_texto.setReadOnly(True)
    #     # Validación (mask)
    #     self.linea_texto.setInputMask('+00-000-000-0000')
    #     # Evento enter, cambio selección de texto, cambio de texto
    #     # Evento Enter
    #     self.linea_texto.returnPressed.connect(self.enter_presionado)
    #     # Evento Cambio de Selección
    #     self.linea_texto.selectionChanged.connect(self.cambio_seleccion)
    #     # Evento Cambio de Texto
    #     self.linea_texto.textChanged.connect(self.cambio_texto)
    #
    #     # Publicar LineEdit
    #     self.setCentralWidget(self.linea_texto)
    #
    # def enter_presionado(self):
    #     print(f'El celular ingresado es: {self.linea_texto.text()}')
    #     self.linea_texto.clear()
    #
    # def cambio_seleccion(self):
    #     print('Cambio selección de texto')
    #     print(self.centralWidget().selectedText())
    #
    # def cambio_texto(self, nuevo_texto):
    #     print(f'Cambio de texto: {nuevo_texto}')


        # # Componente QListWidget se parece al combobox
        # lista = QListWidget()
        # lista.addItem('Uno')
        # lista.addItems(['Dos', 'Tres'])
        # # Monitoreamos el cambio el elemento seleccionado, tanto el elemento como el texto
        # lista.currentItemChanged.connect(self.cambio_elemento)
        # lista.currentTextChanged.connect(self.cambio_texto)
        #
        #
        # # Publicar lista
        # self.setCentralWidget(lista)

    # def cambio_elemento(self, nuevo_elemento):
    #     print(f'Nuevo elemento seleccionado: {nuevo_elemento.text()}')
    #
    # def cambio_texto(self, nuevo_texto):
    #     print(f'Nuevo texto seleccionado: {nuevo_texto}')


        # # Creamos un nuevo componente llamado combobox (drop down list)
        # combobox = QComboBox()
        # # Agregar elementos al combobox
        # combobox.addItem('Uno')
        # combobox.addItems(['Dos', 'Tres'])
        # # Monitoreamos el cambio del elemento seleccionado, tanto el índice como de texto
        # combobox.currentIndexChanged.connect(self.cambio_indice)
        # combobox.currentTextChanged.connect(self.cambio_texto)
        # # Hacemos el editable el combobox
        # combobox.setEditable(True)
        # # Especificamos la politica de inserción
        # # No permite agregar nuevos elementos
        # # combobox.setInsertPolicy(QComboBox.NoInsert)
        # # Agregar al inicio de nuestro combobox
        # # combobox.setInsertPolicy(QComboBox.InsertAtTop)
        # # Modifica el elemento actual
        # # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        # # Insertar al final
        # # combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        # # Insertar antes del elemento actual
        # # combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        # # Insertar después del elemento actual
        # # combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)
        # # Insertar alfabeticamente
        # combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        #
        # # Limitar cuantos elementos agregamos al combobox
        # combobox.setMaxCount(6)
        # # Publicamos nuestro componente de combobox
        # self.setCentralWidget(combobox)

    # def cambio_indice(self, nuevo_indice):
    #     print(f'Nuevo indice seleccionado: {nuevo_indice}')
    #
    # def cambio_texto(self, nuevo_texto):
    #     print(f'Nuevo texto seleccionado: {nuevo_texto}')



        # # Creamos un nuevo componente
        # checkbox = QCheckBox('Este es un checkbox')
        # # Activamos el tercer estado del checkbox
        # # Tenemos 3 estados del checkbox: 0. Apagado - 1. Parcialmente checado - 2. Encendido
        # checkbox.setTristate(True)
        # # Vamos a conectar la señal de cambio de componente
        # checkbox.stateChanged.connect(self.mostrar_estado)

        # # Publicamos el componente de checkbox
        # self.setCentralWidget(checkbox)

    # def mostrar_estado(self, estado):
    #     print(f'Estado del checkbox: {estado}')
    #     # Trabajamos con las constantes
    #     if estado == Qt.Checked:
    #         print('Checkbox encendido')
    #     elif estado == Qt.PartiallyChecked:
    #         print('Checkbox parcialmente checado')
    #     elif estado == Qt.Unchecked:
    #         print('Checkbox apagado')
    #     else:
    #         print('Checkbox con estado invalido')


        # self.setFixedSize(500, 600)
        # # Creamos el componente de tipo etiqueta (Label)
        # etiqueta = QLabel('Hola')
        # etiqueta.setPixmap(QPixmap('layla.jpg'))
        # etiqueta.setScaledContents(True)



        # # Modificamos el valor inicial del texto
        # etiqueta.setText('Saludos')
        # # Modificamos la fuente
        # fuente = etiqueta.font()
        # fuente.setPointSize(25)
        # etiqueta.setFont(fuente)
        # # Modificar la alineación de la etiqueta
        # # etiqueta.setAlignment(Qt.AlignCenter)
        # etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Publicamos este componente
        # self.setCentralWidget(etiqueta)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()

