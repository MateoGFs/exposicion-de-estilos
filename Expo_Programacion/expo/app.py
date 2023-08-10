from PySide6.QtWidgets import QWidget, QApplication,QPushButton, QStyle, QComboBox, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QIcon, QPixmap, QRadialGradient
import sys
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        
        icono1 = QIcon("img/about.png")
        
        boton = QPushButton(icono1,"hola",self)
        boton2 = QPushButton("Bye",self)
        
        
        
        layout = QVBoxLayout()
        layout.addWidget(boton)
        layout.addWidget(boton2)
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #Agregando temas predefinidos con setStyle
    #app.setStyle("")
    
    gradient = QRadialGradient(50, 50, 50, 50, 50)
    gradient.setColorAt(0, QColor.fromRgbF(0, 1, 0, 1))
    gradient.setColorAt(1, QColor.fromRgbF(0, 0, 0, 0))
    
    palette = QPalette()
    palette.setBrush(QPalette.Window, gradient)
    app.setPalette(palette)
    window = MainWindow()
    window.show()
    app.exec()