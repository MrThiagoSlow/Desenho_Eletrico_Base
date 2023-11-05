import PySide6.QtCore
from PySide6.QtWidgets import (QGraphicsView, 
                                QGraphicsItem,
                                QGraphicsScene, 
                                QApplication,
                                QGraphicsItemGroup,
                                QGraphicsLineItem,
                                QGraphicsTextItem,
                                QGraphicsPathItem,
                                QGraphicsRectItem
                                )
from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QFont, QPainterPath
from PySide6.QtCore import QRectF, Qt
import sys

"""class Motor(QGraphicsItem):
    def __init__(self):
        super().__init__()

    def boundingRect(self):
        penWidth = 1
        return QRectF(-10 - penWidth / 2, -10 - penWidth / 2, 20+penWidth, 20+penWidth)
    
    def paint(self,painter,option, widget):
        painter.drawEllipse(-30,-30,50,50)
"""

class Motor(QGraphicsItem):
    def __init__(self):
        super().__init__()

    def boundingRect(self):
        penWidth = 1
        return QRectF(-15 - penWidth/2, -15 - penWidth/2, 30+penWidth, 30+penWidth)

    def paint(self,painter,option,widget):
        pen = QPen(QColor(0,0,0), 1)
        brush = QBrush(QColor(0,255,0))
        painter.setPen(pen)
        """path = QPainterPath()
        path.moveTo(0,0)
        path.arcTo(0, 0, 30, 30, 0, 360)
        arch_item = QGraphicsPathItem(path)
        arch_item.setPen(pen)
        """
        painter.drawEllipse(-25,-25,50,50)
        #Configurar a fonte
        font = QFont("Arial",12)
        painter.setFont(font)
        painter.setPen(QColor(0, 0, 0))
        painter.drawText(-6,3,"M")


class Tomada(QGraphicsItem):
    def __init__(self):
        super().__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

    def boundingRect(self):
        penWidth =  penWidth = 1
        return QRectF(-15 - penWidth/2, -15 - penWidth/2, 30+penWidth, 30+penWidth)
    
    def paint(self,painter,option,widget):
        pen = QPen(QColor(0,0,0), 1)
        painter.setPen(pen)
        painter.drawLine(-15,-15,15,-15)
        painter.drawLine(15,-15,0,15)
        painter.drawLine(0,15,-15,-15)
        font = QFont("Arial",10)
        painter.setFont(font)
        painter.drawText(-3,0,"T")


class QuadroDiagonal(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.setRect(-40,-20,80,40)
    def boundingRect(self):
        rect = super().boundingRect()
        penWidth = 1
        return QRectF(rect.x() - penWidth / 2, rect.y() - penWidth / 2, rect.width() + penWidth, rect.height() + penWidth)

    def paint(self,painter,option,widget):
        super().paint(painter, option, widget)  
        pen = QPen(QColor(0, 0, 0), 1)
        painter.setPen(pen)
        painter.drawLine(-40, -20, 40, 20)
    

class QuadroPreenchido(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.setRect(-40,-20,80,40)
    def boundingRect(self):
        rect = super().boundingRect()
        penWidth = 1
        return QRectF(rect.x() - penWidth / 2, rect.y() - penWidth / 2, rect.width() + penWidth, rect.height() + penWidth)

    def paint(self,painter,option,widget):
        super().paint(painter, option, widget)  
        brush = QBrush(QColor(0,0,0))
        painter.setBrush(brush)
        painter.drawRect(self.rect())


"""
app = QApplication(sys.argv)

scene =  QGraphicsScene()
Motor1 = Motor()
Tomada1 = Tomada()
QD1 = QuadroDiagonal()
QD2 = QuadroPreenchido()

Tomada1.setPos(-30,0)
Motor1.setPos(50,0)
QD1.setPos(0,-60)
QD1.setFlag(QGraphicsRectItem.ItemIsMovable, True)
QD1.setFlag(QGraphicsRectItem.ItemIsSelectable, True)
scene.addItem(Motor1)
scene.addItem(Tomada1)
scene.addItem(QD1)
scene.addItem(QD2)
view = QGraphicsView()
view.setScene(scene)
view.setGeometry(0,0,500,500)
view.show()

app.exec()"""