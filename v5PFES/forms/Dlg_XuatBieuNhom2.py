# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_Xuatbieunhom2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_XuatBieuNhom2(object):
    def setupUi(self, Dialog_XuatBieuNhom2):
        Dialog_XuatBieuNhom2.setObjectName("Dialog_XuatBieuNhom2")
        Dialog_XuatBieuNhom2.resize(531, 300)
        self.com_tinh = QtWidgets.QComboBox(Dialog_XuatBieuNhom2)
        self.com_tinh.setGeometry(QtCore.QRect(20, 50, 161, 22))
        self.com_tinh.setObjectName("com_tinh")
        self.com_churung = QtWidgets.QComboBox(Dialog_XuatBieuNhom2)
        self.com_churung.setGeometry(QtCore.QRect(210, 50, 301, 22))
        self.com_churung.setObjectName("com_churung")
        self.btn_ok = QtWidgets.QPushButton(Dialog_XuatBieuNhom2)
        self.btn_ok.setGeometry(QtCore.QRect(350, 230, 75, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(Dialog_XuatBieuNhom2)
        self.btn_cancel.setGeometry(QtCore.QRect(440, 230, 75, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        self.lbl_tinh = QtWidgets.QLabel(Dialog_XuatBieuNhom2)
        self.lbl_tinh.setGeometry(QtCore.QRect(22, 31, 71, 16))
        self.lbl_tinh.setObjectName("lbl_tinh")
        self.lbl_churung = QtWidgets.QLabel(Dialog_XuatBieuNhom2)
        self.lbl_churung.setGeometry(QtCore.QRect(213, 30, 71, 16))
        self.lbl_churung.setObjectName("lbl_churung")
        self.lbl_ketqua = QtWidgets.QLabel(Dialog_XuatBieuNhom2)
        self.lbl_ketqua.setGeometry(QtCore.QRect(20, 110, 161, 16))
        self.lbl_ketqua.setObjectName("lbl_ketqua")
        self.layoutWidget = QtWidgets.QWidget(Dialog_XuatBieuNhom2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 491, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.out_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.out_path.setObjectName("out_path")
        self.horizontalLayout.addWidget(self.out_path)
        self.btn_path = QtWidgets.QToolButton(self.layoutWidget)
        self.btn_path.setObjectName("btn_path")
        self.horizontalLayout.addWidget(self.btn_path)

        self.retranslateUi(Dialog_XuatBieuNhom2)
        QtCore.QMetaObject.connectSlotsByName(Dialog_XuatBieuNhom2)

    def retranslateUi(self, Dialog_XuatBieuNhom2):
        _translate = QtCore.QCoreApplication.translate
        Dialog_XuatBieuNhom2.setWindowTitle(_translate("Dialog_XuatBieuNhom2", "v5PFES - Xuất biểu chủ rừng nhóm 2"))
        self.btn_ok.setText(_translate("Dialog_XuatBieuNhom2", "OK"))
        self.btn_cancel.setText(_translate("Dialog_XuatBieuNhom2", "Cancel"))
        self.lbl_tinh.setText(_translate("Dialog_XuatBieuNhom2", "Tỉnh"))
        self.lbl_churung.setText(_translate("Dialog_XuatBieuNhom2", "Chủ rừng"))
        self.lbl_ketqua.setText(_translate("Dialog_XuatBieuNhom2", "Chọn thư mục lưu kết quả"))
        self.btn_path.setText(_translate("Dialog_XuatBieuNhom2", "..."))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_XuatBieuNhom2 = QtWidgets.QDialog()
    ui = Ui_Dialog_XuatBieuNhom2()
    ui.setupUi(Dialog_XuatBieuNhom2)
    Dialog_XuatBieuNhom2.show()
    sys.exit(app.exec_())

