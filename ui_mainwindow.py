# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(270, 250)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 211, 181))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.splitter_2 = QSplitter(self.groupBox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName(u"label")
        self.splitter_2.addWidget(self.label)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.splitter_2.addWidget(self.label_2)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.splitter_2.addWidget(self.label_3)
        self.label_4 = QLabel(self.splitter_2)
        self.label_4.setObjectName(u"label_4")
        self.splitter_2.addWidget(self.label_4)
        self.label_5 = QLabel(self.splitter_2)
        self.label_5.setObjectName(u"label_5")
        self.splitter_2.addWidget(self.label_5)
        self.label_6 = QLabel(self.splitter_2)
        self.label_6.setObjectName(u"label_6")
        self.splitter_2.addWidget(self.label_6)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(100, 30, 133, 120))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(True)
        self.lineEdit = QLineEdit(self.splitter)
        self.lineEdit.setObjectName(u"lineEdit")
        self.splitter.addWidget(self.lineEdit)
        self.lineEdit_2 = QLineEdit(self.splitter)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.splitter.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QLineEdit(self.splitter)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.splitter.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QLineEdit(self.splitter)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.splitter.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QLineEdit(self.splitter)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.splitter.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QLineEdit(self.splitter)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.splitter.addWidget(self.lineEdit_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 270, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
    # retranslateUi

