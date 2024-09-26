import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QWidget, QRadioButton, QCheckBox, QPushButton, QLabel,
                             QLineEdit, QSpinBox, QDateTimeEdit, QTableWidget, QTableWidgetItem,
                             QTextEdit, QComboBox, QSlider, QProgressBar, QDial)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 Example')
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QGridLayout(central_widget)
        
        # Group 1
        group1_layout = QVBoxLayout()
        self.radio1 = QRadioButton("Radio Button 1")
        self.radio2 = QRadioButton("Radio Button 2")
        self.radio3 = QRadioButton("Radio Button 3")
        self.tristate_checkbox = QCheckBox("Tri-state check box")
        group1_layout.addWidget(self.radio1)
        group1_layout.addWidget(self.radio2)
        group1_layout.addWidget(self.radio3)
        group1_layout.addWidget(self.tristate_checkbox)
        
        # Group 2
        group2_layout = QVBoxLayout()
        self.default_push_button = QPushButton("Default Push Button")
        self.toggle_push_button = QPushButton("Toggle Push Button")
        self.toggle_push_button.setCheckable(True)
        group2_layout.addWidget(self.default_push_button)
        group2_layout.addWidget(self.toggle_push_button)
        
        # Group 3
        group3_layout = QVBoxLayout()
        self.group3_checkbox = QCheckBox("Group 3")
        self.flat_push_button = QPushButton("Flat Push Button")
        self.flat_push_button.setFlat(True)
        self.code_edit = QLineEdit()
        self.number_spinbox = QSpinBox()
        self.date_edit = QDateTimeEdit()
        group3_layout.addWidget(self.group3_checkbox)
        group3_layout.addWidget(self.flat_push_button)
        group3_layout.addWidget(QLabel("Code:"))
        group3_layout.addWidget(self.code_edit)
        group3_layout.addWidget(QLabel("Number:"))
        group3_layout.addWidget(self.number_spinbox)
        group3_layout.addWidget(QLabel("Date:"))
        group3_layout.addWidget(self.date_edit)
        
        # Table and Text Edit
        self.table_widget = QTableWidget(4, 2)
        self.table_widget.setHorizontalHeaderLabels(["1", "2"])
        self.text_edit = QTextEdit()
        
        # Slider and Dial
        self.slider = QSlider()
        self.dial = QDial()
        
        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(24)
        
        # Combo Box
        self.style_combobox = QComboBox()
        self.style_combobox.addItem("--Choose one--")
        
        # Adding to main layout
        main_layout.addLayout(group1_layout, 0, 0)
        main_layout.addLayout(group2_layout, 0, 1)
        main_layout.addLayout(group3_layout, 0, 2)
        main_layout.addWidget(self.table_widget, 1, 0, 1, 2)
        main_layout.addWidget(self.text_edit, 1, 2)
        main_layout.addWidget(self.slider, 2, 0, 1, 2)
        main_layout.addWidget(self.dial, 2, 2)
        main_layout.addWidget(self.progress_bar, 3, 0, 1, 3)
        main_layout.addWidget(QLabel("Style:"), 4, 0)
        main_layout.addWidget(self.style_combobox, 4, 1)
        
        self.show()

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
