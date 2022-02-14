# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg_XayDungCSDL.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_XayDungCSDL(object):
    def setupUi(self, Dialog_XayDungCSDL):
        Dialog_XayDungCSDL.setObjectName("Dialog_XayDungCSDL")
        Dialog_XayDungCSDL.resize(400, 202)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_XayDungCSDL)
        self.buttonBox.setGeometry(QtCore.QRect(40, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.inPath = QgsFileWidget(Dialog_XayDungCSDL)
        self.inPath.setGeometry(QtCore.QRect(20, 70, 361, 27))
        self.inPath.setObjectName("inPath")
        self.label = QtWidgets.QLabel(Dialog_XayDungCSDL)
        self.label.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_XayDungCSDL)
        self.buttonBox.accepted.connect(Dialog_XayDungCSDL.accept)
        self.buttonBox.rejected.connect(Dialog_XayDungCSDL.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_XayDungCSDL)

    def retranslateUi(self, Dialog_XayDungCSDL):
        _translate = QtCore.QCoreApplication.translate
        Dialog_XayDungCSDL.setWindowTitle(_translate("Dialog_XayDungCSDL", "v5PFES - Xây dựng cơ sở dữ liệu"))
        self.inPath.setFilter(_translate("Dialog_XayDungCSDL", "Shape file (*.shp)"))
        self.label.setText(_translate("Dialog_XayDungCSDL", "Chọn lớp bản đồ đầu vào (.shp)"))

from qgsfilewidget import QgsFileWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_XayDungCSDL = QtWidgets.QDialog()
    ui = Ui_Dialog_XayDungCSDL()
    ui.setupUi(Dialog_XayDungCSDL)
    Dialog_XayDungCSDL.show()
    sys.exit(app.exec_())

