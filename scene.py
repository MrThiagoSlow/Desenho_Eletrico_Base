from PySide6.QtWidgets import QGraphicsScene
#from PySide6.QtCore import *
#from PySide6.QtGui import *
from Objetos import Motor, Tomada, QuadroDiagonal, QuadroPreenchido

class MyScene(QGraphicsScene):
      def __init__(self, parent=None):
         super().__init__(parent)
