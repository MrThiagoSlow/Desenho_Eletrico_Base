from PySide6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QRect, QRectF

from ui_mainwindow import Ui_MainWindow
from scene import MyScene
from Objetos import Motor, Tomada, QuadroDiagonal, QuadroPreenchido

class GraphicsView(QGraphicsView):
    def __init__(self, scene):
        super(GraphicsView, self).__init__(scene)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.zoom_factor = 1.25

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scale(self.zoom_factor, self.zoom_factor)
        else:
            self.scale(1 / self.zoom_factor, 1 / self.zoom_factor)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.MainScene = MyScene()
        self.layout = QVBoxLayout()
        self.new_view = GraphicsView(self.ui.centralwidget)
        #self.new_view.setObjectName(u"MyView")
        self.new_view.setGeometry(QRect(10, 100, 771, 451))
        self.new_view.setScene(self.MainScene)
        self.new_view.setSceneRect(QRectF(-200, 0, 1000, 1000))
        self.ui.MyView = self.new_view
        
        self.ui.pushButton.clicked.connect(self.desenhar)
        self.ui.pushButton_2.clicked.connect(self.limpa)

    def desenhar(self):
        print(self.ui.tipoCarga_comboBox.currentText(), self.ui.tipoQuadro_comboBox.currentText())
        self.MainScene.clear()
        if self.ui.tipoCarga_comboBox.currentText() == "Motor" and self.ui.tipoQuadro_comboBox.currentText() == "Quadro Preenchido":
            M1 = Motor()
            M1.setPos(0,200)
            QP = QuadroPreenchido()
            QP.setPos(0,-100)
            self.MainScene.addItem(M1)
            self.MainScene.addLine(0,-80,0,200-25)
            self.MainScene.addItem(QP)

        elif self.ui.tipoCarga_comboBox.currentText() == "Motor" and self.ui.tipoQuadro_comboBox.currentText() == "Quadro Diagonal":
            M1 = Motor()
            M1.setPos(0,200)
            QD = QuadroDiagonal()
            QD.setPos(0,-100)
            self.MainScene.addItem(M1)
            self.MainScene.addLine(0,-80,0,200-25)
            self.MainScene.addItem(QD)

        elif self.ui.tipoCarga_comboBox.currentText() == "Tomada" and self.ui.tipoQuadro_comboBox.currentText() == "Quadro Diagonal":
            T1 = Tomada()
            T1.setPos(0,200)
            QD = QuadroDiagonal()
            QD.setPos(0,-100)
            self.MainScene.addItem(T1)
            self.MainScene.addLine(0,-80,0,200-15)
            self.MainScene.addItem(QD)

        elif self.ui.tipoCarga_comboBox.currentText() == "Tomada" and self.ui.tipoQuadro_comboBox.currentText() == "Quadro Preenchido":
            T1 = Tomada()
            T1.setPos(0,200)
            QP = QuadroPreenchido()
            QP.setPos(0,-100)
            self.MainScene.addItem(T1)
            self.MainScene.addLine(0,-80,0,200-15)
            self.MainScene.addItem(QP)
            
    def limpa(self):
        self.MainScene.clear()
    