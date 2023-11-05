from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from scene import MyScene
from Objetos import Motor, Tomada, QuadroDiagonal, QuadroPreenchido
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # Correção: Use super() com a classe atual.
        self.setupUi(self)
        self.MainScene = MyScene()
        self.pushButton.clicked.connect(self.desenhar)
        self.pushButton_2.clicked.connect(self.limpa)

        self.MyView.setScene(self.MainScene)

    def desenhar(self):
        if self.tipoCarga_comboBox.currentText() == "Motor" and self.tipoQuadro_comboBox.currentText() == "Quadro Preenchido":
            M1 = Motor()
            M1.setPos(0,200)
            QP = QuadroPreenchido()
            QP.setPos(0,-100)
            self.MainScene.addItem(M1)
            self.MainScene.addLine(0,-80,0,200-25)
            self.MainScene.addItem(QP)

        elif self.tipoCarga_comboBox.currentText() == "Motor" and self.tipoQuadro_comboBox.currentText() == "Quadro Diagonal":
            M1 = Motor()
            M1.setPos(0,200)
            QD = QuadroDiagonal()
            QD.setPos(0,-100)
            self.MainScene.addItem(M1)
            self.MainScene.addLine(0,-80,0,200-25)
            self.MainScene.addItem(QD)

        elif self.tipoCarga_comboBox.currentText() == "Tomada" and self.tipoQuadro_comboBox.currentText() == "Quadro Diagonal":
            T1 = Tomada()
            T1.setPos(0,200)
            QD = QuadroDiagonal()
            QD.setPos(0,-100)
            self.MainScene.addItem(T1)
            self.MainScene.addLine(0,-80,0,200-15)
            self.MainScene.addItem(QD)

        elif self.tipoCarga_comboBox.currentText() == "Tomada" and self.tipoQuadro_comboBox.currentText() == "Quadro Preenchido":
            T1 = Tomada()
            T1.setPos(0,200)
            QP = QuadroPreenchido()
            QP.setPos(0,-100)
            self.MainScene.addItem(T1)
            self.MainScene.addLine(0,-80,0,200-15)
            self.MainScene.addItem(QP)
            
    def limpa(self):
        self.MainScene.clear()
    