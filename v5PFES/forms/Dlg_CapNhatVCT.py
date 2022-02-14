# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_CapNhatVCT.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_CapNhatVCT(object):
    def setupUi(self, Dialog_CapNhatVCT):
        Dialog_CapNhatVCT.setObjectName("Dialog_CapNhatVCT")
        Dialog_CapNhatVCT.resize(481, 240)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog_CapNhatVCT)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(Dialog_CapNhatVCT)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_CapNhatVCT)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog_CapNhatVCT)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog_CapNhatVCT)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog_CapNhatVCT)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog_CapNhatVCT)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.comboBox, 3, 0, 1, 1)
        self.comboBox2 = QtWidgets.QComboBox(Dialog_CapNhatVCT)
        self.comboBox2.setObjectName("comboBox2")
        self.gridLayout_4.addWidget(self.comboBox2, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog_CapNhatVCT)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog_CapNhatVCT)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_CapNhatVCT)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 5, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(Dialog_CapNhatVCT)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 6, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog_CapNhatVCT)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog_CapNhatVCT)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 7, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_CapNhatVCT)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 8, 0, 1, 2)

        self.retranslateUi(Dialog_CapNhatVCT)
        self.buttonBox.accepted.connect(Dialog_CapNhatVCT.accept)
        self.buttonBox.rejected.connect(Dialog_CapNhatVCT.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CapNhatVCT)

    def retranslateUi(self, Dialog_CapNhatVCT):
        _translate = QtCore.QCoreApplication.translate
        Dialog_CapNhatVCT.setWindowTitle(_translate("Dialog_CapNhatVCT", "v5PES - Cập nhật vùng chi trả"))
        self.label.setText(_translate("Dialog_CapNhatVCT", "Chọn lớp bản đồ đầu vào (.shp)"))
        self.pushButton.setText(_translate("Dialog_CapNhatVCT", "..."))
        self.label_2.setText(_translate("Dialog_CapNhatVCT", "Chọn lưu vực "))
        self.checkBox.setText(_translate("Dialog_CapNhatVCT", "Trùng với lưu vực đã cập nhật"))
        self.label_3.setText(_translate("Dialog_CapNhatVCT", "Chọn lớp ranh giới lưu vực (.shp)"))
        self.pushButton_2.setText(_translate("Dialog_CapNhatVCT", "..."))
        self.label_4.setText(_translate("Dialog_CapNhatVCT", "Chọn lớp bản đồ đầu ra  (.shp)"))
        self.pushButton_3.setText(_translate("Dialog_CapNhatVCT", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_CapNhatVCT = QtWidgets.QDialog()
    ui = Ui_Dialog_CapNhatVCT()
    ui.setupUi(Dialog_CapNhatVCT)
    Dialog_CapNhatVCT.show()
    sys.exit(app.exec_())

