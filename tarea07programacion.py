import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QWidget, QRadioButton, QCheckBox, QPushButton, QLabel,
                             QLineEdit, QSpinBox, QDateTimeEdit, QTableWidget, QTableWidgetItem,
                             QTextEdit, QComboBox, QSlider, QProgressBar, QDial)
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    """
    Clase que representa la ventana principal de la aplicación PyQt6 con apariencia personalizada.

    Hereda de la clase QMainWindow.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ejemplo de PyQt6 con Apariencia Personalizada')

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QGridLayout(central_widget)

        # Grupo 1
        group1_layout = QVBoxLayout()
        self.radio1 = QRadioButton("Botón de Radio 1")
        self.radio2 = QRadioButton("Botón de Radio 2")
        self.radio3 = QRadioButton("Botón de Radio 3")
        self.tristate_checkbox = QCheckBox("Casilla de Verificación de Tres Estados")
        group1_layout.addWidget(self.radio1)
        group1_layout.addWidget(self.radio2)
        group1_layout.addWidget(self.radio3)
        group1_layout.addWidget(self.tristate_checkbox)

        # Grupo 2
        group2_layout = QVBoxLayout()
        self.default_push_button = QPushButton("Botón de Empuje Predeterminado")
        self.toggle_push_button = QPushButton("Botón de Empuje Conmutado")
        self.toggle_push_button.setCheckable(True)
        group2_layout.addWidget(self.default_push_button)
        group2_layout.addWidget(self.toggle_push_button)

        # Grupo 3
        group3_layout = QVBoxLayout()
        self.group3_checkbox = QCheckBox("Grupo 3")
        self.flat_push_button = QPushButton("Botón de Empuje Plano")
        self.flat_push_button.setFlat(True)
        self.code_edit = QLineEdit()
        self.number_spinbox = QSpinBox()
        self.date_edit = QDateTimeEdit()
        group3_layout.addWidget(self.group3_checkbox)
        group3_layout.addWidget(self.flat_push_button)
        group3_layout.addWidget(QLabel("Código:"))
        group3_layout.addWidget(self.code_edit)
        group3_layout.addWidget(QLabel("Número:"))
        group3_layout.addWidget(self.number_spinbox)
        group3_layout.addWidget(QLabel("Fecha:"))
        group3_layout.addWidget(self.date_edit)

        # Tabla y Editor de Texto
        self.table_widget = QTableWidget(4, 2)
        self.table_widget.setHorizontalHeaderLabels(["1", "2"])
        self.text_edit = QTextEdit()

        # Slider y Dial
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.dial = QDial()

        # Barra de Progreso
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(24)

        # Cuadro de Selección
        self.style_combobox = QComboBox()
        self.style_combobox.addItem("--Elija uno--")

        # Añadiendo al layout principal
        main_layout.addLayout(group1_layout, 0, 0)
        main_layout.addLayout(group2_layout, 0, 1)
        main_layout.addLayout(group3_layout, 0, 2)
        main_layout.addWidget(self.table_widget, 1, 0, 1, 2)
        main_layout.addWidget(self.text_edit, 1, 2)
        main_layout.addWidget(self.slider, 2, 0, 1, 2)
        main_layout.addWidget(self.dial, 2, 2)
        main_layout.addWidget(self.progress_bar, 3, 0, 1, 3)
        main_layout.addWidget(QLabel("Estilo:"), 4, 0)
        main_layout.addWidget(self.style_combobox, 4, 1)

        self.apply_styles()

        self.show()

    def apply_styles(self):
        # Aplicar estilos personalizados a los widgets
        self.setStyleSheet("""
            QRadioButton {
                color: #2E8B57;  /* Color SeaGreen */
            }
            QCheckBox {
                color: #8A2BE2;  /* Color BlueViolet */
            }
            QPushButton {
                background-color: #4682B4;  /* Color SteelBlue */
                color: white;
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:checked {
                background-color: #5F9EA0;  /* Color CadetBlue */
            }
            QLineEdit {
                background-color: #FFFACD;  /* Color LemonChiffon */
                border: 1px solid #BDB76B;  /* Color DarkKhaki */
            }
            QSpinBox {
                background-color: #FFFACD;  /* Color LemonChiffon */
                border: 1px solid #BDB76B;  /* Color DarkKhaki */
            }
            QDateTimeEdit {
                background-color: #FFFACD;  /* Color LemonChiffon */
                border: 1px solid #BDB76B;  /* Color DarkKhaki */
            }
            QTableWidget {
                background-color: #F5F5F5;  /* Color WhiteSmoke */
                gridline-color: #A9A9A9;  /* Color DarkGray */
            }
            QTextEdit {
                background-color: #F0FFF0;  /* Color Honeydew */
                border: 1px solid #98FB98;  /* Color PaleGreen */
            }
            QSlider::groove:horizontal {
                background: #B0C4DE;  /* Color LightSteelBlue */
                height: 10px;
            }
            QSlider::handle:horizontal {
                background: #4682B4;  /* Color SteelBlue */
                border: 1px solid #1C1C1C;  /* Color VeryDarkGray */
                width: 20px;
                margin: -5px 0;  /* Superposición del control */
            }
            QDial {
                background-color: #FFF8DC;  /* Color Cornsilk */
            }
            QProgressBar {
                background-color: #D3D3D3;  /* Color LightGray */
                border: 1px solid #A9A9A9;  /* Color DarkGray */
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #32CD32;  /* Color LimeGreen */
                width: 10px;
                margin: 1px;
            }
            QComboBox {
                background-color: #F5DEB3;  /* Color Wheat */
                border: 1px solid #CD853F;  /* Color Peru */
                padding: 3px;
            }
        """)

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
