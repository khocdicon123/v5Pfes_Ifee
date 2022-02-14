# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_CapNhatDT.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_CapNhatDT(object):
    def setupUi(self, Dialog_CapNhatDT):
        Dialog_CapNhatDT.setObjectName("Dialog_CapNhatDT")
        Dialog_CapNhatDT.resize(460, 164)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog_CapNhatDT)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog_CapNhatDT)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog_CapNhatDT)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_CapNhatDT)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog_CapNhatDT)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.inPath = QtWidgets.QLineEdit(Dialog_CapNhatDT)
        self.inPath.setObjectName("inPath")
        self.gridLayout.addWidget(self.inPath, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog_CapNhatDT)
        self.pushButton.setMaximumSize(QtCore.QSize(10777205, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog_CapNhatDT)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_CapNhatDT)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.retranslateUi(Dialog_CapNhatDT)
        self.buttonBox.accepted.connect(Dialog_CapNhatDT.accept)
        self.buttonBox.rejected.connect(Dialog_CapNhatDT.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CapNhatDT)

    def retranslateUi(self, Dialog_CapNhatDT):
        _translate = QtCore.QCoreApplication.translate
        Dialog_CapNhatDT.setWindowTitle(_translate("Dialog_CapNhatDT", "v5PES - Cập nhật diện tích chi trả"))
        self.label_2.setText(_translate("Dialog_CapNhatDT", "Chọn lớp bản đồ đầu ra (.shp)"))
        self.checkBox.setText(_translate("Dialog_CapNhatDT", "Bảo toàn diện tích (Bỏ chọn để tính lại diện tích)"))
        self.label.setText(_translate("Dialog_CapNhatDT", "Chọn lớp bản đồ đầu vào (.shp)"))
        self.pushButton.setText(_translate("Dialog_CapNhatDT", "..."))
        self.pushButton_2.setText(_translate("Dialog_CapNhatDT", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_CapNhatDT = QtWidgets.QDialog()
    ui = Ui_Dialog_CapNhatDT()
    ui.setupUi(Dialog_CapNhatDT)
    Dialog_CapNhatDT.show()
    sys.exit(app.exec_())

