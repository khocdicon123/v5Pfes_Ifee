# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_xakk.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update_xakk(object):
    def setupUi(self, update_xakk):
        update_xakk.setObjectName("update_xakk")
        update_xakk.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(update_xakk)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(update_xakk)
        self.buttonBox.accepted.connect(update_xakk.accept)
        self.buttonBox.rejected.connect(update_xakk.reject)
        QtCore.QMetaObject.connectSlotsByName(update_xakk)

    def retranslateUi(self, update_xakk):
        _translate = QtCore.QCoreApplication.translate
        update_xakk.setWindowTitle(_translate("update_xakk", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_xakk = QtWidgets.QDialog()
    ui = Ui_update_xakk()
    ui.setupUi(update_xakk)
    update_xakk.show()
    sys.exit(app.exec_())

