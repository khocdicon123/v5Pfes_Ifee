# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_ChuanHoaDBR.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_ChuanHoa(object):
    def setupUi(self, Dialog_ChuanHoa):
        Dialog_ChuanHoa.setObjectName("Dialog_ChuanHoa")
        Dialog_ChuanHoa.setWindowModality(QtCore.Qt.WindowModal)
        Dialog_ChuanHoa.resize(461, 191)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../v5PFES/Pict/logo_ifee.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_ChuanHoa.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_ChuanHoa)
        self.gridLayout.setObjectName("gridLayout")
        self.label1 = QtWidgets.QLabel(Dialog_ChuanHoa)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self.inputShapefile = QtWidgets.QLineEdit(Dialog_ChuanHoa)
        self.inputShapefile.setObjectName("inputShapefile")
        self.gridLayout1.addWidget(self.inputShapefile, 0, 0, 1, 1)
        self.btnInputShp = QtWidgets.QPushButton(Dialog_ChuanHoa)
        self.btnInputShp.setObjectName("btnInputShp")
        self.gridLayout1.addWidget(self.btnInputShp, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout1, 1, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(Dialog_ChuanHoa)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.setObjectName("gridLayout2")
        self.inputChurung = QtWidgets.QLineEdit(Dialog_ChuanHoa)
        self.inputChurung.setObjectName("inputChurung")
        self.gridLayout2.addWidget(self.inputChurung, 0, 0, 1, 1)
        self.btnChurung = QtWidgets.QPushButton(Dialog_ChuanHoa)
        self.btnChurung.setObjectName("btnChurung")
        self.gridLayout2.addWidget(self.btnChurung, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout2, 3, 0, 1, 1)
        self.label3 = QtWidgets.QLabel(Dialog_ChuanHoa)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 4, 0, 1, 1)
        self.gridLayout3 = QtWidgets.QGridLayout()
        self.gridLayout3.setObjectName("gridLayout3")
        self.outputShapefile = QtWidgets.QLineEdit(Dialog_ChuanHoa)
        self.outputShapefile.setObjectName("outputShapefile")
        self.gridLayout3.addWidget(self.outputShapefile, 0, 0, 1, 1)
        self.btnOutput = QtWidgets.QPushButton(Dialog_ChuanHoa)
        self.btnOutput.setObjectName("btnOutput")
        self.gridLayout3.addWidget(self.btnOutput, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout3, 5, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_ChuanHoa)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 1)
        self.buttonBox.raise_()
        self.label1.raise_()
        self.label2.raise_()
        self.label3.raise_()

        self.retranslateUi(Dialog_ChuanHoa)
        self.buttonBox.accepted.connect(Dialog_ChuanHoa.accept)
        self.buttonBox.rejected.connect(Dialog_ChuanHoa.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ChuanHoa)

    def retranslateUi(self, Dialog_ChuanHoa):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ChuanHoa.setWindowTitle(_translate("Dialog_ChuanHoa", "v5PES - Chuẩn hóa bản đồ DBR"))
        self.label1.setText(_translate("Dialog_ChuanHoa", "Chọn lớp bản đồ diễn biến rừng (.shp)"))
        self.btnInputShp.setText(_translate("Dialog_ChuanHoa", "..."))
        self.label2.setText(_translate("Dialog_ChuanHoa", "Chọn danh sách chủ rừng (.xlsx)"))
        self.btnChurung.setText(_translate("Dialog_ChuanHoa", "..."))
        self.label3.setText(_translate("Dialog_ChuanHoa", "Chọn thư mục lưu kết quả chuẩn hóa"))
        self.btnOutput.setText(_translate("Dialog_ChuanHoa", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ChuanHoa = QtWidgets.QDialog()
    ui = Ui_Dialog_ChuanHoa()
    ui.setupUi(Dialog_ChuanHoa)
    Dialog_ChuanHoa.show()
    sys.exit(app.exec_())

