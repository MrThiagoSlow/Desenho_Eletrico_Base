import ezdxf

dwg = ezdxf.new()
msp = dwg.modelspace()

# Adicione uma linha
msp.add_line(start=(0, 0), end=(100, 0))

# Adicione um círculo
msp.add_circle(center=(50, 50), radius=30)

# Salve o desenho como DXF
dwg.saveas('drawing.dxf')
