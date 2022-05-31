# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PID.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 337)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Port = QtWidgets.QComboBox(Dialog)
        self.Port.setObjectName("Port")
        self.verticalLayout.addWidget(self.Port)
        self.sendBut = QtWidgets.QPushButton(Dialog)
        self.sendBut.setObjectName("sendBut")
        self.verticalLayout.addWidget(self.sendBut)
        self.resetBut = QtWidgets.QPushButton(Dialog)
        self.resetBut.setObjectName("resetBut")
        self.verticalLayout.addWidget(self.resetBut)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.KdIn = QtWidgets.QLineEdit(Dialog)
        self.KdIn.setObjectName("KdIn")
        self.gridLayout.addWidget(self.KdIn, 2, 3, 1, 1)
        self.KiIn = QtWidgets.QLineEdit(Dialog)
        self.KiIn.setObjectName("KiIn")
        self.gridLayout.addWidget(self.KiIn, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.Ki = QtWidgets.QLabel(Dialog)
        self.Ki.setObjectName("Ki")
        self.gridLayout.addWidget(self.Ki, 1, 1, 1, 1)
        self.Kd = QtWidgets.QLabel(Dialog)
        self.Kd.setObjectName("Kd")
        self.gridLayout.addWidget(self.Kd, 2, 1, 1, 1)
        self.Kp = QtWidgets.QLabel(Dialog)
        self.Kp.setObjectName("Kp")
        self.gridLayout.addWidget(self.Kp, 0, 1, 1, 1)
        self.KpIn = QtWidgets.QLineEdit(Dialog)
        self.KpIn.setObjectName("KpIn")
        self.gridLayout.addWidget(self.KpIn, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sendBut.setText(_translate("Dialog", "Send"))
        self.resetBut.setText(_translate("Dialog", "Reset"))
        self.Ki.setText(_translate("Dialog", "Ki Value"))
        self.Kd.setText(_translate("Dialog", "Kd Value"))
        self.Kp.setText(_translate("Dialog", "Kp Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

