# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\2022-Daftar\PyQt\Babel\bin\gui\worddialog.ui'
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
        self.lineEditCon = QtWidgets.QLineEdit(Dialog)
        self.lineEditCon.setObjectName("lineEditCon")
        self.horizontalLayout.addWidget(self.lineEditCon)
        self.lineEditConDisplay = QtWidgets.QLineEdit(Dialog)
        self.lineEditConDisplay.setReadOnly(True)
        self.lineEditConDisplay.setObjectName("lineEditConDisplay")
        self.horizontalLayout.addWidget(self.lineEditConDisplay)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditNat = QtWidgets.QLineEdit(Dialog)
        self.lineEditNat.setObjectName("lineEditNat")
        self.horizontalLayout_2.addWidget(self.lineEditNat)
        self.lineEditNatDisplay = QtWidgets.QLineEdit(Dialog)
        self.lineEditNatDisplay.setReadOnly(True)
        self.lineEditNatDisplay.setObjectName("lineEditNatDisplay")
        self.horizontalLayout_2.addWidget(self.lineEditNatDisplay)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditPOS = QtWidgets.QLineEdit(Dialog)
        self.lineEditPOS.setObjectName("lineEditPOS")
        self.horizontalLayout_4.addWidget(self.lineEditPOS)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditPron = QtWidgets.QLineEdit(Dialog)
        self.lineEditPron.setObjectName("lineEditPron")
        self.horizontalLayout_3.addWidget(self.lineEditPron)
        self.lineEditPronDisplay = QtWidgets.QLineEdit(Dialog)
        self.lineEditPronDisplay.setReadOnly(True)
        self.lineEditPronDisplay.setObjectName("lineEditPronDisplay")
        self.horizontalLayout_3.addWidget(self.lineEditPronDisplay)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
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
        self.lineEditCon.setPlaceholderText(_translate("Dialog", "Conlang word"))
        self.lineEditNat.setPlaceholderText(_translate("Dialog", "Natlang word"))
        self.lineEditPOS.setPlaceholderText(_translate("Dialog", "Part of Speech"))
        self.lineEditPron.setPlaceholderText(_translate("Dialog", "Pronunciation"))
        self.textEditInfo.setPlaceholderText(_translate("Dialog", "Definition"))

