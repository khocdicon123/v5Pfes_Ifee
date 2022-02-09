# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_vungchitra.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update_vungchitra(object):
    def setupUi(self, update_vungchitra):
        update_vungchitra.setObjectName("update_vungchitra")
        update_vungchitra.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(update_vungchitra)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(update_vungchitra)
        self.buttonBox.accepted.connect(update_vungchitra.accept)
        self.buttonBox.rejected.connect(update_vungchitra.reject)
        QtCore.QMetaObject.connectSlotsByName(update_vungchitra)

    def retranslateUi(self, update_vungchitra):
        _translate = QtCore.QCoreApplication.translate
        update_vungchitra.setWindowTitle(_translate("update_vungchitra", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_vungchitra = QtWidgets.QDialog()
    ui = Ui_update_vungchitra()
    ui.setupUi(update_vungchitra)
    update_vungchitra.show()
    sys.exit(app.exec_())

