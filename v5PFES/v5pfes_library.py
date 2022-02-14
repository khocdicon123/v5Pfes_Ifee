
import csv
import math
import os.path
import operator
import sys
import re

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
from itertools import groupby

# Initialize Qt resources from file resources.py

# Import the code for the dialog
import os.path
import processing
import pathlib
from pathlib import Path

from qgis.core import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import QgsVectorFileWriter
import qgis.utils
from qgis.utils import iface


def delete_fields(inputPath,outputPath):
    del_fields = ["plot_uuid","desc","change_typ","date_time","area_affec","volume_aff","stems_no_a", "method_pla","density_wo", "density_ba","stems_no_t","stems_no_b","desc_monit", "change_t_1", "ts_created", "ts_modifie","avg_year_c"]
    processing.run('qgis:deletecolumn', {'INPUT':inputPath,'COLUMN':del_fields,'OUTPUT': outputPath})

def add_fields(layer):
    layer.isValid()
    layer_provider = layer.dataProvider()
    layer_provider.addAttributes([QgsField("tt", QVariant.Double,'',7,0),
                            QgsField("id", QVariant.Double,'',7,0),
                            QgsField("tinh", QVariant.String,'',30),
                            QgsField("huyen", QVariant.String,'',30),
                            QgsField("xa", QVariant.String,'',30),
                            QgsField("matinh", QVariant.Double,'',2,0),
                            QgsField("mahuyen", QVariant.Double,'',3,0),
                            QgsField("churung", QVariant.String,'',50),
                            QgsField("nguoink", QVariant.String,'',30),
                            QgsField("nguoirch", QVariant.String,'',30),
                            QgsField("kd", QVariant.Double,'',10,2),
                            QgsField("vd", QVariant.Double,'',11,2),
                            QgsField("capkd", QVariant.Double,'',5,0),
                            QgsField("capvd", QVariant.Double,'',5,0),
                            QgsField("ldlr", QVariant.String,'',5),
                            QgsField("sldlr", QVariant.String,'',30),
                            QgsField("mdsd", QVariant.String,'',4),
                            QgsField("malr3", QVariant.Double,'',2,0),
                            QgsField("captuoi", QVariant.Double,'',2,0)])

def rename_fields(layer):
    old_fields = ['province_c','district_c','commune_co','compt_code','sub_compt_','plot_code','parcel_cod','map_sheet','village','area','forest_org','forest_typ','tree_spec_','planting_y','p_forest_o','plant_stat','volume_per','stem_per_h','volume_p_1','stem_per_p','site_cond_','forest_fun','actor_type','actor_name','actor_id','conflict_s','land_use_c','land_use_t','prot_contr','forest_use','actor_id_p','actor_id_c','nar_for_or','old_plot_c','pos_status']
    new_field = ['matinh','mahuyen','maxa','tk','khoanh','lo','thuad','tobando','ddanh','dtich','nggocr','maldlr','maloaicay','namtr','nggocrt','thanhrung','mgo','mtn','mgolo','mtnlo','lapdia','mamdsd','dtuong','churung','machur','trchap','quyensd','thoihansd','khoan','nqh','mangnk','mangtrch','ngsinh','locu','vitrithua']
    current_field = [x.name() for x in layer.fields()]
    for index, old_field in enumerate(old_fields):
        if old_field in current_field:
            with edit(layer):
                column = layer.fields().indexFromName(old_field)
                layer.renameAttribute(column,new_field[index])


def join_fields(output_Path,churung_Path):

    df_churung = pd.read_excel(churung_Path)
    ds_churung = json.loads(df_churung.to_json(orient='records'))

    with open(str(Path(__file__).parent.absolute()) +"/data/ds_tinhhuyenxa.json", 'r') as myfile:
        data=myfile.read()
    ds_tinhhuyenxa = json.loads(data)

    with open(str(Path(__file__).parent.absolute()) +"/data/ds_loairung.json", 'r') as myfile:
        data=myfile.read()
    ds_loairung = json.loads(data)

    with open(str(Path(__file__).parent.absolute()) +"/data/ds_loaicay.json", 'r') as myfile:
        data=myfile.read()
    ds_loaicay = json.loads(data)

    with open(str(Path(__file__).parent.absolute()) +"/data/ds_mdsd.json", 'r') as myfile:
        data=myfile.read()
    ds_mdsd = json.loads(data)

    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(output_Path, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        maxa = str(feature.GetField("maxa"))
        xa = [x for x in ds_tinhhuyenxa if x['maxa']==maxa]
        if len(xa) >0:
            feature.SetField("xa", xa[0]['xa'])
            feature.SetField("tinh", xa[0]['tinh'])
            feature.SetField("matinh", xa[0]['matinh'])
            feature.SetField("huyen", xa[0]['huyen'])
            feature.SetField("mahuyen", xa[0]['mahuyen'])

        maldlr = str(feature.GetField("maldlr"))
        ldlr = [x for x in ds_loairung if x['maldlr']== maldlr]
        if len(ldlr) >0:
            feature.SetField("ldlr", ldlr[0]['ldlr'])

        maloaicay = str(feature.GetField("maloaicay"))
        sldlr = [x for x in ds_loaicay if x['maloaicay']== maloaicay]

        if len(sldlr) >0:
            feature.SetField("sldlr", sldlr[0]['sldlr'])
            feature.SetField("captuoi", sldlr[0]['captuoi'])

        mamdsd = str(feature.GetField("mamdsd"))
        mdsd = [x for x in ds_mdsd if x['mamdsd']== mamdsd]

        if len(mdsd) > 0:
            feature.SetField("mdsd", mdsd[0]['mdsd'])
            feature.SetField("malr3", mdsd[0]['malr3'])

        machur = feature.GetField("machur")
        maxa = feature.GetField("maxa")

        churung = [x for x in ds_churung if x['commune_code']== maxa and x['actor_id']== machur]
        if len(churung)>0:
            feature.SetField("churung",churung[0]['actor_name'])

        layer.SetFeature(feature)

def update_doituong(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['dtuong'] >= 4 :
            feature.SetField("dtuong", 5)
        layer.SetFeature(feature)

def docdsloaicay():
    ds = str(Path(__file__).parent.absolute()) + '/data/ds_loaicay.json'
    with open(ds) as f1:
        data = json.load(f1)
        return data

def layloaicay(malc):
    dsloai = docdsloaicay()
    dsma = malc.split("+")
    fcay = (dsma)[0]
    for lc in dsloai:
        global floai
        if lc['maloaicay'] == fcay:
            floai = lc['sldlr']
    tenloai = floai
    n=1
    for malc in range (1, len(dsma)):
        spcode = (dsma)[n]
        for lc in dsloai:
            if lc['maloaicay'] == spcode:
                loai = lc['sldlr']
        n=n+1
        tenloai = tenloai + '+' + loai
    return tenloai

def add_newfields(layer, export):
    layer.isValid()
    layer_provider = layer.dataProvider()
    layer_provider.addAttributes([QgsField("vungchitra", QVariant.Double,'',1,0),
                            QgsField("chitra", QVariant.Double,'',1,0),
                            QgsField("dgia", QVariant.Double,'',9,0),
                            QgsField("dtichct", QVariant.Double,'',9,2),
                            QgsField("thanhtien", QVariant.Double,'',9,0),
                            QgsField("k0", QVariant.Double,'',5,4),
                            QgsField("k1", QVariant.Double,'',3,2),
                            QgsField("k2", QVariant.Double,'',3,2),
                            QgsField("k3", QVariant.Double,'',3,2),
                            QgsField("k4", QVariant.Double,'',3,2),
                            QgsField("mucct", QVariant.Double,'',2,0),
                            QgsField("khuvuc", QVariant.Double,'',2,0),
                            QgsField("maluuvuc", QVariant.String,'',30),
                            QgsField("dt2", QVariant.Double,'',9,2)])
    layer.updateFields()

    idx = layer_provider.fieldNameIndex('dt2')

    areas = [ feat.geometry().area()
          for feat in layer.getFeatures() ]

    for area in areas:
        new_values = {idx : float(area)/10000}
        layer_provider.changeAttributeValues({areas.index(area):new_values})

    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "UTF-8", layer.crs(), "ESRI Shapefile")

def convert_json(inputDsLuuvuc):
    # Open the workbook and select the first worksheet
    wb = xlrd.open_workbook(inputDsLuuvuc)
    sh = wb.sheet_by_index(0)
    # List to hold dictionaries
    data_list = []
    # Iterate through each row in worksheet and fetch values into dict
    for rownum in range(1, sh.nrows):
        data = OrderedDict()
        row_values = sh.row_values(rownum)
        data['malv'] = row_values[0]
        data['Tenlv'] = row_values[1]
        data['tongsotien'] = row_values[2]
        data['dgia'] = row_values[3]
        data_list.append(data)
    # Serialize the list of dicts to JSON
    j = json.dumps(data_list,ensure_ascii=False)
    # Write to file
    export = str(Path(__file__).parent.absolute()) + '/data/dsluuvuc.json'
    with open(export, 'w',encoding='utf8') as f:
        f.write(j)

def clip(inputPath,clipPath,outPath):	

    processing.run("native:clip", {"INPUT":inputPath, "OVERLAY":clipPath, "OUTPUT":outPath})

def union(inputPath,overlayPath,outPath):	

    processing.run("qgis:union", {"INPUT":inputPath, "OVERLAY":overlayPath, "OUTPUT":outPath})

def buffer(inputPath,outPath):
    processing.run("native:buffer", {'INPUT':inputPath,
              'DISTANCE': 0.01,
              'SEGMENTS': 5,
              'DISSOLVE': False,
              'END_CAP_STYLE': 0,
              'JOIN_STYLE': 0,
              'MITER_LIMIT': 2,
              'OUTPUT': outPath})

def docdsluuvuc():
    ds = str(Path(__file__).parent.absolute()) + '/data/dsluuvuc.json'
    with open(ds) as f1:
        data = json.load(f1)
        return data

def selectbylocation(inpath,clippath,malv,export):
    layer = QgsVectorLayer(inpath, '', 'ogr')
    QgsProject.instance().addMapLayer(layer)
    processing.run("qgis:selectbylocation", {"INPUT":inpath, "INTERSECT":clippath, "METHOD": 0,"PREDICATE": [6]})

    with edit(layer):
        listOfIds = [feat.id() for feat in layer.getFeatures() if feat['maxa'] == NULL]
        layer.deleteFeatures(listOfIds)
        for feature in layer.getSelectedFeatures():
            feature.setAttribute(feature.fieldNameIndex('vungchitra'),1)
            if feature['maluuvuc'] == NULL :
                feature.setAttribute(feature.fieldNameIndex('maluuvuc'),malv )
            else:
                giatri = feature['maluuvuc']+'+'+malv
                feature.setAttribute(feature.fieldNameIndex('maluuvuc'), giatri)
            layer.updateFeature(feature)
    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "UTF-8", layer.crs(), "ESRI Shapefile")

def update_malv(inpath,malv1,malv2,export):
    layer = QgsVectorLayer(inpath, '', 'ogr')
    QgsProject.instance().addMapLayer(layer)

    with edit(layer):
        for feature in layer.getFeatures():
            maluuvuc = str(feature['maluuvuc']).split('+')
            if  malv1 in maluuvuc :
                giatri = feature['maluuvuc']+'+'+malv2
                feature.setAttribute(feature.fieldNameIndex('maluuvuc'),giatri )
            layer.updateFeature(feature)
    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "UTF-8", layer.crs(), "ESRI Shapefile")

def delete_duplicate_fields(inputPath,outputPath):
    del_fields = ["maxa_2","tk_2","khoanh_2","lo_2","thuad_2","tobando_2","ddanh_2","dtich_2", "nqh_2",
    "mamdsd_2","lapdia_2", "maldlr_2","nggocr_2","ngsinh_2","nggocrt_2", "thanhrung_","maloaicay_","namtr_2", "mgo_2",
    "mgolo_2","mtn_2", "mtnlo_2","machur_2","dtuong_2","quyensd_2", "thoihansd_","trchap_2","mangtrch_2", "khoan_2",
    "mangnk_2","locu_2", "vitrithua_","tt_2","id_2","nguoink_2", "nguoirch_2","kd_2","vd_2", "churung_2",
    "matinh_2","tinh_2", "mahuyen_2","huyen_2","xa_2","ldlr_2", "sldlr_2","captuoi_2","mdsd_2", "malr3_2",
    "vungchit_1", "chitra_2","dgia_2","dtichct_2","thanhtien_","k0_2", "k1_2","k2_2","k3_2", "k4_2",
    "mucct_2", "khuvuc_2","maluuvuc_2","capkd_2","capvd_2","dt2_2"]
    processing.run('qgis:deletecolumn', {'INPUT':inputPath,'COLUMN':del_fields,'OUTPUT': outputPath})

def recalculate_area_1(layer, export):
    layer.isValid()
    layer_provider = layer.dataProvider()
    layer_provider.addAttributes([QgsField("dt3", QVariant.Double,'',9,2)])

    layer.updateFields()
    idx1 = layer_provider.fieldNameIndex('dtich')
    idx3 = layer_provider.fieldNameIndex('dt3')
    idx2 = layer_provider.fieldNameIndex('dt2')

    areas = [ feat.geometry().area()
          for feat in layer.getFeatures() ]

    for area in areas:
        new_values = {idx3 : float(area)/10000}
        layer_provider.changeAttributeValues({areas.index(area):new_values})


    layer.startEditing()
    for feature in layer.getFeatures():
        s1 = feature['dtich']
        s2 = feature['dt2']
        s3 = feature['dt3']
        if s3 == NULL or s2 == NULL or s1 == NULL:
            s4 = 0.00
        elif s2 == 0:
            s4 = 0.00
        else:
            s4 = s3 * s1 / s2

        feature.setAttribute(idx1, s4)
        layer.updateFeature(feature)
    layer.commitChanges()

    res = layer_provider.deleteAttributes([idx2,idx3])
    layer.updateFields()

    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "UTF-8", layer.crs(), "ESRI Shapefile")

def recalculate_area_2(layer, export):
    layer.isValid()
    layer_provider = layer.dataProvider()
    idx1 = layer_provider.fieldNameIndex('dtich')
    idx2 = layer_provider.fieldNameIndex('dt2')

    areas = [ feat.geometry().area()
          for feat in layer.getFeatures() ]

    for area in areas:
        new_values = {idx1 : float(area)/10000}
        layer_provider.changeAttributeValues({areas.index(area):new_values})

    res = layer_provider.deleteAttributes([idx2])
    layer.updateFields()


    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "UTF-8", layer.crs(), "ESRI Shapefile")

def rtn_payment(layer):
    with edit(layer):
        for feature in layer.getFeatures():
            if feature['vungchitra'] ==1 and feature['nggocr']==1:
                feature.setAttribute(feature.fieldNameIndex('chitra'),1)
            layer.updateFeature(feature)

def rtg_payment(layer):
    with edit(layer):
        for feature in layer.getFeatures():
            if feature['vungchitra'] ==1 and feature['maldlr'] >59 and feature['maldlr'] <65:
                feature.setAttribute(feature.fieldNameIndex('chitra'),1)
            layer.updateFeature(feature)

def rttn_payment(layer):
    with edit(layer):
        for feature in layer.getFeatures():
            if feature['vungchitra'] ==1 and feature['maldlr'] >64 and feature['maldlr'] <70:
                feature.setAttribute(feature.fieldNameIndex('chitra'),1)
            layer.updateFeature(feature)

def rtk_payment(layer):
    with edit(layer):
        for feature in layer.getFeatures():
            if feature['vungchitra'] ==1 and feature['maldlr'] >69 and feature['maldlr'] <72:
                feature.setAttribute(feature.fieldNameIndex('chitra'),1)
            layer.updateFeature(feature)

def ctr_payment(layer):
    with edit(layer):
        for feature in layer.getFeatures():
            if feature['vungchitra'] ==1 and feature['maldlr'] >71 and feature['maldlr'] <78:
                feature.setAttribute(feature.fieldNameIndex('chitra'),1)
            layer.updateFeature(feature)

def lc_payment(layer,ds_loaicay,export):
    with edit(layer):
        for feature in layer.getFeatures():
            if feature['sldlr'] in ds_loaicay and feature['chitra'] ==1:
                feature.setAttribute(feature.fieldNameIndex('chitra'),1)
            else:
                feature.setAttribute(feature.fieldNameIndex('chitra'), NULL)

    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "UTF-8", layer.crs(), "ESRI Shapefile")

def lc__non_payment(layer,export):
    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "UTF-8", layer.crs(), "ESRI Shapefile")

def docdsxkk():
    ds = str(Path(__file__).parent.absolute()) + '/data/xakk.json'
    with open(ds) as f1:
        data = json.load(f1)
        return data

def update_xkk(layer,maxa,khuvuc):
    # layer.selectByExpression("'chitra' = 1")
    with edit(layer):
        for feature in layer.getFeatures():
            giatri = str(feature['maxa'])
            if feature['chitra']== 1 and giatri in maxa:
                index = maxa.index(giatri)
                feature.setAttribute(feature.fieldNameIndex('khuvuc'),khuvuc[index])
            layer.updateFeature(feature)

def edit_dsxkk(maxa,khuvuc):
    ds = str(Path(__file__).parent.absolute()) + '/data/xakk.json'
    with open(ds) as f1:
        data = json.load(f1)
        for feat in data:
            if feat['MAXA'] in maxa:
                ind = maxa.index(feat['MAXA'])
                feat['KHUVUC'] = khuvuc[ind]
        j = json.dumps(data, ensure_ascii=False)
        export = str(Path(__file__).parent.absolute()) + '/data/xakk.json'
        with open(export, 'w',encoding='utf8') as f:
            f.write(j)

def join_xkk(inPath):
    with open(str(Path(__file__).parent.absolute()) +"/data/xakk.json", 'r') as myfile:
        data=myfile.read()
    ds_xkk = json.loads(data)

    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1:
            maxa = str(feature.GetField("maxa"))
            xa = [x for x in ds_xkk if x['MAXA']==maxa]
            if len(xa) >0:
                feature.SetField("khuvuc", xa[0]['KHUVUC'])
            layer.SetFeature(feature)

def update_K(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1:
            feature.SetField("k0", 1)
            feature.SetField("k1", 1)
            feature.SetField("k2", 1)
            feature.SetField("k3", 1)
            feature.SetField("k4", 1)
        layer.SetFeature(feature)

def update_K1(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1 :
            if 0<feature['maldlr']<48 or 59<feature['maldlr']<65 or 69<feature['maldlr']<72 or 93<feature['maldlr']<99:
                if feature['mgo']>200:
                    feature.SetField("k1", 1)
                elif 100< feature['mgo'] <=200:
                    feature.SetField("k1", 0.95)
                elif feature['mgo'] <=100:
                    feature.SetField("k1", 0.9)
                else:
                    pass
            elif feature['maldlr']== 48 or feature['maldlr']== 50 or feature['maldlr']== 65 or feature['maldlr']== 66:
                if feature['mtn'] >=3:
                    feature.SetField("k1", 1)
                elif 1<= feature['mtn'] <3:
                    feature.SetField("k1", 0.95)
                elif feature['mtn'] <1:
                    feature.SetField("k1", 0.9)
                else:
                    pass
            elif feature['maldlr']== 49:
                if feature['mtn'] >=8:
                    feature.SetField("k1", 1)
                elif 5<= feature['mtn'] <8:
                    feature.SetField("k1", 0.95)
                elif feature['mtn'] <5:
                    feature.SetField("k1", 0.9)
                else:
                    pass
            elif feature['maldlr']== 51:
                if feature['mtn'] >=4:
                    feature.SetField("k1", 1)
                elif 2<= feature['mtn'] <4:
                    feature.SetField("k1", 0.95)
                elif feature['mtn'] <2:
                    feature.SetField("k1", 0.9)
                else:
                    pass
            elif feature['maldlr']== 52:
                if feature['mtn'] >=10:
                    feature.SetField("k1", 1)
                elif 6<= feature['mtn'] <10:
                    feature.SetField("k1", 0.95)
                elif feature['mtn'] <6:
                    feature.SetField("k1", 0.9)
                else:
                    pass
            elif feature['maldlr']== 53:
                if feature['mtn'] >=6:
                    feature.SetField("k1", 1)
                elif 3<= feature['mtn'] <6:
                    feature.SetField("k1", 0.95)
                elif feature['mtn'] <3:
                    feature.SetField("k1", 0.9)
                else:
                    pass
            elif 53 <feature['maldlr']< 60 or 66 <feature['maldlr']< 70 or 71 <feature['maldlr']< 78:
                feature.SetField("k1", 0.9)
            else:
                pass
        layer.SetFeature(feature)

def update_K1_uncheck(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1:
            feature.SetField("k1", 1)
        layer.SetFeature(feature)

def update_K2(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1 :
            if feature['malr3']== 2:
                feature.SetField("k2", 1)
            elif feature['malr3']== 1:
                feature.SetField("k2", 0.95)
            elif feature['malr3']== 3 or feature['malr3']== 0 or feature['malr3']== NULL:
                feature.SetField("k2", 0.9)
            else:
                pass
        layer.SetFeature(feature)

def update_K2_uncheck(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1:
            feature.SetField("k2", 1)
        layer.SetFeature(feature)

def update_K3(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1 :
            if feature['nggocr']== 1:
                feature.SetField("k3", 1)
            elif feature['nggocr']== 2 or feature['nggocr']== 3:
                feature.SetField("k3", 0.9)
            else:
                pass
        layer.SetFeature(feature)

def update_K3_uncheck(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1:
            feature.SetField("k3", 1)
        layer.SetFeature(feature)

def update_K4(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1 :
            if feature['khuvuc']== 3:
                feature.SetField("k4", 1)
            elif feature['khuvuc']== 2:
                feature.SetField("k4", 0.95)
            elif feature['khuvuc']== 1:
                feature.SetField("k4", 0.9)
            else:
                pass
        layer.SetFeature(feature)

def update_K4_uncheck(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1:
            feature.SetField("k4", 1)
        layer.SetFeature(feature)

def update_K0(inPath):
    shp =  QgsVectorLayer(inPath, '', 'ogr')
    layer = QgsProject.instance().addMapLayer(shp)

    exp = QgsExpression('"k1"*"k2"*"k3"*"k4"')
    context = QgsExpressionContext()
    context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

    with edit(layer):
        for feature in layer.getFeatures():
            context.setFeature(feature)
            if feature['chitra']== 1:
                feature['k0'] = exp.evaluate(context)
            layer.updateFeature(feature)

def payment_area(inPath):
    shp =  QgsVectorLayer(inPath, '', 'ogr')
    layer = QgsProject.instance().addMapLayer(shp)

    exp = QgsExpression('"dtich"*"k0"')
    context = QgsExpressionContext()
    context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

    with edit(layer):
        for feature in layer.getFeatures():
            context.setFeature(feature)
            if feature['k0']> 0:
                feature['dtichct'] = exp.evaluate(context)
            layer.updateFeature(feature)

def price(inPath):
    with open(str(Path(__file__).parent.absolute()) +"/data/dsluuvuc.json", 'r') as myfile:
        data=myfile.read()
    ds_dongia = json.loads(data)

    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()
    listmlv = []
    listdg = []
    for feat in ds_dongia:
        listmlv.append(feat['malv'])
        listdg.append(feat['dgia'])

    for feature in layer:
        if feature['chitra']== 1:
            malv = feature.GetField("maluuvuc").split('+')
            dongia = 0
            for x in malv:
                ind = listmlv.index(int(x))
                dongia = dongia + listdg[ind]
            feature.SetField("dgia", dongia)
            layer.SetFeature(feature)

def payment_level(inPath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(inPath, 1)
    layer = dataSource.GetLayer()

    for feature in layer:
        if feature['chitra']== 1 :
            if feature['dgia']<= 50000:
                feature.SetField("mucct", 1)
            elif 50000<feature['dgia']<= 100000:
                feature.SetField("mucct", 2)
            elif 100000<feature['dgia']<= 150000:
                feature.SetField("mucct", 3)
            elif 150000<feature['dgia']<= 200000:
                feature.SetField("mucct", 4)
            elif 200000<feature['dgia']<= 300000:
                feature.SetField("mucct", 5)
            elif 300000<feature['dgia']<= 500000:
                feature.SetField("mucct", 6)
            elif feature['dgia']> 500000:
                feature.SetField("mucct", 7)
            else:
                pass
        layer.SetFeature(feature)

def export_THX(inPath, export):
    df = pd.read_excel(inPath)
    df = df.loc[(df['chitra'] == 1)]
    df = df.loc[:, ['matinh','tinh','mahuyen','huyen','maxa','xa']]
    df.drop_duplicates(subset=['maxa'], keep='first', inplace=True)
    df.to_json(export, orient='records')

    with open(export) as f1:
        data = json.load(f1)
        j = json.dumps(data, ensure_ascii=False)
        with open(export, 'w',encoding='utf8') as f:
            f.write(j)

def export_ChuRung(inPath, export):
    df = pd.read_excel(inPath)
    df = df.loc[(df['chitra'] == 1) & (df['dtuong'] == 5)]
    df = df.loc[:, ['matinh','tinh','machur','churung']]
    df.drop_duplicates(subset=['machur'], keep='first', inplace=True)
    df.to_json(export, orient='records')

    with open(export) as f1:
        data = json.load(f1)
        j = json.dumps(data, ensure_ascii=False)
        with open(export, 'w',encoding='utf8') as f:
            f.write(j)

def get_ma_xa(tinh,huyen,xa):
    pathTHX = str(Path(__file__).parent.absolute()) + '/tempo/THX.json'
    df = pd.read_json (pathTHX)
    maxa = df[(df['tinh'] == tinh) & (df['huyen']== huyen)&( df['xa']== xa)]['maxa'].iloc[0]
    return maxa

def get_maChuRung(churung):
    pathTHX = str(Path(__file__).parent.absolute()) + '/tempo/ChuRung.json'
    df = pd.read_json (pathTHX)
    machurung = df[( df['churung']== churung)]['machur'].iloc[0]
    return machurung

def report_comumune(df,maxa,output):
    dtuong_header = [['I','TÊN HỘ GIA ĐÌNH, CÁ NHÂN'],['II','TÊN CỘNG ĐỒNG DÂN CƯ'],['III','ỦY BAN NHÂN DÂN XÃ'],['IV','TÊN TỔ CHỨC KHÁC ĐƯỢC NHÀ NƯỚC GIAO TRÁCH NHIỆM QUẢN LÝ RỪNG']]
    df_group = df.groupby(['maxa','dtuong'])
    df_doituong = df[df['maxa']==maxa]
    ds_dtuong_temp = df_doituong['dtuong'].unique().tolist()
    ds_dtuong = sorted(list(filter(lambda x: x > 0 and x < 5, ds_dtuong_temp)))

    def tinh_doituong(df_con):
        out = df_con.groupby(['churung']).apply(lambda sub_df: sub_df.pivot_table(
            index=['dtuong', 'churung', 'lo', 'khoanh', 'tk','ddanh', 'k0', 'k1', 'k2', 'k3', 'k4'],
            values=['dtich', 'dtichct'],
            aggfunc={'dtich': np.sum, 'dtichct': np.sum},
            fill_value=0,
            margins=True,
            margins_name='Tổng'))
        out.index = out.index.droplevel(0)
        return out

    # Tạo file tạm và trường dữ liệu
    temp = QgsVectorLayer("none","result","memory")
    temp_data = temp.dataProvider()
    temp.startEditing()

    myheader = ['TT','Bên cung ứng DVMTR','Lô','Khoảnh','Tiểu khu','Tên địa phương(Nếu có)','Diện tích cung ứng DVMTR (ha)','Hệ số K','K1','K2','K3','K4','Diện tích được chi trả tiền DVMTR (ha)']

    myField = QgsField( 'ID', QVariant.Double)
    temp.addAttribute(myField)

    for head in myheader :
        myField = QgsField( head, QVariant.String )
        temp.addAttribute(myField)
    temp.updateFields()
    # Xong tạo file tạm
    # Một số biến tạm để đếm
    row_id = 0
    thutu = 0
    name = ''
    i = 0
    total_cungung = 0
    total_ct = 0

    for index,dtuong  in enumerate(ds_dtuong):

        row_id = row_id +1
        f = QgsFeature()
        f.setAttributes([row_id,dtuong_header[index][0],dtuong_header[index][1],'','','','','','','','','','',''])
        temp.addFeature(f)


        df_doituong_con = df_group.get_group((maxa,dtuong))
        doituongX = tinh_doituong(df_doituong_con)

        for row in doituongX.itertuples():
            row_id = row_id +1

            dtich_cung_ung = str(round(float(row[1]),2))
            dtich_ct = str(round(float(row[2]),2))

            if len(str(row[0][1])) == 0:
                cot3 = 'Cộng'
                total_cungung = total_cungung +float(row[1])
                total_ct = total_cungung +float(row[2])
            else:
                cot3 = row[0][1]
                if row[0][1] != name:
                    thutu = thutu+1
                    name =  row[0][1]

            fet = QgsFeature()
            fet.setAttributes([row_id,thutu, cot3, row[0][2],row[0][3],row[0][4],row[0][5],dtich_cung_ung,row[0][6],row[0][7],row[0][8],row[0][9], row[0][10],dtich_ct])
            temp.addFeature(fet)

    row_id = row_id +1
    f = QgsFeature()
    f.setAttributes([row_id,'','Tổng','','','','',str(round(total_cungung,2)),'','','','','',str(round(total_ct,2))])
    temp.addFeature(f)

    temp.deleteAttributes([0])
    temp.updateFields()
    temp.commitChanges()
    QgsProject.instance().addMapLayer(temp)
    layer = iface.activeLayer()
    QgsVectorFileWriter.writeAsVectorFormat(layer, output , "", layer.crs(), 'xlsx')


def hanhchinh_export(inPath,maxa,export):
    df = pd.read_excel(inPath)
    df = df.loc[(df['dgia'] > 0)]
    df = df.loc[(df['maxa'] == maxa)]
    df =df.loc[:, ['xa','huyen','tinh']]
    df.drop_duplicates(subset=['xa'], keep='first', inplace=True)

    temp = QgsVectorLayer("none","result","memory")
    temp_data = temp.dataProvider()
    temp.startEditing()
    myheader = ['Churung']

    for head in myheader :
        myField = QgsField( head, QVariant.String )
        temp.addAttribute(myField)
    temp.updateFields()

    for df in df.itertuples():
        f = QgsFeature()
        f.setAttributes([df[1] + '-' + df[2]+ '-' +df[3]])
        temp.addFeature(f)
    temp.commitChanges()
    QgsProject.instance().addMapLayer(temp)

    layer = iface.activeLayer()
    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "utf-8", layer.crs(), 'xlsx')

def tinh_export(inPath,maxa,export):
    df = pd.read_excel(inPath)
    df = df.loc[(df['dgia'] > 0)]
    df = df.loc[(df['maxa'] == maxa)]
    df =df.loc[:, ['xa','huyen','tinh']]
    df.drop_duplicates(subset=['xa'], keep='first', inplace=True)

    temp = QgsVectorLayer("none","result","memory")
    temp_data = temp.dataProvider()
    temp.startEditing()
    myheader = ['tinh']

    for head in myheader :
        myField = QgsField( head, QVariant.String )
        temp.addAttribute(myField)
    temp.updateFields()

    for df in df.itertuples():
        f = QgsFeature()
        f.setAttributes([df[3]])
        temp.addFeature(f)
    temp.commitChanges()
    QgsProject.instance().addMapLayer(temp)

    layer = iface.activeLayer()
    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "utf-8", layer.crs(), 'xlsx')

def xa_export(inPath,maxa,export):
    df = pd.read_excel(inPath)
    df = df.loc[(df['dgia'] > 0)]
    df = df.loc[(df['maxa'] == maxa)]
    df =df.loc[:, ['xa']]
    df.drop_duplicates(subset=['xa'], keep='first', inplace=True)

    temp = QgsVectorLayer("none","result","memory")
    temp_data = temp.dataProvider()
    temp.startEditing()
    myheader = ['xa']

    for head in myheader :
        myField = QgsField( head, QVariant.String )
        temp.addAttribute(myField)
    temp.updateFields()

    for df in df.itertuples():
        f = QgsFeature()
        f.setAttributes([df[1]])
        temp.addFeature(f)
    temp.commitChanges()
    QgsProject.instance().addMapLayer(temp)

    layer = iface.activeLayer()
    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "utf-8", layer.crs(), 'xlsx')

def convert_TVKD(text):
    patterns = {
        '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
        '[ÀÁẢÃẠĂẮẰẴẶẲÂẦẤẬẪẨ]' : 'A',
        '[đ]': 'd',
        '[Đ]': 'D',
        '[èéẻẽẹêềếểễệ]': 'e',
        '[ÈÉẺẼẸÊỀẾỂỄỆ]':'E',
        '[ìíỉĩị]': 'i',
        '[ÌÍỈĨỊ]': 'I',
        '[ÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢ]': 'O',
        '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
        '[ùúủũụưừứửữự]': 'u',
        '[ÙÚỦŨỤƯỪỨỬỮỰ]': 'U',
        '[ỳýỷỹỵ]': 'y',
        '[ỲÝỶỸỴ]': 'Y',
        '[`~@#$%^&*-<>?/\!-+!"]': '_',
        '[ ]' : ''
    }
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output

def report_forestActor(df,outputpath):
    def tinh_doituong(df_con):
        out = df_con.pivot_table(
            index=['lo', 'khoanh', 'tk', 'k0', 'k1', 'k2', 'k3', 'k4'],
            values=['dtich', 'dtichct'],
            aggfunc={'dtich': np.sum, 'dtichct': np.sum},
            fill_value=0,
            margins=True,
            margins_name='Tổng')
        return out
    # Tạo file tạm và trường dữ liệu
    temp = QgsVectorLayer("none","result","memory")
    temp_data = temp.dataProvider()
    temp.startEditing()

    myheader = ['TT','Lô','Khoảnh','Tiểu khu','Diện tích cung ứng DVMTR (ha)','Hệ số K','K1','K2','K3','K4','Diện tích được chi trả tiền DVMTR (ha)']
    myField = QgsField( 'ID', QVariant.Double)
    temp.addAttribute(myField)

    for head in myheader : 
        myField = QgsField( head, QVariant.String )
        temp.addAttribute(myField)
    temp.updateFields()

    # Một số biến tạm để đếm
    row_id = 0
    thutu = 0
    name = ''
    total_cungung = 0
    total_ct = 0
    
    doituongX = tinh_doituong(df)
    for row in doituongX.itertuples():    
        row_id = row_id +1
        dtich_cung_ung = str(round(float(row[1]),2))
        dtich_ct = str(round(float(row[2]),2))
        thutu = thutu+1        
        lo = row[0][0]        
        if row[0][0] == 'Tổng':
            lo = 'Tổng'

        fet = QgsFeature()
        fet.setAttributes([row_id,thutu,lo,row[0][1],row[0][2],dtich_cung_ung,row[0][3],row[0][4],row[0][5],row[0][6],row[0][7],dtich_ct])
        temp.addFeature(fet)

    temp.deleteAttributes([0])
    temp.updateFields()
    temp.commitChanges()
    QgsProject.instance().addMapLayer(temp)
    layer = iface.activeLayer()
    QgsVectorFileWriter.writeAsVectorFormat(layer, outputpath , "", layer.crs(), 'xlsx')
def report_cr(df,output):
    #dtuong_header = [['I','TÊN HỘ GIA ĐÌNH, CÁ NHÂN'],['II','TÊN CỘNG ĐỒNG DÂN CƯ'],['III','ỦY BAN NHÂN DÂN XÃ'],['IV','TÊN TỔ CHỨC KHÁC ĐƯỢC NHÀ NƯỚC GIAO TRÁCH NHIỆM QUẢN LÝ RỪNG']]
    #df_group = df.groupby(['maxa','dtuong'])
    #df_doituong = df[df['macr'] == macr]
    #ds_dtuong_temp = df_doituong['dtuong'].unique().tolist()
    #ds_dtuong = sorted(list(filter(lambda x: x = 5, ds_dtuong_temp)))

    def tinh_doituong(df_con):
        out = df_con.groupby(['churung']).apply(lambda sub_df: sub_df.pivot_table(
            index=['tt', 'lo', 'khoanh', 'tk', 'k0', 'k1', 'k2', 'k3', 'k4'],
            values=['dtich', 'dtichct'],
            aggfunc={'dtich': np.sum, 'dtichct': np.sum},
            fill_value=0,
            margins=True,
            margins_name='Tổng'))
        out.index = out.index.droplevel(0)
        return out

    # Tạo file tạm và trường dữ liệu
    temp = QgsVectorLayer("none","result","memory")
    temp_data = temp.dataProvider()
    temp.startEditing()

    myheader = ['TT','Lô','Khoảnh','Tiểu khu','Diện tích cung ứng DVMTR (ha)','Hệ số K','K1','K2','K3','K4','Diện tích được chi trả tiền DVMTR (ha)']

    myField = QgsField( 'ID', QVariant.Double)
    temp.addAttribute(myField)

    for head in myheader :
        myField = QgsField( head, QVariant.String )
        temp.addAttribute(myField)
    temp.updateFields()
    # Xong tạo file tạm
    # Một số biến tạm để đếm
    row_id = 0
    thutu = 0
    name = ''
    i = 0
    total_cungung = 0
    total_ct = 0

    #for index,dtuong  in enumerate(ds_dtuong):

        #row_id = row_id +1
        #f = QgsFeature()
        #f.setAttributes([row_id,dtuong_header[index][0],dtuong_header[index][1],'','','','','','','','','','',''])
        #temp.addFeature(f)


        #df_doituong_con = df_group.get_group((maxa,dtuong))
        #doituongX = tinh_doituong(df_doituong_con)

    for row in doituongX.itertuples():
        row_id = row_id +1

        dtich_cung_ung = str(round(float(row[1]),2))
        dtich_ct = str(round(float(row[2]),2))

        if len(str(row[0][1])) == 0:
            cot3 = 'Cộng'
            total_cungung = total_cungung +float(row[1])
            total_ct = total_cungung +float(row[2])
        else:
            cot3 = row[0][1]
            if row[0][1] != name:
                thutu = thutu+1
                name =  row[0][1]

        fet = QgsFeature()
        fet.setAttributes([row_id,cot3, row[0][2],row[0][3],row[0][4],dtich_cung_ung,row[0][5],row[0][6],row[0][7],row[0][8], row[0][9],dtich_ct])
        temp.addFeature(fet)


    f = QgsFeature()
    f.setAttributes([row_id,'','Tổng','','','','',str(round(total_cungung,2)),'','','','','',str(round(total_ct,2))])
    temp.addFeature(f)

    temp.deleteAttributes([0])
    temp.updateFields()
    temp.commitChanges()
    QgsProject.instance().addMapLayer(temp)
    layer = iface.activeLayer()
    QgsVectorFileWriter.writeAsVectorFormat(layer, output , "", layer.crs(), 'xlsx')


def churung_export(inPath,machurung,export):
    df = pd.read_excel(inPath)
    df = df.loc[(df['dgia'] > 0)]
    df = df.loc[(df['machur'] == machurung)]
    df =df.loc[:, ['churung']]
    df.drop_duplicates(subset=['churung'], keep='first', inplace=True)

    temp = QgsVectorLayer("none","result","memory")
    temp_data = temp.dataProvider()
    temp.startEditing()
    myheader = ['Churung']

    for head in myheader :
        myField = QgsField( head, QVariant.String )
        temp.addAttribute(myField)
    temp.updateFields()

    for df in df.itertuples():
        f = QgsFeature()
        f.setAttributes([df[1]])
        temp.addFeature(f)
    temp.commitChanges()
    QgsProject.instance().addMapLayer(temp)

    layer = iface.activeLayer()
    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "utf-8", layer.crs(), 'xlsx')

def province_export(inPath,machurung,export):
    df = pd.read_excel(inPath)
    df = df.loc[(df['dgia'] > 0)]
    df = df.loc[(df['machur'] == machurung)]
    df =df.loc[:, ['tinh']]
    df.drop_duplicates(subset=['tinh'], keep='first', inplace=True)

    temp = QgsVectorLayer("none","result","memory")
    temp_data = temp.dataProvider()
    temp.startEditing()
    myheader = ['tinh']

    for head in myheader :
        myField = QgsField( head, QVariant.String )
        temp.addAttribute(myField)
    temp.updateFields()

    for df in df.itertuples():
        f = QgsFeature()
        f.setAttributes([df[1]])
        temp.addFeature(f)
    temp.commitChanges()
    QgsProject.instance().addMapLayer(temp)

    layer = iface.activeLayer()
    QgsVectorFileWriter.writeAsVectorFormat(layer, export, "utf-8", layer.crs(), 'xlsx')
def docds():
    dir = str(Path(__file__).parent.absolute()) + '/tempo/ChuRung.json'
    with open(dir) as f:
        datax = json.load(f)
        return datax
