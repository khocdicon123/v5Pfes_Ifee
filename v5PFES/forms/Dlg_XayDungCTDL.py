# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_XayDungCTDL.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_XayDungCTDL(object):
    def setupUi(self, Dialog_XayDungCTDL):
        Dialog_XayDungCTDL.setObjectName("Dialog_XayDungCTDL")
        Dialog_XayDungCTDL.resize(448, 194)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog_XayDungCTDL)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(Dialog_XayDungCTDL)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_XayDungCTDL)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog_XayDungCTDL)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog_XayDungCTDL)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog_XayDungCTDL)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_XayDungCTDL)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog_XayDungCTDL)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog_XayDungCTDL)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog_XayDungCTDL)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 5, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_XayDungCTDL)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 6, 0, 1, 1)

        self.retranslateUi(Dialog_XayDungCTDL)
        self.buttonBox.accepted.connect(Dialog_XayDungCTDL.accept)
        self.buttonBox.rejected.connect(Dialog_XayDungCTDL.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_XayDungCTDL)

    def retranslateUi(self, Dialog_XayDungCTDL):
        _translate = QtCore.QCoreApplication.translate
        Dialog_XayDungCTDL.setWindowTitle(_translate("Dialog_XayDungCTDL", "v5PES - Xây dựng cấu trúc dữ liệu"))
        self.label.setText(_translate("Dialog_XayDungCTDL", "Chọn lớp bản đồ hiện trạng rừng (.shp)"))
        self.pushButton.setText(_translate("Dialog_XayDungCTDL", "..."))
        self.label_2.setText(_translate("Dialog_XayDungCTDL", "Chọn danh sách lưu vực (.xlsx)"))
        self.pushButton_2.setText(_translate("Dialog_XayDungCTDL", "..."))
        self.label_3.setText(_translate("Dialog_XayDungCTDL", "Chọn thu mục chứa lớp bản đồ đầu ra  (.shp)"))
        self.pushButton_3.setText(_translate("Dialog_XayDungCTDL", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_XayDungCTDL = QtWidgets.QDialog()
    ui = Ui_Dialog_XayDungCTDL()
    ui.setupUi(Dialog_XayDungCTDL)
    Dialog_XayDungCTDL.show()
    sys.exit(app.exec_())

