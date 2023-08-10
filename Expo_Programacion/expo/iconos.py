from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLineEdit, QSpinBox, QPushButton, QStyle)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QIcon, QPixmap
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        
        #poner icono con QIcon
        icono2 = QIcon("img/tic_tac_toe.png")
        
        
        #iconos predeterminados
        icono = self.style().standardIcon(QStyle.SP_DirIcon)
        
        #cambiar icono de la ventana principar
        self.setWindowIcon(icono)
        
        #cambiando el icono cuando este en estado activo
        pix = QPixmap("img/about.png")
        icono2.addPixmap(pix,QIcon.Active)
        
        # lo podemos asignar a un botón
        boton1 = QPushButton(icono, "Botón \nguardar")
        boton1.setFixedHeight(50)
        boton1.setIconSize(QSize(40,40))
        
        
        
        formulario = QFormLayout()
        line = QLineEdit("Hector")
        line.setEnabled(False)
        formulario.addRow("Nombre", line)
        formulario.addRow("Email", QLineEdit(text="hola@ejemplo.com"))
        formulario.addRow("Edad", QSpinBox(value=32))
        formulario.addRow(boton1)
        boton = QPushButton("Enviar")
        #boton.setEnabled(False)
        boton.setIcon(icono2)
        #boton.setEnabled(False)
        formulario.addRow(boton)

        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    #with open("style.css", "r") as file:
    #   app.setStyleSheet(file.read())
    
    #dark fusion https://gist.github.com/lschmierer/443b8e21ad93e2a2d7eb
   
    dark_fusion = QPalette()
    
    dark_fusion.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.WindowText, Qt.white)
    dark_fusion.setColor(QPalette.Base, QColor("lime"))
    dark_fusion.setColor(QPalette.AlternateBase, QColor("lime"))
    dark_fusion.setColor(QPalette.ToolTipBase, QColor("lime"))
    dark_fusion.setColor(QPalette.ToolTipText, Qt.white)
    dark_fusion.setColor(QPalette.Text, Qt.white)
    dark_fusion.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ButtonText, Qt.white)
    dark_fusion.setColor(QPalette.BrightText, Qt.red)
    #dark_fusion.setColor(QPalette.Light, Qt.red)
    #dark_fusion.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_fusion.setColor(QPalette.Highlight, QColor("orange"))
    dark_fusion.setColor(QPalette.HighlightedText, QColor("blue"))
    #dark_fusion.setColor(QPalette.Normal, QPalette.Button, QColor("pink"))
    
    
    dark_fusion.setColor(QPalette.Inactive, QPalette.ButtonText, Qt.red)
    palette = QPalette()
    
    palette.setColor(QPalette.Inactive, QPalette.WindowText, Qt.red)
    
    dark_fusion.setColor(QPalette.Disabled, QPalette.Text, Qt.blue)
    dark_fusion.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.red)
    dark_fusion.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
    # activamos la paleta en la aplicación
    app.setPalette(dark_fusion)

    window = MainWindow()
    window.show()
    app.exec()
