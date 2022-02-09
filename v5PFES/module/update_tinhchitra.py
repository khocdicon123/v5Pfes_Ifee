# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_tinhchitra.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update_tinhchitra(object):
    def setupUi(self, update_tinhchitra):
        update_tinhchitra.setObjectName("update_tinhchitra")
        update_tinhchitra.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(update_tinhchitra)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(update_tinhchitra)
        self.buttonBox.accepted.connect(update_tinhchitra.accept)
        self.buttonBox.rejected.connect(update_tinhchitra.reject)
        QtCore.QMetaObject.connectSlotsByName(update_tinhchitra)

    def retranslateUi(self, update_tinhchitra):
        _translate = QtCore.QCoreApplication.translate
        update_tinhchitra.setWindowTitle(_translate("update_tinhchitra", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_tinhchitra = QtWidgets.QDialog()
    ui = Ui_update_tinhchitra()
    ui.setupUi(update_tinhchitra)
    update_tinhchitra.show()
    sys.exit(app.exec_())

