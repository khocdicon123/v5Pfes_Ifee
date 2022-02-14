#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------------------------------------------------
#    v5pfes_menu - QGIS plugins menu class
##  --------------------------------------------------------

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from .v5pfes_dialogs import *
from .v5pfes_library import *
# ---------------------------------------------

class v5pfes_menu:
	
	def __init__(self, iface):
		self.iface = iface
		self.v5pfes_menu = None

	def ifee_add_submenu(self, submenu):
		if self.v5pfes_menu != None:
			self.v5pfes_menu.addMenu(submenu)
		else:
			self.iface.addPluginToMenu("&ifee", submenu.menuAction())

	def initGui(self):


		# Khởi tạo IFEE trên menubar của QGIS
		self.v5pfes_menu = QMenu(QCoreApplication.translate("v5pfes", "v5PFES"))
		self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.v5pfes_menu)


        # Menu  

		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.chuanhoabd_action = QAction(icon, u'Chuẩn hóa bản đồ DBR', self.iface.mainWindow())
		self.chuanhoabd_action.triggered.connect(self.chuanhoabd)
		self.v5pfes_menu.addAction(self.chuanhoabd_action)

		# --- Menu Build map ---
		self.xaydungbando_DVMTR = QMenu(u'Xây dựng bản đồ DVMTR')		
		self.ifee_add_submenu(self.xaydungbando_DVMTR)

		# Menu Build data structure
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu1 = QAction(icon, u'Xây dựng cấu trúc dữ liệu', self.iface.mainWindow())
		self.congcu1.triggered.connect(self.xaydungCTDL)
		self.xaydungbando_DVMTR.addAction(self.congcu1)

		# Menu Update payment area
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu2 = QAction(icon, u'Cập nhật vùng chi trả', self.iface.mainWindow())
		self.congcu2.triggered.connect(self.capnhatVCT)
		self.xaydungbando_DVMTR.addAction(self.congcu2)

		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu3 = QAction(icon, u'Cập nhật diện tích chi trả', self.iface.mainWindow())
		self.congcu3.triggered.connect(self.capnhatDT)
		self.xaydungbando_DVMTR.addAction(self.congcu3)
        
        # Menu Update Payment forest
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu4 = QAction(icon, u'Cập nhật đối tượng chi trả', self.iface.mainWindow())
		self.congcu4.triggered.connect(self.capnhatDTCT)
		self.xaydungbando_DVMTR.addAction(self.congcu4)
        
        # Menu Update Difficulty Level
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu5 = QAction(icon, u'Cập nhật xã khó khăn', self.iface.mainWindow())
		self.congcu5.triggered.connect(self.capnhatXKK)
		self.xaydungbando_DVMTR.addAction(self.congcu5)
        
        # Menu Update K Coefficient
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu6 = QAction(icon, u'Cập nhật hệ số K', self.iface.mainWindow())
		self.congcu6.triggered.connect(self.capnhatHSK)
		self.xaydungbando_DVMTR.addAction(self.congcu6)
        
        # Menu Calculate Payment
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu7 = QAction(icon, u'Xác định mức chi trả', self.iface.mainWindow())
		self.congcu7.triggered.connect(self.xacdinhMCT)
		self.xaydungbando_DVMTR.addAction(self.congcu7)

		# Menu Manager Database
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.xaydungCSDL_action = QAction(icon, u'Xây dựng cơ sở dữ liệu', self.iface.mainWindow())
		self.xaydungCSDL_action.triggered.connect(self.xaydungCSDL)
		self.v5pfes_menu.addAction(self.xaydungCSDL_action)

		

		# Thêm Menu Statistic
		self.thongkeSL = QMenu(u'Thống kê số liệu')		
		self.ifee_add_submenu(self.thongkeSL)		

		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu1 = QAction(icon, u'Xuất biểu nhóm 1', self.iface.mainWindow())
		self.congcu1.triggered.connect(self.xuatbieuNhom1)
		self.thongkeSL.addAction(self.congcu1)

		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.congcu2 = QAction(icon, u'Xuất biểu nhóm 2', self.iface.mainWindow())
		self.congcu2.triggered.connect(self.xuatbieuNhom2)
		self.thongkeSL.addAction(self.congcu2)
        
        # Menu Help
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.help = QAction(icon, u'Hướng dẫn sử dụng', self.iface.mainWindow())
		self.v5pfes_menu.addAction(self.help)
        
        # Menu About
		icon = QIcon(os.path.dirname(__file__) + "/icons/ifee.png")
		self.about = QAction(icon, u'Giới thiệu', self.iface.mainWindow())
		self.v5pfes_menu.addAction(self.about)
			
	def unload(self):
		if self.v5pfes_menu != None:
			self.iface.mainWindow().menuBar().removeAction(self.v5pfes_menu.menuAction())
		else:
			self.iface.removePluginMenu("&ifee", self.geoprocessing_menu.menuAction())
			self.iface.removePluginMenu("&ifee", self.tool_menu.menuAction())


	##########################
        
	def chuanhoabd(self):
		dialog = ChuanHoaDBR_Dlg(self.iface)
		dialog.exec_()

	def xaydungCTDL(self):
		dialog = XayDungCTDL_Dlg(self.iface)
		dialog.exec_()

	def capnhatVCT(self):
		dialog = CapNhatVCT_Dlg(self.iface)
		dialog.exec_()

	def capnhatDT(self):
		dialog = CapNhatDT_Dlg(self.iface)
		dialog.exec_()

	def capnhatDTCT(self):
		dialog = CapNhatDTCT_Dlg(self.iface)
		dialog.exec_()			

	def capnhatXKK(self):
		dialog = CapNhatXKK_Dlg(self.iface)
		dialog.exec_()		

	def capnhatHSK(self):
		dialog = CapNhatHSK_Dlg(self.iface)
		dialog.exec_()

	def xacdinhMCT(self):
		dialog = XacDinhMCT_Dlg(self.iface)
		dialog.exec_()

	def xaydungCSDL(self):
		dialog = XayDungCSDL_Dlg(self.iface)
		dialog.exec_()	

	def xuatbieuNhom1(self):
		dialog = XuatBieuNhom1_Dlg(self.iface)
		dialog.exec_()

	def xuatbieuNhom2(self):
		dialog = XuatBieuNhom2_Dlg(self.iface)
		dialog.exec_()
