from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QTabWidget, QRadioButton, QCheckBox, QComboBox, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear un botón
        self.button = QPushButton('Botón', self)
        self.button.move(50, 50)

        # Crear un menú
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('Menú')

        # Crear una pestaña
        self.tab_widget = QTabWidget(self)
        self.tab_widget.move(50, 100)
        self.tab1 = QWidget()
        self.tab_widget.addTab(self.tab1, "Pestaña")

        # Crear un radiobutton
        self.radio_button = QRadioButton("RadioButton", self.tab1)

        # Crear un checkbox
        self.checkbox = QCheckBox("Checkbox", self.tab1)
        self.checkbox.move(0, 30)

        # Crear un combobox (seleccionable)
        self.combobox = QComboBox(self.tab1)
        self.combobox.addItem("Opción 1")
        self.combobox.addItem("Opción 2")
        self.combobox.move(0, 60)

        self.setCentralWidget(self.tab_widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
