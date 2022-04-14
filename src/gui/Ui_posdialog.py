# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\2022-Daftar\PyQt\Babel\bin\gui\posdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1138, 610)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditPOS = QtWidgets.QLineEdit(Dialog)
        self.lineEditPOS.setObjectName("lineEditPOS")
        self.horizontalLayout.addWidget(self.lineEditPOS)
        self.lineEditPOSDisplay = QtWidgets.QLineEdit(Dialog)
        self.lineEditPOSDisplay.setReadOnly(True)
        self.lineEditPOSDisplay.setObjectName("lineEditPOSDisplay")
        self.horizontalLayout.addWidget(self.lineEditPOSDisplay)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditAbbr = QtWidgets.QLineEdit(Dialog)
        self.lineEditAbbr.setObjectName("lineEditAbbr")
        self.horizontalLayout_4.addWidget(self.lineEditAbbr)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.textEditInfo = QtWidgets.QTextEdit(Dialog)
        self.textEditInfo.setObjectName("textEditInfo")
        self.verticalLayout_2.addWidget(self.textEditInfo)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEditPOS.setPlaceholderText(_translate("Dialog", "Part of Speech"))
        self.lineEditAbbr.setPlaceholderText(_translate("Dialog", "Abbreviation"))
        self.textEditInfo.setPlaceholderText(_translate("Dialog", "Definition"))

