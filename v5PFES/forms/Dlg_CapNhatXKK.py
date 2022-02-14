# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_CapNhatXKK.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_CapNhatXKK(object):
    def setupUi(self, Dialog_CapNhatXKK):
        Dialog_CapNhatXKK.setObjectName("Dialog_CapNhatXKK")
        Dialog_CapNhatXKK.resize(394, 417)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_CapNhatXKK)
        self.buttonBox.setGeometry(QtCore.QRect(40, 380, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_CapNhatXKK)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog_CapNhatXKK)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 361, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(Dialog_CapNhatXKK)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 361, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.inPath = QtWidgets.QLineEdit(self.layoutWidget)
        self.inPath.setObjectName("inPath")
        self.gridLayout.addWidget(self.inPath, 0, 0, 1, 1)
        self.inBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.inBtn.setObjectName("inBtn")
        self.gridLayout.addWidget(self.inBtn, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog_CapNhatXKK)
        self.checkBox.setGeometry(QtCore.QRect(20, 60, 161, 18))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Dialog_CapNhatXKK)
        self.buttonBox.accepted.connect(Dialog_CapNhatXKK.accept)
        self.buttonBox.rejected.connect(Dialog_CapNhatXKK.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CapNhatXKK)

    def retranslateUi(self, Dialog_CapNhatXKK):
        _translate = QtCore.QCoreApplication.translate
        Dialog_CapNhatXKK.setWindowTitle(_translate("Dialog_CapNhatXKK", "v5PFES - Cập nhật xã khó khăn"))
        self.label.setText(_translate("Dialog_CapNhatXKK", "Chọn lớp bản đồ đầu vào (.shp)"))
        self.inBtn.setText(_translate("Dialog_CapNhatXKK", "..."))
        self.checkBox.setText(_translate("Dialog_CapNhatXKK", "Điều chỉnh khu vực khó khăn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_CapNhatXKK = QtWidgets.QDialog()
    ui = Ui_Dialog_CapNhatXKK()
    ui.setupUi(Dialog_CapNhatXKK)
    Dialog_CapNhatXKK.show()
    sys.exit(app.exec_())

