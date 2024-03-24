#from ezdxf.math import Vector
from PySide6.QtGui import QColor, QPen, QBrush, QFont
from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtCore import QRectF
from math import cos, sin
import ezdxf


# Crie um novo desenho DXF
dwg = ezdxf.new('R2010')

# Adicione uma nova camada ao desenho
dwg.layers.new('ELLIPSES')

# Crie um novo bloco de layout (modelo)
msp = dwg.modelspace()

class Motor(QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()
        self.setRect(-25,-25,50,50)
        self.penWidth = 1

    def boundingRect(self):
        #return QRectF(-15 - penWidth/2, -15 - penWidth/2, 30+penWidth, 30+penWidth)
        rect = super().boundingRect()
        
        return QRectF(rect.x() - self.penWidth / 2, rect.y() - self.penWidth / 2, rect.width() + self.penWidth, rect.height() + self.penWidth)

    def paint(self,painter,option,widget):
        super().paint(painter, option, widget)  
        pen = QPen(QColor(0,0,0), 1)
        brush = QBrush(QColor(0,255,0))
        painter.setPen(pen)
        painter.setBrush(brush)
        #painter.drawEllipse(-25,-25,50,50)
        #Configurar a fonte
        font = QFont("Arial",12)
        painter.setFont(font)
        painter.setPen(QColor(0, 0, 0))
        painter.drawText(-6,3, "M")
# Crie uma nova instância de Motor
motor = Motor()

# Obtenha as propriedades da elipse
ellipse_rect = motor.rect()
center = ellipse_rect.center()
major_radius = ellipse_rect.width() / 2
minor_radius = ellipse_rect.height() / 2

# Adicione a elipse ao desenho DXF usando linhas de arco
try:
    msp.add_ellipse(
        center=(center.x(), center.y(), 0),
        major_axis=(major_radius, 0, 0),
        ratio=minor_radius/major_radius,
        dxfattribs={'layer': 'MOTORS'}
    )
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    # Se a elipse não puder ser representada como uma elipse DXF, desenhe-a como um polígono
    msp.add_lwpolyline(
        points=[
            (center.x() + major_radius * cos(theta), center.y() + minor_radius * sin(theta))
            for theta in range(0, 360, 5)  # Use um intervalo pequeno para obter uma curva suave
        ],
        close=True,
        dxfattribs={'layer': 'MOTORS'}
    )

# Adicione o texto ao desenho DXF
text = msp.add_text(
    "M",
    dxfattribs={
        'layer': 'MOTORS',
        'height': 10,  # Ajuste a altura do texto conforme necessário
    }
)
text.dxf.insert = (center.x(), center.y(), 0)

# Salve o desenho DXF
dwg.saveas('motor.dxf')
