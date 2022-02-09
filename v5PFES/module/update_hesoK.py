# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_hesoK.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update_hesoK(object):
    def setupUi(self, update_hesoK):
        update_hesoK.setObjectName("update_hesoK")
        update_hesoK.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(update_hesoK)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(update_hesoK)
        self.buttonBox.accepted.connect(update_hesoK.accept)
        self.buttonBox.rejected.connect(update_hesoK.reject)
        QtCore.QMetaObject.connectSlotsByName(update_hesoK)

    def retranslateUi(self, update_hesoK):
        _translate = QtCore.QCoreApplication.translate
        update_hesoK.setWindowTitle(_translate("update_hesoK", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_hesoK = QtWidgets.QDialog()
    ui = Ui_update_hesoK()
    ui.setupUi(update_hesoK)
    update_hesoK.show()
    sys.exit(app.exec_())

