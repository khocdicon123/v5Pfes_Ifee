# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_CapNhatHSK.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_CapNhatHSK(object):
    def setupUi(self, Dialog_CapNhatHSK):
        Dialog_CapNhatHSK.setObjectName("Dialog_CapNhatHSK")
        Dialog_CapNhatHSK.resize(354, 353)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_CapNhatHSK)
        self.buttonBox.setGeometry(QtCore.QRect(0, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_CapNhatHSK)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog_CapNhatHSK)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 331, 80))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 139, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.noK_rBtn = QtWidgets.QRadioButton(self.layoutWidget)
        self.noK_rBtn.setObjectName("noK_rBtn")
        self.verticalLayout_2.addWidget(self.noK_rBtn)
        self.K_rBtn = QtWidgets.QRadioButton(self.layoutWidget)
        self.K_rBtn.setObjectName("K_rBtn")
        self.verticalLayout_2.addWidget(self.K_rBtn)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_CapNhatHSK)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 331, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 167, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.k1_cBx = QtWidgets.QCheckBox(self.layoutWidget1)
        self.k1_cBx.setObjectName("k1_cBx")
        self.verticalLayout.addWidget(self.k1_cBx)
        self.k2_cBx = QtWidgets.QCheckBox(self.layoutWidget1)
        self.k2_cBx.setObjectName("k2_cBx")
        self.verticalLayout.addWidget(self.k2_cBx)
        self.k3_cBx = QtWidgets.QCheckBox(self.layoutWidget1)
        self.k3_cBx.setObjectName("k3_cBx")
        self.verticalLayout.addWidget(self.k3_cBx)
        self.k4_cBx = QtWidgets.QCheckBox(self.layoutWidget1)
        self.k4_cBx.setObjectName("k4_cBx")
        self.verticalLayout.addWidget(self.k4_cBx)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog_CapNhatHSK)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 331, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.inPath = QtWidgets.QLineEdit(self.layoutWidget2)
        self.inPath.setObjectName("inPath")
        self.gridLayout.addWidget(self.inPath, 0, 0, 1, 1)
        self.inBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.inBtn.setObjectName("inBtn")
        self.gridLayout.addWidget(self.inBtn, 0, 1, 1, 1)

        self.retranslateUi(Dialog_CapNhatHSK)
        self.buttonBox.accepted.connect(Dialog_CapNhatHSK.accept)
        self.buttonBox.rejected.connect(Dialog_CapNhatHSK.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CapNhatHSK)

    def retranslateUi(self, Dialog_CapNhatHSK):
        _translate = QtCore.QCoreApplication.translate
        Dialog_CapNhatHSK.setWindowTitle(_translate("Dialog_CapNhatHSK", "v5PFES - Cập nhật hệ số K"))
        self.label.setText(_translate("Dialog_CapNhatHSK", "Chọn lớp bản đồ đầu vào (.shp)"))
        self.groupBox.setTitle(_translate("Dialog_CapNhatHSK", "Tùy chọn"))
        self.noK_rBtn.setText(_translate("Dialog_CapNhatHSK", "Không áp dụng hệ số K"))
        self.K_rBtn.setText(_translate("Dialog_CapNhatHSK", "Áp dụng hệ số K"))
        self.groupBox_2.setTitle(_translate("Dialog_CapNhatHSK", "Hệ số K thành phần"))
        self.k1_cBx.setText(_translate("Dialog_CapNhatHSK", "Hệ số K1 - Chất lượng rừng"))
        self.k2_cBx.setText(_translate("Dialog_CapNhatHSK", "Hệ số K2 - Chức năng rừng"))
        self.k3_cBx.setText(_translate("Dialog_CapNhatHSK", "Hệ số K3 - Nguồn gốc rừng"))
        self.k4_cBx.setText(_translate("Dialog_CapNhatHSK", "Hệ số K4 - Khu vực khó khăn"))
        self.inBtn.setText(_translate("Dialog_CapNhatHSK", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_CapNhatHSK = QtWidgets.QDialog()
    ui = Ui_Dialog_CapNhatHSK()
    ui.setupUi(Dialog_CapNhatHSK)
    Dialog_CapNhatHSK.show()
    sys.exit(app.exec_())

