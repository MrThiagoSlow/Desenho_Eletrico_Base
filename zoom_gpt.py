import sys
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QGraphicsView

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

def main():
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    view = GraphicsView(scene)

    button = QPushButton("Add Item")
    button.clicked.connect(lambda: scene.addEllipse(0, 0, 100, 100))

    layout = QVBoxLayout()
    layout.addWidget(view)
    layout.addWidget(button)

    widget = QWidget()
    widget.setLayout(layout)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
