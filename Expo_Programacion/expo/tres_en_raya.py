from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QLabel,
                               QPushButton,
                               QLineEdit,
                               QStackedLayout,
                               QVBoxLayout,
                               QFormLayout,
                               QGridLayout,
                               QSizePolicy,
                               QFrame,)
from PySide6.QtGui import QPixmap, QIcon, QPalette, QColor

from PySide6.QtCore import Qt, QSize 
from functools import partial
import sys
import os
basedir = os.path.dirname(__file__)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        icono=QIcon("img/back_game.png") 
        self.setWindowIcon(icono)
        self.setWindowTitle("App Juego Tres en Raya")
        self.resize(450, 500)
        self.setup_ui()
        #with open("style.css", "r") as file:
            
        
    def setup_ui(self):
        self.stl_main = QStackedLayout()
        
        # capa 0 Login
        self.stl_main.addWidget(self.ui_login())
        
        # capa 1 game
        self.stl_main.addWidget(self.ui_game())
        
        
        # capa 2 about
        self.stl_main.addWidget(self.ui_about())
        self.setLayout(self.stl_main)
        
    def ui_about(self):
        vbx_about = QVBoxLayout()
        btn_volver = QPushButton("volver al juego")
        
        btn_volver.setObjectName("inicio") 
        
        lbl_icono=QLabel()
        lbl_icono.setPixmap(QPixmap(os.path.join(basedir,"img","back_game.png" )).scaled(150,100))
        lbl_icono.setAlignment(Qt.AlignmentFlag.AlignHCenter) 
        btn_home = QPushButton("ir a login")
        desarrollado = QLabel("Desarrollado por:")
        nombres = QLabel("Emerson Steven Imbajoa \nCristian Mateo Rodríguez Solarte")
        
        vbx_about.addWidget(desarrollado)
        
        vbx_about.addWidget(nombres)
        vbx_about.addStretch(12)
        vbx_about.addWidget(lbl_icono)
        vbx_about.addStretch(12)
        #btn_volver.clicked.connect(self.validar_jugadores)
        btn_volver.clicked.connect(lambda: self.stl_main.setCurrentIndex(1))
        btn_home.clicked.connect(lambda: self.stl_main.setCurrentIndex(0))
        vbx_about.addWidget(btn_volver)
        #vbx_about.addWidget(btn_home)
        widget = QWidget()
        widget.setLayout(vbx_about)
        return widget
    def ui_login(self):
        # Layout principal de la sección login
        vbx_login = QVBoxLayout()
        
        # logo        
        lbl_logo = QLabel()
        pixmap = QPixmap(os.path.join(basedir, "img", "tic_tac_toe.png"))
        lbl_logo.setPixmap(pixmap)
        # reducir tamaño del logo al 20%
        ancho_logo, alto_logo = lbl_logo.size().toTuple()
        lbl_logo.setPixmap(pixmap.scaled(ancho_logo * 0.2,
                                         alto_logo * 0.2,
                                         Qt.KeepAspectRatio))
        lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbx_login.addWidget(lbl_logo)
        
        # título
        lbl_titulo = QLabel("TIC TAC TOE", alignment=Qt.AlignmentFlag.AlignCenter)
        
        vbx_login.addWidget(lbl_titulo)
        
        # entradas de los jugadores 
        frm_players = QFormLayout()
        self.playerX = QLineEdit()
        self.playerX.setFixedSize(QSize(400,34))
        self.playerO = QLineEdit()
        self.playerO.setFixedSize(QSize(400,34))
        frm_players.addRow("Jugador X:", self.playerX)
        frm_players.addRow("Jugador O:", self.playerO)
        vbx_login.addLayout(frm_players)
        
        # info estado
        self.lbl_estado = QLabel()
        self.lbl_estado.setObjectName("estado")
        vbx_login.addWidget(self.lbl_estado)
        
        # botón de login
        btn_login = QPushButton("Jugar")
        btn_login.setObjectName("inicio")
        btn_login.clicked.connect(self.validar_jugadores)
        vbx_login.addWidget(btn_login)
        
        widget = QWidget()
        widget.setLayout(vbx_login)
        return widget
        
    def validar_jugadores(self):
        print("entra")
        msj = ""
        if self.playerX.text().strip() == "":
            msj = "El nombre del jugador X es Incorrecto!\n"
            self.lbl_estado.setText(msj)
        if self.playerO.text().strip()== "":
            msj += "El nombre del jugador O es Incorrecto!"
            self.lbl_estado.setText(msj)
        if self.playerO.text().strip() == self.playerX.text().strip():
            msj = "Los nombres deben ser diferentes"
            self.lbl_estado.setText(msj)   
        if self.playerO.text().strip() == "" and self.playerX.text().strip()=="":
            msj = "Debe rellenar los campos"
            self.lbl_estado.setText(msj)        
        if msj == "":
            self.stl_main.setCurrentIndex(1) #La segunda capa del stacked
            self.lbl_titulo.setText(f"TIC TAC TOE\nen turno: {self.playerX.text()}") 
            
            
    # Capa 1 juego        
    def ui_game(self):
        # layout principal de la sección de juego
        self.vbx_game = QVBoxLayout()    
                
          
        self.marca_jugador = "X"
        self.matriz_juego = [[0,0,0],
                             [0,0,0],
                             [0,0,0]]
        # Título
        self.lbl_titulo = QLabel("TIC TAC TOE",
                                 alignment=Qt.AlignmentFlag.AlignCenter)
        self.lbl_titulo.setObjectName("titulo")
        self.vbx_game.addWidget(self.lbl_titulo, 20)
        
        # interfaz del juego
        self.frmGame = QFrame()
        self.grd_game = QGridLayout()
        
        for row in range(3):
            for column in range(3):
                btn_jugar = QPushButton()
                btn_jugar.setObjectName("jugar")
                btn_jugar.clicked.connect(partial(self.clicked_jugar,btn_jugar, row, column))
                btn_jugar.setSizePolicy(QSizePolicy.Expanding,
                                        QSizePolicy.Expanding)
                self.grd_game.addWidget(btn_jugar, row, column)
        self.frmGame.setLayout(self.grd_game)        
        self.vbx_game.addWidget(self.frmGame, 80)
        
        # Botón de about 
        btn_about = QPushButton()
        btn_about.setObjectName("about")
        btn_about.setIcon(QIcon(os.path.join(basedir, "img","about.png")))        
        btn_about.setLayoutDirection(Qt.RightToLeft)
        btn_about.setFixedSize(QSize(40,40))
        btn_about.setIconSize(QSize(30,30))
        btn_about.clicked.connect(lambda: self.stl_main.setCurrentIndex(2))
        self.vbx_game.addWidget(btn_about)
        
        
        widget = QWidget()
        widget.setLayout(self.vbx_game)
        return widget 
        
    def clicked_jugar(self, btn_jugar,x,y):
        print(x,y)
        if btn_jugar.text() not in ["X", "O"]:
            btn_jugar.setText(self.marca_jugador)
            btn_jugar.setEnabled(False)
            self.matriz_juego[x][y] = 1 if self.marca_jugador == "X" else -1
            if not self.hay_ganador():
                bTodoJugado = True
                #Comprobar si hay una celda por jugar
                for row in self.matriz_juego:
                    if 0 in row:
                        bTodoJugado = False
                        break
                if not bTodoJugado:
                    if self.marca_jugador == "O":
                        self.marca_jugador = "X"
                        self.lbl_titulo.setText(f"TIC TAC TOE\nen turno {self.playerX.text()}") 
                    else:
                        self.marca_jugador = "O"
                        self.lbl_titulo.setText(f"TIC TAC TOE\nen turno {self.playerO.text()}")
                else: # todo ya esta jugado, no hay celdas disponibles 
                    self.frmGame.setEnabled(False)
                    self.lbl_titulo.setText("TIC TAC TOE\nGame Over")       
            else:
                #cuando hay un ganador 
                self.frmGame.setEnabled(False) 
                
    def hay_ganador(self):
        # sumatoria de todas las filas
        resRows = [sum(row) for row in self.matriz_juego]  
        # sumatoria de todas las columnas
        resCols = [sum(col) for col in zip(*self.matriz_juego)]
        # sumatoria de la diagonal principal
        sum_first_diagonal = sum(self.matriz_juego[i][i] for i in range(3))
        # sumatoria de la diagonal secundaria
        sum_second_diagonal = sum(self.matriz_juego[i][2-i] for i in range(3))
        resDiags = [sum_first_diagonal, sum_second_diagonal]
        if self.marca_jugador == "X":
            if 3 in resRows or 3 in resCols or 3 in resDiags:
                self.lbl_titulo.setText(f"TIC TAC TOE\nGanador {self.playerX.text()}")
                return True
        else: # marca del jugador "O"
            if -3 in resRows or -3 in resCols or -3 in resDiags:
                self.lbl_titulo.setText(f"TIC TAC TOE\nGanador {self.playerO.text()}")
                
                return True
        return False        
                    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    with open("style.css", "r") as file:
       app.setStyleSheet(file.read())
       
       
    app.setStyle("Fusion")
    dark_fusion = QPalette()
    dark_fusion.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.WindowText, QColor("white"))
    dark_fusion.setColor(QPalette.Base, QColor(35, 35, 35))
    dark_fusion.setColor(QPalette.Text, Qt.white)
    dark_fusion.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ButtonText, Qt.white)
    dark_fusion.setColor(QPalette.Highlight, QColor("green"))
    dark_fusion.setColor(QPalette.HighlightedText, QColor("white"))
    dark_fusion.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.black)
    dark_fusion.setColor(QPalette.Disabled, QPalette.Button, QColor("gray"))
    dark_fusion.setColor(QPalette.Inactive, QPalette.WindowText, Qt.red)
    # activamos la paleta en la aplicación
    app.setPalette(dark_fusion)
    window = MainWindow()
    window.show()
    app.exec()       