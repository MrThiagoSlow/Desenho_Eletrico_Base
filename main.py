import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyWindow = MainWindow()
    MyWindow.show()
    sys.exit(app.exec())

