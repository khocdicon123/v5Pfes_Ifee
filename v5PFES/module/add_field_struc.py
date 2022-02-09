# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_field_struc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_field_struc(object):
    def setupUi(self, add_field_struc):
        add_field_struc.setObjectName("add_field_struc")
        add_field_struc.setEnabled(True)
        add_field_struc.resize(327, 166)
        self.gridLayout = QtWidgets.QGridLayout(add_field_struc)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(add_field_struc)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(add_field_struc)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(add_field_struc)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LblOutput = QtWidgets.QLabel(add_field_struc)
        self.LblOutput.setEnabled(True)
        self.LblOutput.setMaximumSize(QtCore.QSize(16777215, 16777211))
        self.LblOutput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LblOutput.setObjectName("LblOutput")
        self.horizontalLayout.addWidget(self.LblOutput)
        self.lineEdit = QtWidgets.QLineEdit(add_field_struc)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(add_field_struc)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.output_file_name = QgsFileWidget(add_field_struc)
        self.output_file_name.setEnabled(False)
        self.output_file_name.setObjectName("output_file_name")
        self.verticalLayout.addWidget(self.output_file_name)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(add_field_struc)
        self.buttonBox.accepted.connect(add_field_struc.accept)
        self.buttonBox.rejected.connect(add_field_struc.reject)
        QtCore.QMetaObject.connectSlotsByName(add_field_struc)

    def retranslateUi(self, add_field_struc):
        _translate = QtCore.QCoreApplication.translate
        add_field_struc.setWindowTitle(_translate("add_field_struc", "Dialog"))
        self.label.setText(_translate("add_field_struc", "1. Chọn lớp bản đồ DBR"))
        self.LblOutput.setText(_translate("add_field_struc", "2. Nhập số lưu vực"))
        self.label_2.setText(_translate("add_field_struc", "3. Chọn thư mục lưu kết quả"))

from qgsfilewidget import QgsFileWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_field_struc = QtWidgets.QDialog()
    ui = Ui_add_field_struc()
    ui.setupUi(add_field_struc)
    add_field_struc.show()
    sys.exit(app.exec_())

