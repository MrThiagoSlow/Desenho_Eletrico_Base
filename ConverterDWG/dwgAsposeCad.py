import aspose.cad as cad

# Carrega o arquivo DXF
cadImage = cad.Image.load("drawer2.dxf")

# Salva o arquivo como DWG
cadImage.save("output.dwg", cad.DwgOptions())
