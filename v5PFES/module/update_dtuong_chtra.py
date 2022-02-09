# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_dtuong_chtra.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update_dtuong_chtra(object):
    def setupUi(self, update_dtuong_chtra):
        update_dtuong_chtra.setObjectName("update_dtuong_chtra")
        update_dtuong_chtra.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(update_dtuong_chtra)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(update_dtuong_chtra)
        self.buttonBox.accepted.connect(update_dtuong_chtra.accept)
        self.buttonBox.rejected.connect(update_dtuong_chtra.reject)
        QtCore.QMetaObject.connectSlotsByName(update_dtuong_chtra)

    def retranslateUi(self, update_dtuong_chtra):
        _translate = QtCore.QCoreApplication.translate
        update_dtuong_chtra.setWindowTitle(_translate("update_dtuong_chtra", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_dtuong_chtra = QtWidgets.QDialog()
    ui = Ui_update_dtuong_chtra()
    ui.setupUi(update_dtuong_chtra)
    update_dtuong_chtra.show()
    sys.exit(app.exec_())

