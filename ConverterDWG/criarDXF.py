import ezdxf
from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QPushButton, QMainWindow, QVBoxLayout
from PySide6.QtCore import Qt
from math import cos, sin, radians
# Crie uma aplicação Qt
app = QApplication([])
window = QMainWindow()
layout = QVBoxLayout()

# Crie uma cena e uma visão
scene = QGraphicsScene()
view = QGraphicsView(scene)
botao1 = QPushButton("Salvar desenho")
layout.addWidget(view)
layout.addWidget(botao1)
window.setLayout(layout)
window.show()
# Adicione uma elipse à cena
ellipse_item = QGraphicsEllipseItem(0, 0, 100, 50)
ellipse_item.setPos(50, 50)
scene.addItem(ellipse_item)

# Crie um novo desenho DXF
dwg = ezdxf.new('R2010')

# Adicione uma nova camada ao desenho
dwg.layers.new('ELLIPSES')

# Crie um novo bloco de layout (modelo)
msp = dwg.modelspace()

# Obtenha as propriedades da elipse
ellipse_rect = ellipse_item.rect()
center = ellipse_rect.center()
major_radius = ellipse_rect.width() / 2
minor_radius = ellipse_rect.height() / 2

# Adicione a elipse ao desenho DXF usando linhas de arco
msp.add_lwpolyline(
    points=[
        (center.x() + major_radius * cos(theta), center.y() + minor_radius * sin(theta))
        for theta in range(0, 360, 5)  # Use um intervalo pequeno para obter uma curva suave
    ],
    close=True,
    dxfattribs={'layer': 'ELLIPSES'}
)

# Salve o desenho DXF
dwg.saveas('ellipse2.dxf')


# Exiba a visão
view.show()

# Execute o loop de eventos do aplicativo
app.exec()

