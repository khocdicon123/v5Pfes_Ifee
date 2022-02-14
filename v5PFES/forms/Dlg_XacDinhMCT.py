# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_XacDinhMCT.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_XacDinhMCT(object):
    def setupUi(self, Dialog_XacDinhMCT):
        Dialog_XacDinhMCT.setObjectName("Dialog_XacDinhMCT")
        Dialog_XacDinhMCT.resize(392, 233)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_XacDinhMCT)
        self.buttonBox.setGeometry(QtCore.QRect(20, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_XacDinhMCT)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Dialog_XacDinhMCT)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 361, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.inBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.inBtn.setObjectName("inBtn")
        self.gridLayout.addWidget(self.inBtn, 0, 1, 1, 1)
        self.inPath = QtWidgets.QLineEdit(self.layoutWidget)
        self.inPath.setObjectName("inPath")
        self.gridLayout.addWidget(self.inPath, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog_XacDinhMCT)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 155, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.xddt_cBx = QtWidgets.QCheckBox(self.layoutWidget1)
        self.xddt_cBx.setObjectName("xddt_cBx")
        self.verticalLayout.addWidget(self.xddt_cBx)
        self.dg_cBx = QtWidgets.QCheckBox(self.layoutWidget1)
        self.dg_cBx.setObjectName("dg_cBx")
        self.verticalLayout.addWidget(self.dg_cBx)
        self.xdmct_cBx = QtWidgets.QCheckBox(self.layoutWidget1)
        self.xdmct_cBx.setObjectName("xdmct_cBx")
        self.verticalLayout.addWidget(self.xdmct_cBx)

        self.retranslateUi(Dialog_XacDinhMCT)
        self.buttonBox.accepted.connect(Dialog_XacDinhMCT.accept)
        self.buttonBox.rejected.connect(Dialog_XacDinhMCT.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_XacDinhMCT)

    def retranslateUi(self, Dialog_XacDinhMCT):
        _translate = QtCore.QCoreApplication.translate
        Dialog_XacDinhMCT.setWindowTitle(_translate("Dialog_XacDinhMCT", "v5PFES - Xác định mức chi trả"))
        self.label.setText(_translate("Dialog_XacDinhMCT", "Chọn lớp bản đồ đầu vào (.shp)"))
        self.inBtn.setText(_translate("Dialog_XacDinhMCT", "..."))
        self.xddt_cBx.setText(_translate("Dialog_XacDinhMCT", "Xác định diện tích quy đổi "))
        self.dg_cBx.setText(_translate("Dialog_XacDinhMCT", "Tính đơn giá "))
        self.xdmct_cBx.setText(_translate("Dialog_XacDinhMCT", "Xác định mức chi trả "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_XacDinhMCT = QtWidgets.QDialog()
    ui = Ui_Dialog_XacDinhMCT()
    ui.setupUi(Dialog_XacDinhMCT)
    Dialog_XacDinhMCT.show()
    sys.exit(app.exec_())

