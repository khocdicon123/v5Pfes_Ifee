# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_CapNhatDTCT.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_CapNhatDTCT(object):
    def setupUi(self, Dialog_CapNhatDTCT):
        Dialog_CapNhatDTCT.setObjectName("Dialog_CapNhatDTCT")
        Dialog_CapNhatDTCT.resize(385, 617)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_CapNhatDTCT)
        self.buttonBox.setGeometry(QtCore.QRect(40, 570, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog_CapNhatDTCT)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 371, 151))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 232, 116))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rtn_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.rtn_checkbox.setObjectName("rtn_checkbox")
        self.verticalLayout.addWidget(self.rtn_checkbox)
        self.rtg_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.rtg_checkbox.setObjectName("rtg_checkbox")
        self.verticalLayout.addWidget(self.rtg_checkbox)
        self.rttn_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.rttn_checkbox.setObjectName("rttn_checkbox")
        self.verticalLayout.addWidget(self.rttn_checkbox)
        self.rtk_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.rtk_checkbox.setObjectName("rtk_checkbox")
        self.verticalLayout.addWidget(self.rtk_checkbox)
        self.ctr_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.ctr_checkbox.setObjectName("ctr_checkbox")
        self.verticalLayout.addWidget(self.ctr_checkbox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_CapNhatDTCT)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 371, 41))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lc_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.lc_checkbox.setGeometry(QtCore.QRect(10, 20, 171, 18))
        self.lc_checkbox.setObjectName("lc_checkbox")
        self.label = QtWidgets.QLabel(Dialog_CapNhatDTCT)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_CapNhatDTCT)
        self.label_2.setGeometry(QtCore.QRect(10, 510, 171, 16))
        self.label_2.setObjectName("label_2")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog_CapNhatDTCT)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 361, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.inPath = QtWidgets.QLineEdit(self.layoutWidget1)
        self.inPath.setObjectName("inPath")
        self.gridLayout.addWidget(self.inPath, 0, 0, 1, 1)
        self.inBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.inBtn.setObjectName("inBtn")
        self.gridLayout.addWidget(self.inBtn, 0, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog_CapNhatDTCT)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 530, 371, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.outPath = QtWidgets.QLineEdit(self.layoutWidget2)
        self.outPath.setObjectName("outPath")
        self.gridLayout_2.addWidget(self.outPath, 0, 0, 1, 1)
        self.outBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.outBtn.setObjectName("outBtn")
        self.gridLayout_2.addWidget(self.outBtn, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Dialog_CapNhatDTCT)
        self.scrollArea.setGeometry(QtCore.QRect(10, 260, 371, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 239))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog_CapNhatDTCT)
        self.buttonBox.accepted.connect(Dialog_CapNhatDTCT.accept)
        self.buttonBox.rejected.connect(Dialog_CapNhatDTCT.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CapNhatDTCT)

    def retranslateUi(self, Dialog_CapNhatDTCT):
        _translate = QtCore.QCoreApplication.translate
        Dialog_CapNhatDTCT.setWindowTitle(_translate("Dialog_CapNhatDTCT", "v5PES - Cập nhật đối tượng chi trả"))
        self.groupBox.setTitle(_translate("Dialog_CapNhatDTCT", "Chọn đối tượng:"))
        self.rtn_checkbox.setText(_translate("Dialog_CapNhatDTCT", "Các trạng thái Rừng tự nhiên"))
        self.rtg_checkbox.setText(_translate("Dialog_CapNhatDTCT", "Các trạng thái Rừng trồng gỗ"))
        self.rttn_checkbox.setText(_translate("Dialog_CapNhatDTCT", "Các trạng thái Rừng trồng tre nứa"))
        self.rtk_checkbox.setText(_translate("Dialog_CapNhatDTCT", "Các trạng thái rừng trồng khác"))
        self.ctr_checkbox.setText(_translate("Dialog_CapNhatDTCT", "Rừng mới trồng nhưng chưa thành rừng"))
        self.groupBox_2.setTitle(_translate("Dialog_CapNhatDTCT", "Cập nhật loài cây:"))
        self.lc_checkbox.setText(_translate("Dialog_CapNhatDTCT", "Cập nhật theo loài cây trồng"))
        self.label.setText(_translate("Dialog_CapNhatDTCT", "Chọn lớp bản đồ đầu vào (.shp):"))
        self.label_2.setText(_translate("Dialog_CapNhatDTCT", "Chọn lớp bản đồ đầu ra (.shp):"))
        self.inBtn.setText(_translate("Dialog_CapNhatDTCT", "..."))
        self.outBtn.setText(_translate("Dialog_CapNhatDTCT", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_CapNhatDTCT = QtWidgets.QDialog()
    ui = Ui_Dialog_CapNhatDTCT()
    ui.setupUi(Dialog_CapNhatDTCT)
    Dialog_CapNhatDTCT.show()
    sys.exit(app.exec_())
