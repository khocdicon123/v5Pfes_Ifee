# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_XuatBieuNhom1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_XuatBieuNhom1(object):
    def setupUi(self, Dialog_XuatBieuNhom1):
        Dialog_XuatBieuNhom1.setObjectName("Dialog_XuatBieuNhom1")
        Dialog_XuatBieuNhom1.resize(561, 135)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_XuatBieuNhom1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog_XuatBieuNhom1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog_XuatBieuNhom1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog_XuatBieuNhom1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.com_tinh = QtWidgets.QComboBox(Dialog_XuatBieuNhom1)
        self.com_tinh.setObjectName("com_tinh")
        self.gridLayout.addWidget(self.com_tinh, 1, 0, 1, 1)
        self.com_huyen = QtWidgets.QComboBox(Dialog_XuatBieuNhom1)
        self.com_huyen.setObjectName("com_huyen")
        self.gridLayout.addWidget(self.com_huyen, 1, 1, 1, 1)
        self.combo_xa = QtWidgets.QComboBox(Dialog_XuatBieuNhom1)
        self.combo_xa.setObjectName("combo_xa")
        self.gridLayout.addWidget(self.combo_xa, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog_XuatBieuNhom1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.output_path = QtWidgets.QLineEdit(Dialog_XuatBieuNhom1)
        self.output_path.setObjectName("output_path")
        self.horizontalLayout.addWidget(self.output_path)
        self.toolButton = QtWidgets.QToolButton(Dialog_XuatBieuNhom1)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_OK = QtWidgets.QPushButton(Dialog_XuatBieuNhom1)
        self.btn_OK.setObjectName("btn_OK")
        self.horizontalLayout_2.addWidget(self.btn_OK)
        self.btn_cancel = QtWidgets.QPushButton(Dialog_XuatBieuNhom1)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 2, 1, 1)

        self.retranslateUi(Dialog_XuatBieuNhom1)
        QtCore.QMetaObject.connectSlotsByName(Dialog_XuatBieuNhom1)

    def retranslateUi(self, Dialog_XuatBieuNhom1):
        _translate = QtCore.QCoreApplication.translate
        Dialog_XuatBieuNhom1.setWindowTitle(_translate("Dialog_XuatBieuNhom1", "v5PFES - Xuất biểu nhóm 1"))
        self.label.setText(_translate("Dialog_XuatBieuNhom1", "Chọn tỉnh"))
        self.label_2.setText(_translate("Dialog_XuatBieuNhom1", "Chọn huyện"))
        self.label_3.setText(_translate("Dialog_XuatBieuNhom1", "Chọn xã"))
        self.label_5.setText(_translate("Dialog_XuatBieuNhom1", "Chọn thư mục lưu kết quả"))
        self.toolButton.setText(_translate("Dialog_XuatBieuNhom1", "..."))
        self.btn_OK.setText(_translate("Dialog_XuatBieuNhom1", "OK"))
        self.btn_cancel.setText(_translate("Dialog_XuatBieuNhom1", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_XuatBieuNhom1 = QtWidgets.QDialog()
    ui = Ui_Dialog_XuatBieuNhom1()
    ui.setupUi(Dialog_XuatBieuNhom1)
    Dialog_XuatBieuNhom1.show()
    sys.exit(app.exec_())

