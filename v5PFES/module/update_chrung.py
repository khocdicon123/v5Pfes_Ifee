# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_chrung.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update_chrung(object):
    def setupUi(self, update_chrung):
        update_chrung.setObjectName("update_chrung")
        update_chrung.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(update_chrung)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(update_chrung)
        self.buttonBox.accepted.connect(update_chrung.accept)
        self.buttonBox.rejected.connect(update_chrung.reject)
        QtCore.QMetaObject.connectSlotsByName(update_chrung)

    def retranslateUi(self, update_chrung):
        _translate = QtCore.QCoreApplication.translate
        update_chrung.setWindowTitle(_translate("update_chrung", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_chrung = QtWidgets.QDialog()
    ui = Ui_update_chrung()
    ui.setupUi(update_chrung)
    update_chrung.show()
    sys.exit(app.exec_())

