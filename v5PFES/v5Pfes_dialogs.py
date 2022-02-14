#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------
#	v5pfes_dialogs - Dialog classes for v5pfes
#
#	begin				: 21/03/2020
#	copyright			: (c) 2020 by IFEE
#	email				: ifee@ifee.edu.vn
# --------------------------------------------------------
import csv
import math
import os.path
import operator
import sys
import time
import shutil
import re
import glob
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QDir
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog
from qgis.core import QgsProject, Qgis
from osgeo import ogr
import pandas as pd
import numpy as np
import xlrd
from collections import OrderedDict
import simplejson as json
import json
from json import *

# Initialize Qt resources from file resources.py

# Import the code for the dialog
import os.path
import processing

from qgis.core import *
import qgis.utils
from qgis.utils import iface
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from .v5pfes_library import *


#from .spilit_layer_dialog import SplitByAttributesDialog

from qgis.gui import QgsMessageBar
import pathlib
from pathlib import Path


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/forms")

from Dlg_ChuanHoaDBR import *
from Dlg_XayDungCTDL import *
from Dlg_CapNhatVCT import *
from Dlg_CapNhatDT import *
from Dlg_CapNhatDTCT import *
from Dlg_CapNhatXKK import *
from Dlg_CapNhatHSK import *
from Dlg_XacDinhMCT import *
from Dlg_XayDungCSDL import *
from Dlg_XuatBieuNhom1 import *
from Dlg_XuatBieuNhom2 import *

class ChuanHoaDBR_Dlg(QDialog, Ui_Dialog_ChuanHoa):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.inputShapefile.setText('')
		self.btnInputShp.clicked.connect(self.select_input_shape)
		self.inputChurung.setText('')
		self.btnChurung.clicked.connect(self.select_input_xls)
		self.outputShapefile.setText('')											 
		self.btnOutput.clicked.connect(self.select_output_shape)
		self.buttonBox.accepted.connect(self.run)

		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8
		
	def select_input_shape(self):
	  
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp bản đồ diễn biến rừng", "", "Shapefile (*.shp)")[0])
		self.inputShapefile.setText(self.path_solution)
 

	def select_input_xls(self):
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn danh sách chủ rừng", "", "MS - Excel (*.xlsx);;MS - Excel (*.xls)")[0])
		self.inputChurung.setText(self.path_solution)
		
	def select_output_shape(self):
		self.path_solution = str(QFileDialog.getSaveFileName(self, "v5PFES-Chọn thư mục lưu kết quả chuẩn hóa", "", "Shapefile (*.shp)")[0])
		self.outputShapefile.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)

		inpath = self.inputShapefile.text()
		outpath = self.outputShapefile.text()
		inputChurung = self.inputChurung.text()
		bname = os.path.split(outpath)[1]
		fname = os.path.splitext(bname)[0]
		bpath = os.path.dirname(inpath)

		i=0
		for n in range(1,6):
			i=i+1
			if n ==1:
			#1
				delete_fields(inpath,outpath)
				shp =  QgsVectorLayer(outpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)
			#2
			elif n==2:
				add_fields(layer)
			#3
			elif n==3:
				rename_fields(layer)
				QgsProject.instance().removeAllMapLayers()
			#4
			elif n==4:
				join_fields(outpath,inputChurung)
				update_doituong(outpath)

			else:	
				shp =  QgsVectorLayer(outpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)
				with edit(layer):		
					for feature in layer.getFeatures():
						malcay = feature['maloaicay']
						if malcay:
							loaicay = layloaicay(malcay)
							feature.setAttribute(feature.fieldNameIndex('sldlr'), loaicay)
							layer.updateFeature(feature)

				QgsProject.instance().removeAllMapLayers()
				shp =  QgsVectorLayer(outpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)		
			percent = (i/float(6)) * 100
			progress.setValue(percent)				
			time.sleep(1)
		qgis.utils.iface.messageBar().clearWidgets()			
			
			
		self.iface.messageBar().pushMessage("Quá trình chuẩn hóa thành công!", level=Qgis.Success, duration=5)

class XayDungCTDL_Dlg(QDialog, Ui_Dialog_XayDungCTDL):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.lineEdit.setText('')
		self.pushButton.clicked.connect(self.select_input_shape)
		self.lineEdit_2.setText('')
		self.pushButton_2.clicked.connect(self.select_input_xls)
		self.lineEdit_3.setText('')											 
		self.pushButton_3.clicked.connect(self.select_output_shape)
		self.buttonBox.accepted.connect(self.run)

		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8
		
	def select_input_shape(self):
	  
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp bản đồ hiện trạng rừng", "", "Shapefile (*.shp)")[0])
		self.lineEdit.setText(self.path_solution)
 
	def select_input_xls(self):
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn danh sách lưu vực", "", "MS - Excel (*.xlsx);;MS - Excel (*.xls)")[0])
		self.lineEdit_2.setText(self.path_solution)
		
	def select_output_shape(self):
		self.path_solution = str(QFileDialog.getSaveFileName(self, "v5PFES-Chọn thư mục chứa lớp bản đồ đầu ra", "", "Shapefile (*.shp)")[0])
		self.lineEdit_3.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)
		
		tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.shp'  
		inpath = self.lineEdit.text()
		outpath = self.lineEdit_3.text()
		inputLuuvuc = self.lineEdit_2.text()
		bname = os.path.split(outpath)[1]
		fname = os.path.splitext(bname)[0]
		bpath = os.path.dirname(inpath)

		i=0
		for n in range(1,4):
			i=i+1
			if n ==1:		   
				shp =  QgsVectorLayer(inpath, '', 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

				QgsVectorFileWriter.writeAsVectorFormat(layer, tempo, "UTF-8", layer.crs(), "ESRI Shapefile")
				QgsProject.instance().removeAllMapLayers()

			elif n ==2:
				nshp =  QgsVectorLayer(tempo, '', 'ogr')
				nlayer = QgsProject.instance().addMapLayer(nshp)
				add_newfields(nlayer, outpath)

			else:
				convert_json(inputLuuvuc)	 
				QgsProject.instance().removeAllMapLayers()

				shp =  QgsVectorLayer(outpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

			percent = (i/float(6)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình xây dựng cấu trúc dữ liệu thành công", level=Qgis.Success, duration=5)

class CapNhatVCT_Dlg(QDialog, Ui_Dialog_CapNhatVCT):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.lineEdit.setText('')
		self.pushButton.clicked.connect(self.select_input_shape)
		self.lineEdit_2.setText('')
		self.pushButton_2.clicked.connect(self.select_input_luuvuc)
		self.lineEdit_4.setText('')											 
		self.pushButton_3.clicked.connect(self.select_output_shape)
		self.buttonBox.accepted.connect(self.run)
		self.laydsluuvuc()
		self.checkBox.stateChanged.connect(self.luuvuctrung)
		self.comboBox2.setEnabled(False)

		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8
		
	def select_input_shape(self):
	  
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp bản đồ đầu vào", "", "Shapefile (*.shp)")[0])
		self.lineEdit.setText(self.path_solution)

	def laydsluuvuc(self):
		self.comboBox.clear()
		watershed = docdsluuvuc()
		for catchment in watershed:
			cname = catchment['Tenlv']
			ccode = catchment['malv']
			self.comboBox.addItems([cname])

	def luuvuctrung(self):
		if self.checkBox.isChecked():
			self.comboBox2.setEnabled(True)
			self.pushButton_2.setEnabled(False)
			self.lineEdit_2.setEnabled(False)
			self.comboBox2.clear()
			watershed = docdsluuvuc()
			for catchment in watershed:
				cname = catchment['Tenlv']
				ccode = catchment['malv']
				self.comboBox2.addItems([cname])
		else:
			self.comboBox2.clear()
			self.comboBox2.setEnabled(False)
			self.pushButton_2.setEnabled(True)
			self.lineEdit_2.setEnabled(True)	   

	def laymalv(self,tenlv):
		listlv = docdsluuvuc()
		for lvchon in listlv:
			if lvchon['Tenlv'] == tenlv:
				return str(lvchon['malv']).split('.')[0]			  

	def select_input_luuvuc(self):
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp ranh giới lưu vực", "", "Shapefile (*.shp)")[0])
		self.lineEdit_2.setText(self.path_solution)
		
	def select_output_shape(self):
		self.path_solution = str(QFileDialog.getSaveFileName(self, "v5PFES-Chọn thư mục chứa lớp bản đồ đầu ra", "", "Shapefile (*.shp)")[0])
		self.lineEdit_4.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)
		
		clip_tempo = str(Path(__file__).parent.absolute()) + '/tempo/clip.shp'
		union_tempo = str(Path(__file__).parent.absolute()) + '/tempo/union.shp'
		buffer_tempo = str(Path(__file__).parent.absolute()) + '/tempo/buffer.shp'
		selected_tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.shp'
		tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.shp' 
		
		inpath = self.lineEdit.text()
		outpath = self.lineEdit_4.text()
		inputLuuvuc = self.lineEdit_2.text()
		mlv1 =  self.laymalv(self.comboBox.currentText())
		mlv2 =  self.laymalv(self.comboBox2.currentText())
		bname = os.path.split(outpath)[1]
		fname = os.path.splitext(bname)[0]
		bpath = os.path.dirname(inpath)

		if self.checkBox.isChecked():			
			k=3
			i=0
			for n in range(1,k):
				if n == 1:
					shp =  QgsVectorLayer(inpath, '', 'ogr')
					layer = QgsProject.instance().addMapLayer(shp)
					QgsVectorFileWriter.writeAsVectorFormat(layer, tempo, "UTF-8", layer.crs(), "ESRI Shapefile")
					QgsProject.instance().removeAllMapLayers()				
				else:
					update_malv(tempo,mlv1,mlv2,outpath)
					QgsProject.instance().removeAllMapLayers()
					shp =  QgsVectorLayer(outpath, fname, 'ogr')
					layer = QgsProject.instance().addMapLayer(shp)
			
		else:
			k=6
			i=0
			for n in range(1,k):
				i=i+1
				if n == 1:
					clip(inpath, inputLuuvuc,clip_tempo)
				elif n == 2:
					union(inpath,clip_tempo,union_tempo)
				elif n == 3:
					buffer(inputLuuvuc,buffer_tempo)
				elif n == 4:
					selectbylocation(union_tempo,buffer_tempo,mlv1,selected_tempo)
				else:
					delete_duplicate_fields(selected_tempo,outpath)
					QgsProject.instance().removeAllMapLayers()
					shp = QgsVectorLayer(outpath, fname, 'ogr')
					layer = QgsProject.instance().addMapLayer(shp)

			percent = (i/float(k-1)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình cập nhật vùng chi trả thành công", level=Qgis.Success, duration=5)

class CapNhatDT_Dlg(QDialog, Ui_Dialog_CapNhatDT):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.inPath.setText('')
		self.pushButton.clicked.connect(self.select_input_shape)
		self.checkBox.setChecked(True)
		self.lineEdit_2.setText('')											 
		self.pushButton_2.clicked.connect(self.select_output_shape)
		self.buttonBox.accepted.connect(self.run)

		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8
		
	def select_input_shape(self):
	  
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp bản đồ đầu vào", "", "Shapefile (*.shp)")[0])
		self.inPath.setText(self.path_solution)	
		
	def select_output_shape(self):
		self.path_solution = str(QFileDialog.getSaveFileName(self, "v5PFES-Chọn thư mục chứa lớp bản đồ đầu ra", "", "Shapefile (*.shp)")[0])
		self.lineEdit_2.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)
		
		tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.shp'  
		inpath = self.inPath.text()
		outpath = self.lineEdit_2.text()
		bname = os.path.split(outpath)[1]
		fname = os.path.splitext(bname)[0]
		bpath = os.path.dirname(inpath)

		i=0
		for n in range(1,3):
			i=i+1
			if n ==1:		 
				shp =  QgsVectorLayer(inpath, '', 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

				QgsVectorFileWriter.writeAsVectorFormat(layer, tempo, "UTF-8", layer.crs(), "ESRI Shapefile")
				QgsProject.instance().removeAllMapLayers()

			else:
				nshp =  QgsVectorLayer(tempo, '', 'ogr')
				nlayer = QgsProject.instance().addMapLayer(nshp)
				
				if self.checkBox.isChecked():
					recalculate_area_1(nlayer, outpath)
				else:
					recalculate_area_2(nlayer, outpath)
				
				QgsProject.instance().removeAllMapLayers()
				
				shp =  QgsVectorLayer(outpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

			percent = (i/float(6)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình cập nhật diện tích chi trả thành công", level=Qgis.Success, duration=5)

class CapNhatDTCT_Dlg(QDialog, Ui_Dialog_CapNhatDTCT):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.inPath.setText('')
		self.inBtn.clicked.connect(self.select_input_shape)
		self.rtn_checkbox.setChecked(True)
		self.rtg_checkbox.setChecked(True)
		self.rttn_checkbox.setChecked(True)
		self.rtk_checkbox.setChecked(False)
		self.ctr_checkbox.setChecked(False)
		self.lc_checkbox.setChecked(False)
		self.lc_checkbox.stateChanged.connect(self.select_treespecies)
		self.outPath.setText('')											 
		self.outBtn.clicked.connect(self.select_output_shape)
		self.buttonBox.accepted.connect(self.run)

		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8
		
	def select_input_shape(self):
	  
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp bản đồ đầu vào", "", "Shapefile (*.shp)")[0])
		self.inPath.setText(self.path_solution)

	def select_treespecies(self):
		try:
			if self.lc_checkbox.isChecked():
				self.tableWidget.clear()

				in_shp = str(self.inPath.text())
				driver = ogr.GetDriverByName("ESRI Shapefile")
				dataSource = driver.Open(in_shp, 1)
				layer = dataSource.GetLayer()

				listlc = []
				for feature in layer:
					if feature['vungchitra'] == 1:
						listlc.append(feature['sldlr'])
				unique_lc = list(set(listlc))
				lc = list(filter(None,unique_lc))
			
				self.tableWidget.setRowCount(len(lc))
				self.tableWidget.setColumnCount(2)
				self.tableWidget.setHorizontalHeaderLabels(["Tên loài cây", "Chitrả"])
				self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.EditTriggers(2))

				for i in range (self.tableWidget.rowCount()):
					self.tableWidget.setItem(i,0,QTableWidgetItem(lc[i]))
					self.tableWidget.setItem(i,1,QTableWidgetItem("1"))
			else:
				for i in reversed (range (self.tableWidget.rowCount())):
					self.tableWidget.removeRow(i)
		except:
			self.iface.messageBar().pushMessage("Chưa chọn lớp đầu vào hoặc lớp đầu vào không đúng định dạng", level=Qgis.Warning, duration=5)

  
	def select_output_shape(self):
		self.path_solution = str(QFileDialog.getSaveFileName(self, "v5PFES-Chọn thư mục chứa lớp bản đồ đầu ra", "", "Shapefile (*.shp)")[0])
		self.outPath.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)
		
		tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.shp'  
		inpath = self.inPath.text()
		outpath = self.outPath.text()
		bname = os.path.split(outpath)[1]
		fname = os.path.splitext(bname)[0]
		bpath = os.path.dirname(inpath)

		ds_loaicay_ct = []
		for i in range (self.tableWidget.rowCount()):
			chitra = self.tableWidget.item(i,1).text()
			if chitra == "1":
				ds_loaicay_ct.append(self.tableWidget.item(i,0).text())		   

		i=0
		for n in range(1,8):
			i=i+1
			if n ==1:		 
				shp =  QgsVectorLayer(inpath, '', 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

				QgsVectorFileWriter.writeAsVectorFormat(layer, tempo, "UTF-8", layer.crs(), "ESRI Shapefile")
				QgsProject.instance().removeAllMapLayers()

			elif n==2:
				nshp =  QgsVectorLayer(tempo, '', 'ogr')
				nlayer = QgsProject.instance().addMapLayer(nshp)	
				if self.rtn_checkbox.isChecked():
					rtn_payment(nlayer)					
				else:
					pass

			elif n==3:
				if self.rtg_checkbox.isChecked():
					rtg_payment(nlayer) 
				else:
					pass
					
			elif n==4:
				if self.rttn_checkbox.isChecked():
					rttn_payment(nlayer) 
				else:
					pass	

			elif n==5:
				if self.rtk_checkbox.isChecked():
					rtk_payment(nlayer) 
				else:
					pass

			elif n==6:
				if self.ctr_checkbox.isChecked():
					ctr_payment(nlayer) 
				else:
					pass

			else:
				if self.lc_checkbox.isChecked():
					lc_payment(nlayer,ds_loaicay_ct,outpath)
				else:
					lc__non_payment(nlayer,outpath)
								 
				QgsProject.instance().removeAllMapLayers()		
				shp =  QgsVectorLayer(outpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

			percent = (i/float(6)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình cập nhật đối tượng chi trả thành công", level=Qgis.Success, duration=5)

class CapNhatXKK_Dlg(QDialog, Ui_Dialog_CapNhatXKK):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.inPath.setText('')
		self.inBtn.clicked.connect(self.select_input_shape)
		self.checkBox.stateChanged.connect(self.edit_remoteArea)
		self.buttonBox.accepted.connect(self.run)

		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8
		
	def select_input_shape(self):   
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp bản đồ đầu vào", "", "Shapefile (*.shp)")[0])
		self.inPath.setText(self.path_solution)

	def edit_remoteArea(self):
		try:
			if self.checkBox.isChecked():
				self.tableWidget.clear()
				xakhokhan = docdsxkk()
				in_shp = str(self.inPath.text())
				driver = ogr.GetDriverByName("ESRI Shapefile")
				dataSource = driver.Open(in_shp, 1)
				layer = dataSource.GetLayer()

				vct = []
				for feature in layer:
					if feature['chitra'] == 1:
						vct.append(feature['maxa'])
				listvct = list(set(vct))

				listmaxa = []
				listxa = []
				listkhuvuc = []

				for feature in xakhokhan:
					giatri = int(feature['MAXA'])
					if giatri in listvct:
						listmaxa.append(feature['MAXA'])
						listxa.append(feature['XA'])
						listkhuvuc.append(feature['KHUVUC'])

				self.tableWidget.setRowCount(len(listmaxa))
				self.tableWidget.setColumnCount(3)
				self.tableWidget.setHorizontalHeaderLabels(["Mã xã", "Tên xã", "Khu vực"])
				self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.EditTriggers(2))

				for i in range (self.tableWidget.rowCount()):
					self.tableWidget.setItem(i,0,QTableWidgetItem(listmaxa[i]))
					self.tableWidget.setItem(i,1,QTableWidgetItem(listxa[i]))
					self.tableWidget.setItem(i,2,QTableWidgetItem(listkhuvuc[i]))
			else:
				for i in reversed (range (self.tableWidget.rowCount())):
						self.tableWidget.removeRow(i)
		except:
			self.iface.messageBar().pushMessage("Chưa chọn lớp đầu vào hoặc lớp đầu vào không đúng định dạng", level=Qgis.Warning, duration=5)	

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)
		
		inpath = self.inPath.text()
		bname = os.path.split(inpath)[1]
		fname = os.path.splitext(bname)[0]
		bpath = os.path.dirname(inpath)

		ds_khuvuc = []
		ds_maxa = []

		for i in range (self.tableWidget.rowCount()):
			xkk= self.tableWidget.item(i,2).text()
			lmx = self.tableWidget.item(i,0).text()
			ds_khuvuc.append(xkk)
			ds_maxa.append(lmx)			  

		i=0
		for n in range(1,3):
			i=i+1
			if n ==1:
				if self.checkBox.isChecked():		 
					shp =  QgsVectorLayer(inpath, '', 'ogr')
					layer = QgsProject.instance().addMapLayer(shp)
					update_xkk(layer,ds_maxa,ds_khuvuc)
					edit_dsxkk(ds_maxa,ds_khuvuc)
				else:
					join_xkk(inpath)					
			else:											
				QgsProject.instance().removeAllMapLayers()		
				shp =  QgsVectorLayer(inpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

			percent = (i/float(6)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình cập nhật vùng khó khăn thành công", level=Qgis.Success, duration=5)

class CapNhatHSK_Dlg(QDialog, Ui_Dialog_CapNhatHSK):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.inPath.setText('')
		self.inBtn.clicked.connect(self.select_input_shape)	
		self.k1_cBx.setEnabled(False)
		self.k2_cBx.setEnabled(False)
		self.k3_cBx.setEnabled(False)
		self.k4_cBx.setEnabled(False)
		self.noK_rBtn.setChecked(True)
		self.noK_rBtn.toggled.connect(self.check_k)
		self.buttonBox.accepted.connect(self.run)
		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8
	
	def check_k(self):
		if self.noK_rBtn.isChecked():
			self.k1_cBx.setEnabled(False)
			self.k2_cBx.setEnabled(False)
			self.k3_cBx.setEnabled(False)
			self.k4_cBx.setEnabled(False)
			self.k1_cBx.setChecked(False)
			self.k2_cBx.setChecked(False)
			self.k3_cBx.setChecked(False)
			self.k4_cBx.setChecked(False)
		else:
			self.k1_cBx.setEnabled(True)
			self.k2_cBx.setEnabled(True)
			self.k3_cBx.setEnabled(True)
			self.k4_cBx.setEnabled(True)					
		
	def select_input_shape(self):	  
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp bản đồ đầu vào", "", "Shapefile (*.shp)")[0])
		self.inPath.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)
  
		inpath = self.inPath.text()
		bname = os.path.split(inpath)[1]
		fname = os.path.splitext(bname)[0]
		bpath = os.path.dirname(inpath)	   

		i=0
		for n in range(1,3):
			i=i+1
			if n==1:	
				if self.noK_rBtn.isChecked():
					update_K(inpath)					
				else:
					if self.k1_cBx.isChecked():
						update_K1(inpath)
					else:
						update_K1_uncheck(inpath)

					if self.k2_cBx.isChecked():
						update_K2(inpath)
					else:
						update_K2_uncheck(inpath)

					if self.k3_cBx.isChecked():
						update_K3(inpath)
					else:
						update_K3_uncheck(inpath)

					if self.k4_cBx.isChecked():
						update_K4(inpath)
					else:
						update_K4_uncheck(inpath)

					update_K0(inpath)					
			else:								 
				QgsProject.instance().removeAllMapLayers()		
				shp =  QgsVectorLayer(inpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

			percent = (i/float(6)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình cập nhật hệ số K thành công", level=Qgis.Success, duration=5)

class XacDinhMCT_Dlg(QDialog, Ui_Dialog_XacDinhMCT):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.inPath.setText('')
		self.inBtn.clicked.connect(self.select_input_shape)
		self.xddt_cBx.setChecked(True)
		self.dg_cBx.setChecked(False)
		self.xdmct_cBx.setChecked(False)
		self.buttonBox.accepted.connect(self.run)
		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8					
		
	def select_input_shape(self):	  
		self.path_solution = str(QFileDialog.getOpenFileName(self, "v5PFES-Chọn lớp bản đồ đầu vào", "", "Shapefile (*.shp)")[0])
		self.inPath.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)
  
		inpath = self.inPath.text()
		bname = os.path.split(inpath)[1]
		fname = os.path.splitext(bname)[0]
		bpath = os.path.dirname(inpath)	   

		i=0
		for n in range(1,5):
			i=i+1
			if n==1:
				if self.xddt_cBx.isChecked():
					payment_area(inpath)		
				else:
					pass
			elif n==2:
				if self.dg_cBx.isChecked():
					price(inpath)				
				else:
					pass
			elif n==3:
				if self.xdmct_cBx.isChecked():
					payment_level(inpath)				
				else:
					pass					
			else:								 
				QgsProject.instance().removeAllMapLayers()		
				shp =  QgsVectorLayer(inpath, fname, 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)

			percent = (i/float(6)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình xác định mức chi trả thành công", level=Qgis.Success, duration=5)

class XayDungCSDL_Dlg(QDialog, Ui_Dialog_XayDungCSDL):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.buttonBox.accepted.connect(self.run)
		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8					

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)
  
		tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.xlsx'
		tempo_THX = str(Path(__file__).parent.absolute()) + '/tempo/THX.json'
		tempo_ChuRung = str(Path(__file__).parent.absolute()) + '/tempo/ChuRung.json'
		inpath = self.inPath.filePath() 

		i=0
		for n in range(1,4):
			i=i+1
			if n==1:
				shp =  QgsVectorLayer(inpath, '', 'ogr')
				layer = QgsProject.instance().addMapLayer(shp)
				QgsVectorFileWriter.writeAsVectorFormat(layer, tempo, "UTF-8", layer.crs(), "xlsx")	
				QgsProject.instance().removeAllMapLayers()				
			elif n==2:
				export_THX(tempo,tempo_THX)
			else:
				export_ChuRung(tempo,tempo_ChuRung)								 
				

			percent = (i/float(3)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình xây dựng cơ sở dữ liệu thành công", level=Qgis.Success, duration=5)


class XuatBieuNhom2_Dlg(QDialog, Ui_Dialog_XuatBieuNhom2):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.out_path.setText('')											 
		self.btn_path.clicked.connect(self.select_output)
		self.btn_ok.clicked.connect(self.run)
		self.btn_cancel.clicked.connect(self.close_form)
		self.laydscr()
		self.laydstinh()
		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8	

	def laydscr(self):
		dscr = docds()
		self.com_churung.clear()
		for cr in dscr:
			tencr = cr['churung']
			self.com_churung.addItems([tencr])
	def layma(self):
		tencr = self.com_churung.currentText()
		dscr = docds()
		for cr in dscr:
			if cr['churung'] == tencr:
				macr = cr['machur']
				tentinh = cr['tinh']
				value = {'macr': macr, 'tinh': tentinh}
				return value
	def laydstinh(self):
		dstinh = docds()
		values = set()
		for item in dstinh:
			values.add(item['tinh'])
		self.com_tinh.addItems(values)

	def select_output(self):
		self.path_solution = str(QFileDialog.getExistingDirectory(self, "v5PFES-Chọn thư mục lưu kết quả"))
		self.out_path.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)

		tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.xlsx'
		outpath = self.out_path.text()
		tinh = (self.layma())['tinh']
		cr = self.com_churung.currentText()
		machur = (self.layma())['macr']
		export = outpath + '/bieu2.xlsx'
		hc_out = outpath + '/TenHanhChinh.xlsx'
		tinh_out = outpath + '/TenTinh.xlsx'
	#xa_out = outpath + '/TenXa.xlsx'
		copy = str(Path(__file__).parent.absolute()) + '/data/Mau13_14.xlsm'
		paste = outpath + '/' + str(machur) +'_'+ convert_TVKD(cr)+'.xlsm'
		run = 'start excel.exe '
		i=0
		for n in range(1,6):
			i=i+1
			if n==1:
				df_pfes = pd.read_excel(tempo)
				df_pfes = df_pfes.loc[(df_pfes['machur'] == machur)]
				df_pfes = df_pfes.loc[((df_pfes['chitra'] == 1))]
				df_pfes = df_pfes.loc[(df_pfes['dtichct'] > 0)]
			elif n==2:
				report_forestActor(df_pfes, export)
			elif n==3:
				churung_export(tempo,machur,hc_out)
			elif n==4:
				province_export(tempo,machur,tinh_out)
			else:
				shutil.copy2(copy, paste)
				os.system(run + paste)
			QgsProject.instance().removeAllMapLayers()

			percent = (i/float(5)) * 100
			progress.setValue(percent)
			time.sleep(1)
		qgis.utils.iface.messageBar().clearWidgets()
		self.iface.messageBar().pushMessage("Quá trình xuất biểu thành công", level=Qgis.Success, duration=5)

	def close_form(self):
		pathout = self.out_path.text()
		databases = filter(os.path.isfile, glob.glob(pathout + '/*.xlsm'))
		if databases:
			for file in databases:
				os.remove(file)
		if os.path.exists(pathout + '/TenHanhChinh.xlsx'):
			os.remove(pathout + '/TenHanhChinh.xlsx')
		if os.path.exists(pathout + '/TenXa.xlsx'):
			os.remove(pathout + '/TenXa.xlsx')
		if os.path.exists(pathout + '/TenTinh.xlsx'):
			os.remove(pathout + '/TenTinh.xlsx')
		if os.path.exists(pathout + '/bieu1.xlsx'):
			os.remove(pathout + '/bieu1.xlsx')
		if os.path.exists(pathout + '/bieu2.xlsx'):
			os.remove(pathout + '/bieu2.xlsx')
		self.close()

class XuatBieuNhom1_Dlg(QDialog, Ui_Dialog_XuatBieuNhom1):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.output_path.setText('')											 
		self.toolButton.clicked.connect(self.select_output)
		self.btn_OK.clicked.connect(self.run)
		self.btn_cancel.clicked.connect(self.close_form)

		orgEncoding=QgsSettings().value('/Processing/encoding') # save setting
		QgsSettings().setValue('/Processing/encoding', 'utf-8') # set uft8	

		try:
			pathTHX = str(Path(__file__).parent.absolute()) + '/tempo/THX.json'

			def loc_tinh():
				df = pd.read_json (pathTHX)
				return (df['tinh'].unique())

			def loc_huyen(tentinh):
				df = pd.read_json (pathTHX)
				df = df[df['tinh'] == tentinh]
				return (df['huyen'].unique())
				
			def loc_xa(tenhuyen):
				df = pd.read_json (pathTHX)
				df = df[df['huyen'] == tenhuyen]
				return (df['xa'].unique())

			def laydanhsachxa():
				self.combo_xa.clear()
				tenhuyen = self.com_huyen.currentText()
				ds_xa = loc_xa(tenhuyen)
				self.combo_xa.addItems(ds_xa)

			def laydanhsachhuyen():
				self.com_huyen.clear()
				self.combo_xa.clear()
				tentinh = self.com_tinh.currentText()
				ds_huyen = loc_huyen(tentinh)
				self.com_huyen.addItems(ds_huyen)

			self.com_huyen.currentIndexChanged.connect(laydanhsachxa)
			self.com_tinh.currentIndexChanged.connect(laydanhsachhuyen)

			ds_tinh = loc_tinh()
			self.com_tinh.clear()
			self.com_tinh.addItems(ds_tinh)

			tentinh = self.com_tinh.currentText()
			ds_huyen = loc_huyen(tentinh)
			self.com_huyen.addItems(ds_huyen)
		except:
			self.iface.messageBar().pushMessage("Chưa xây dựng CSDL", level=Qgis.Warning, duration=5)

	def select_output(self):
		self.path_solution = str(QFileDialog.getExistingDirectory(self, "v5PFES-Chọn thư mục lưu kết quả"))
		self.output_path.setText(self.path_solution)

	def run(self):
		#clear the message bar		
		qgis.utils.iface.messageBar().clearWidgets() 
		#set a new message bar
		progressMessageBar = qgis.utils.iface.messageBar()
		######################################
		# Prepare your progress Bar
		######################################
		progress = QProgressBar()
		#Maximum is set to 100, making it easy to work with percentage of completion
		progress.setMaximum(100) 
		#pass the progress bar to the message Bar
		progressMessageBar.pushWidget(progress)

		tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.xlsx'
		outpath = self.output_path.text()
		tinh = self.com_tinh.currentText()
		huyen = self.com_huyen.currentText()
		xa = self.combo_xa.currentText()
		maxa = get_ma_xa(tinh,huyen,xa)

		tempo = str(Path(__file__).parent.absolute()) + '/tempo/tempo.xlsx'
		export = outpath + '/bieu1.xlsx'
		hc_out = outpath + '/TenHanhChinh.xlsx'
		tinh_out = outpath + '/TenTinh.xlsx'
		xa_out = outpath + '/TenXa.xlsx'
		copy = str(Path(__file__).parent.absolute()) + '/data/Mau12_14.xlsm'
		paste = outpath + '/' + str(maxa) +'_'+ convert_TVKD(xa)+'.xlsm'
		run = 'start excel.exe '

		i=0
		for n in range(1,7):
			i=i+1
			if n==1:
				df_pfes = pd.read_excel(tempo)
				# ds_maxa = sorted(df_pfes['maxa'].unique().tolist())
				df_pfes = df_pfes.sort_values(by=['maxa','dtuong','churung'], ascending=True)
				df_pfes = df_pfes.loc[((df_pfes['chitra'] == 1))]				
			elif n==2:
				report_comumune(df_pfes,maxa,export)
			elif n==3:
				hanhchinh_export(tempo,maxa,hc_out)
			elif n==4:
				tinh_export(tempo,maxa,tinh_out)
			elif n==5:
				xa_export(tempo,maxa,xa_out)
			else:
				shutil.copy2(copy, paste)
				os.system(run + paste)
			QgsProject.instance().removeAllMapLayers()	
		
			percent = (i/float(6)) * 100
			progress.setValue(percent)				
			time.sleep(1) 
		qgis.utils.iface.messageBar().clearWidgets()					  
		self.iface.messageBar().pushMessage("Quá trình xuất biểu thành công", level=Qgis.Success, duration=5)

	def close_form(self):
		pathout = self.output_path.text()
		databases = filter(os.path.isfile, glob.glob(pathout + '/*.xlsm'))
		if databases:
			for file in databases:
				os.remove(file)
		if os.path.exists(pathout + '/TenHanhChinh.xlsx'):
			os.remove(pathout + '/TenHanhChinh.xlsx')
		if os.path.exists(pathout + '/TenXa.xlsx'):
			os.remove(pathout + '/TenXa.xlsx')
		if os.path.exists(pathout + '/TenTinh.xlsx'):
			os.remove(pathout + '/TenTinh.xlsx')
		if os.path.exists(pathout + '/bieu1.xlsx'):

			os.remove(pathout + '/bieu1.xlsx')
		if os.path.exists(pathout + '/bieu2.xlsx'):
			os.remove(pathout + '/bieu2.xlsx')
		self.close()
