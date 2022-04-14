# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\2022-Daftar\PyQt\Babel\bin\gui\poswindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1772, 1319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.POSlist = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.POSlist.sizePolicy().hasHeightForWidth())
        self.POSlist.setSizePolicy(sizePolicy)
        self.POSlist.setMinimumSize(QtCore.QSize(300, 0))
        self.POSlist.setObjectName("POSlist")
        self.horizontalLayout.addWidget(self.POSlist)
        self.POSBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.POSBrowser.setObjectName("POSBrowser")
        self.horizontalLayout.addWidget(self.POSBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1772, 52))
        self.menubar.setObjectName("menubar")
        self.menuPart_of_Speech = QtWidgets.QMenu(self.menubar)
        self.menuPart_of_Speech.setObjectName("menuPart_of_Speech")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionModify = QtWidgets.QAction(MainWindow)
        self.actionModify.setObjectName("actionModify")
        self.menuPart_of_Speech.addAction(self.actionAdd)
        self.menuPart_of_Speech.addAction(self.actionRemove)
        self.menuPart_of_Speech.addAction(self.actionModify)
        self.menubar.addAction(self.menuPart_of_Speech.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Part of Speech"))
        self.menuPart_of_Speech.setTitle(_translate("MainWindow", "Edit"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+`"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionRemove.setShortcut(_translate("MainWindow", "Del"))
        self.actionModify.setText(_translate("MainWindow", "Modify"))
        self.actionModify.setShortcut(_translate("MainWindow", "Ctrl+="))

