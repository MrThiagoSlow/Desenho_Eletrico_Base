# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.tipoQuadro_comboBox = QComboBox(self.centralwidget)
        self.tipoQuadro_comboBox.addItem("")
        self.tipoQuadro_comboBox.addItem("")
        self.tipoQuadro_comboBox.setObjectName(u"tipoQuadro_comboBox")
        self.tipoQuadro_comboBox.setGeometry(QRect(50, 40, 131, 22))
        self.tipoCarga_comboBox = QComboBox(self.centralwidget)
        self.tipoCarga_comboBox.addItem("")
        self.tipoCarga_comboBox.addItem("")
        self.tipoCarga_comboBox.setObjectName(u"tipoCarga_comboBox")
        self.tipoCarga_comboBox.setGeometry(QRect(240, 40, 101, 21))
        self.tipoQuadro = QLabel(self.centralwidget)
        self.tipoQuadro.setObjectName(u"tipoQuadro")
        self.tipoQuadro.setGeometry(QRect(50, 10, 141, 16))
        self.tipoCarga = QLabel(self.centralwidget)
        self.tipoCarga.setObjectName(u"tipoCarga")
        self.tipoCarga.setGeometry(QRect(230, 10, 141, 16))
        self.MyView = QGraphicsView(self.centralwidget)
        self.MyView.setObjectName(u"MyView")
        self.MyView.setGeometry(QRect(10, 100, 771, 451))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(400, 30, 91, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(520, 30, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tipoQuadro_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Quadro Preenchido", None))
        self.tipoQuadro_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Quadro Diagonal", None))

        self.tipoCarga_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Motor", None))
        self.tipoCarga_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tomada", None))

        self.tipoQuadro.setText(QCoreApplication.translate("MainWindow", u"Escolha o tipo de Quadro", None))
        self.tipoCarga.setText(QCoreApplication.translate("MainWindow", u"Escolha o tipo de Carga", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Desenhar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
    # retranslateUi

