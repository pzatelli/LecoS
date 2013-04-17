# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LecoS
                                 A QGIS plugin
 Contains analytical functions for landscape analysis
                              -------------------
        begin                : 2012-09-06
        copyright            : (C) 2013 by Martin Jung
        email                : martinjung@zoho.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import PyQT bindings
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Import QGIS analysis tools
from qgis.core import *
from qgis.gui import *
from qgis.analysis import *

# Import base libraries
import os,sys,csv,string,math,operator,subprocess,tempfile,inspect

# Try to import functions from osgeo
try:
    from osgeo import gdal
except ImportError:
    import gdal
try:
    from osgeo import ogr
except ImportError:
    import ogr

# Register gdal and ogr drivers
if hasattr(gdal,"AllRegister"): # Can register drivers
    gdal.AllRegister() # register all gdal drivers
if hasattr(ogr,"RegisterAll"):
    ogr.RegisterAll() # register all ogr drivers

## CODE START ##
# Save results to CSV
def saveToCSV( results, titles, filePath ):
  f = open(filePath, "wb" )
  writer = csv.writer(f,delimiter=';',quotechar="'",quoting=csv.QUOTE_ALL)
  writer.writerow(titles)
  for item in results:
    writer.writerow(item)
  f.close()

# Displays results in a table Dialog
def ShowResultTableDialog( metric_names, results ):
  dlg = QDialog()
  dlg.setWindowTitle( QApplication.translate( "Landcover statistics", "Landcover statistics", "Window title" ) )
  dlg.resize(700, 200)
  # Size Policy
  sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
  sizePolicy.setHorizontalStretch(0)
  sizePolicy.setVerticalStretch(0)
  sizePolicy.setHeightForWidth(dlg.sizePolicy().hasHeightForWidth())
  dlg.setSizePolicy(sizePolicy)

  lines = QVBoxLayout( dlg )
  
  rowCount = len(results)
  colCount = len(metric_names)
  tableWidget = QTableWidget()
  tableWidget.setRowCount(rowCount)
  tableWidget.setColumnCount(colCount)
  tableWidget.setHorizontalHeaderLabels(metric_names) # add header
  tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
  tableWidget.resizeColumnsToContents()
  
  for id, item in enumerate(results):
    for place, value in enumerate(item):
      newItem = QTableWidgetItem(unicode(value))
      tableWidget.setItem(id,place,newItem)

  lines.addWidget(tableWidget)

  btnClose = QPushButton( QApplication.translate( "OK", "OK" ) )
  lines.addWidget( btnClose )
  QObject.connect( btnClose, SIGNAL( "clicked()" ), dlg, SLOT( "close()" ) )
  dlg.exec_()

# Version number 2 for nested metrics and features
def ShowResultTableDialog2( metric_names, results ):
  dlg = QDialog()
  dlg.setWindowTitle( QApplication.translate( "Landcover statistics", "Landcover statistics", "Window title" ) )
  dlg.resize(700, 700)
  # Size Policy
  sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
  sizePolicy.setHorizontalStretch(0)
  sizePolicy.setVerticalStretch(0)
  sizePolicy.setHeightForWidth(dlg.sizePolicy().hasHeightForWidth())
  dlg.setSizePolicy(sizePolicy)

  lines = QVBoxLayout( dlg )
  
  rowCount = len(results[0])
  colCount = len(metric_names)
  tableWidget = QTableWidget()
  tableWidget.setRowCount(rowCount)
  tableWidget.setColumnCount(colCount)
  tableWidget.setHorizontalHeaderLabels(metric_names) # add header
  tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
  tableWidget.resizeColumnsToContents()
  
  for id, item in enumerate(results):
    for place, value in enumerate(item):
      idItem = QTableWidgetItem(unicode(value[0]))
      tableWidget.setItem(place,0,idItem)
      newItem = QTableWidgetItem(unicode(value[2]))
      tableWidget.setItem(place,id+1,newItem)

  lines.addWidget(tableWidget)

  btnClose = QPushButton( QApplication.translate( "OK", "OK" ) )
  lines.addWidget( btnClose )
  QObject.connect( btnClose, SIGNAL( "clicked()" ), dlg, SLOT( "close()" ) )
  dlg.exec_()
  return True


# Shows the about dialog
def AboutDlg( ):
  dlgAbout = QDialog()
  dlgAbout.setWindowTitle( QApplication.translate( "Landcover statistics", "About LecoS", "Window title" ) )
  lines = QVBoxLayout( dlgAbout )
  title = QLabel( QApplication.translate( "LecoS", "<b>LecoS</b>" ) )
  title.setAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
  lines.addWidget( title )
  lines.addWidget( QLabel( QApplication.translate( "LecoS", "Contains analytical functions for landscape analysis" ) ) )
  lines.addWidget( QLabel( QApplication.translate( "LecoS", "<b>Disclaimer:</b>" ) ) )
  text = "This piece of software comes as it is.<br> The developer takes no responsiblity for any miscalcultions or errors in the code.<br> Users are encouraged to use their brain to validate any returned results."
  lines.addWidget( QLabel( text ) )
  lines.addWidget( QLabel( QApplication.translate( "LecoS", "<b>Developer:</b>" ) ) )
  lines.addWidget( QLabel( "Martin Jung" ) )
  lines.addWidget( QLabel( QApplication.translate( "LecoS", "<b>Homepage:</b>") ) )

  link = QLabel( "<a href=\"http://conservationecology.wordpress.com\">http://conservationecology.wordpress.com</a>" )

  link.setOpenExternalLinks( True )
  lines.addWidget( link )
  # Citation
  lines.addWidget( QLabel( QApplication.translate( "LecoS", "<b>Citation:</b>") ) )
  cit = QLineEdit()
  cit.setText("Martin Jung, 2012, LecoS - A QGIS plugin to conduct landscape ecology statistics, http://plugins.qgis.org/plugins/LecoS/")
  lines.addWidget( cit )
  # Supported by
  lines.addWidget( QLabel( QApplication.translate( "LecoS", "<b>Supported by:</b>") ) )
  sup = QLabel( QApplication.translate( "LecoS", "<p>Universidade de &#201;vora, Departamento de Biologia, Unidade de Biologia da Conserva&#231;&#479;o</p>" ) )
  sup.setWordWrap(True)
  lines.addWidget( sup )
  Pic = QLabel()
  Pic.setPixmap(QPixmap(":/pics/icons/evora_small.jpg"))
  lines.addWidget(Pic)

  btnClose = QPushButton( QApplication.translate( "LecoS", "Close" ) )
  lines.addWidget( btnClose )
  QObject.connect( btnClose, SIGNAL( "clicked()" ), dlgAbout, SLOT( "close()" ) )

  dlgAbout.exec_()

# Adapted from Plugin ZonalStats - Copyright (C) 2011 Alexander Bruy
def lastUsedDir():
  settings = QSettings( "Lecoto", "lecos" )
  return settings.value( "lastUsedDir", QVariant( "" ) ).toString()

# Adapted from Plugin ZonalStats - Copyright (C) 2011 Alexander Bruy
def setLastUsedDir( lastDir ):
  path = QFileInfo( lastDir ).absolutePath()
  settings = QSettings( "Lecoto", "lecos" )
  settings.setValue( "lastUsedDir", QVariant( path ) )
  
# Adapted from Plugin ZonalStats - Copyright (C) 2011 Alexander Bruy
def getRasterLayerByName( layerName ):
  layerMap = QgsMapLayerRegistry.instance().mapLayers()
  for name, layer in layerMap.iteritems():
    if layer.type() == QgsMapLayer.RasterLayer and ( layer.providerType() == 'gdal' ) and layer.name() == layerName:
        if layer.isValid():
          return layer
        else:
          return None
          
# Adapted from Plugin ZonalStats - Copyright (C) 2011 Alexander Bruy
def getRasterLayersNames():
  layerList = []
  layerMap = QgsMapLayerRegistry.instance().mapLayers()
  for name, layer in layerMap.iteritems():
    if layer.type() == QgsMapLayer.RasterLayer and ( layer.providerType() == 'gdal' ):
        layerList.append( unicode( layer.name() ) )
  return layerList

# Adapted from Plugin ZonalStats - Copyright (C) 2011 Alexander Bruy
def getVectorLayerByName( layerName ):
  layerMap = QgsMapLayerRegistry.instance().mapLayers()
  for name, layer in layerMap.iteritems():
    if layer.type() == QgsMapLayer.VectorLayer and layer.name() == layerName:
      if layer.isValid():
        return layer
      else:
        return None
  
# Adapted from Plugin ZonalStats - Copyright (C) 2011 Alexander Bruy
def getVectorLayersNames():
  layerList = []
  layerMap = QgsMapLayerRegistry.instance().mapLayers()
  for name, layer in layerMap.iteritems():
    if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == QGis.Polygon:
      layerList.append( unicode( layer.name() ) )
  return layerList

# Adapted from Plugin ZonalStats - Copyright (C) 2011 Alexander Bruy
def getFieldList( vLayer ):
  vProvider = vLayer.dataProvider()
  return vProvider.fields()

# Get all field values of a given attribute from a vector layer
def getAttributeList( vlayer, field):
  path = vlayer.source()
  datasource = ogr.Open(str(path))
  layer = datasource.GetLayer(0)
  layerName = layer.GetName()
  try:
    d = datasource.ExecuteSQL("SELECT DISTINCT %s FROM %s" %(field,layerName))
  except RuntimeError:
    QMessageBox.warning(QDialog(),"LecoS: Warning","Failed to query the vector layers attribute table")
    return
  attr = []
  for i in range(0,d.GetFeatureCount()):
    f = d.GetFeature(i)
    attr.append(f.GetField(0))
  return attr
  
# General function to retrieve layers
def getLayerByName( layerName ):
  layerMap = QgsMapLayerRegistry.instance().mapLayers()
  for name, layer in layerMap.iteritems():
    if layer.name() == layerName:
        if layer.isValid():
          return layer
        else:
          return None


# Add a new attribute to the vectorlayer
# Expected input: Array with [ID,Value]
def addAttributesToLayer(layer,cmd,results,type="qgis"):
  if type == "qgis":
    # Open a Shapefile, and get field names
    provider = layer.dataProvider()
    allAttrs = provider.attributeIndexes()
    if hasattr(provider,"select"): # Worked before, maybe necessary in the future again
      provider.select(allAttrs)
    caps = provider.capabilities()
  
    name = cmd #"".join(e[0] for e in cmd.split()) + "_"
    # Create Attribute Column
    ind = provider.fieldNameIndex(name)
    try:
      if ind == -1:
        if caps & QgsVectorDataProvider.AddAttributes:
          res = provider.addAttributes( [ QgsField(name,QVariant.Double) ] )
    except:
      return False
    ind = provider.fieldNameIndex(name)
    # Write values to newly created coloumn or to existing one
    try:
      for ar in results:
        if caps & QgsVectorDataProvider.ChangeAttributeValues:
          attrs = { ind : QVariant(round(ar[1],6)) }
          provider.changeAttributeValues({ ar[0] : attrs })
    except:
      return False
    layer.commitChanges()
    return True
  elif type == "gdal":
    # Write attributes to table using GDAL #
    path = layer.source()
    vector = ogr.Open(str(path)) # Get layer
    if not vector:
      QMessageBox.warning(QDialog(),"Could not open vector file. Check permissions!")
      return False
    layer = vector.GetLayer()
    # Get fieldDefinitions from featureDefinition
    featureDefinition = layer.GetLayerDefn()
    fieldIndices = xrange(featureDefinition.GetFieldCount())
    fieldDefinitions = []
    for fieldIndex in fieldIndices:
        fieldDefinition = featureDefinition.GetFieldDefn(fieldIndex)
        fieldDefinitions.append((fieldDefinition.GetName(), fieldDefinition.GetType()))
    
    field_name = ogr.FieldDefn(cmd, ogr.OFTReal)
    field_name.SetWidth(24)
    layer.CreateField(field_name)
    for fid in range(0,len(results)):
      feature = layer.GetFeature(fid)
      feature.SetField(cmd,results[fid][1])
      feature.Destroy()
    layer.SyncToDisk()
    vector.Destroy()
    

# Special Function for Metric outputs
# Save multiple different attributes to vector table
# Input = [[[ID,METRIC,VAL],[ID,METRIC,VAL]],[[ID,METRIC,VAL2],[ID,METRIC,VAL2]]]
def addAttributesToLayer2(layer,results):
  # Open a Shapefile, and get field names
  layer.startEditing() # start editing
  provider = layer.dataProvider()
  if hasattr(provider,"select"): # Worked before, maybe necessary in the future again
    allAttrs = provider.attributeIndexes()
    provider.select(allAttrs)
  caps = provider.capabilities()
  for metric in xrange(0,len(results)):
    # Create Attribute Column
    # Name Formating
    cmd = str( results[metric][0][1] )
    cmd = string.capwords(cmd)
    cmd = string.split(cmd)
    name = ""
    for i in range(0,len(cmd)):
      name = name + cmd[i][0:3]
    name = name[0:9] # Make sure only 10 character are Inside the Name
     
    ind = provider.fieldNameIndex(name)
    try:
      if ind == -1:
        if caps & QgsVectorDataProvider.AddAttributes:
          res = provider.addAttributes( [ QgsField(name,QVariant.Double) ] )
    except:
      return False
    ind = provider.fieldNameIndex(name)
    
    # Write values to newly created coloumn or to existing one
    for ar in results[metric]:
      if caps & QgsVectorDataProvider.ChangeAttributeValues:
        attrs = { ind : QVariant(round(ar[2],6)) }
        provider.changeAttributeValues({ ar[0] : attrs })
  
  layer.commitChanges()
  return True

  
    
# Save a rasterfile as geotiff to a given directory
# Need the previous raster (for output size and projection)
# and a path with writing permissions
def exportRaster(array,rasterSource,path):
  raster = gdal.Open(str(rasterSource))
  rows = raster.RasterYSize
  cols = raster.RasterXSize
  nodata = 0#raster.GetRasterBand(1).GetNoDataValue()
  
  driver = gdal.GetDriverByName('GTiff')
  # Create File based in path
  outDs = driver.Create(path, cols, rows, 1, gdal.GDT_Float32)
  if outDs is None:
      QMessageBox.warning(QDialog(),"Could not create output File. Check permissions!")
      sys.exit(1)

  band = outDs.GetRasterBand(1)
  band.WriteArray(array)
  
  # flush data to disk, set the NoData value
  band.FlushCache()
  band.SetNoDataValue(nodata)
  
  # georeference the image and set the projection
  outDs.SetGeoTransform(raster.GetGeoTransform())
  outDs.SetProjection(raster.GetProjection())
  
  band = outDs = None # Close writing

# Adds a generated Raster to the QGis table of contents
def rasterInQgis(rasterPath):
  fileName = str(rasterPath)
  fileInfo = QFileInfo(fileName)
  baseName = fileInfo.baseName()
  rlayer = QgsRasterLayer(fileName, baseName)
  if not rlayer.isValid():
    QMessageBox.warning(QDialog(),"Failed to add the generated Layer to QGis")
  
  QgsMapLayerRegistry.instance().addMapLayer(rlayer)
  
# Adds a vector layer to the QGis table of contents
def tableInQgis(vectorPath):
  fileName = str(vectorPath)
  fileInfo = QFileInfo(fileName)
  baseName = fileInfo.baseName()
  uri = "file:/"+fileName+"?delimiter=%s" % (";")
  vlayer = QgsVectorLayer(uri, baseName, "delimitedtext")
  if not vlayer.isValid():
    QMessageBox.warning(QDialog(),"LecoS: Warning","Failed to add the Layer to QGis")
  QgsMapLayerRegistry.instance().addMapLayer(vlayer)
  
# Error messages wrapper
def DisplayError(iface,header,text,type="WARNING",time=4,both=False):
  if QGis.QGIS_VERSION_INT >= 10900:
    # What time of message?
    if type=="INFO":
      ob = QgsMessageBar.INFO
    elif type=="WARNING":
      ob = QgsMessageBar.WARNING
    elif type=="CRITICAL":
      ob = QgsMessageBar.CRITICAL  

    # Show the Message Bar
    iface.messageBar().pushMessage(header,text, ob, time)    
    if both: # Should the Messagebox also be shown?
      if type == "WARNING":
        QMessageBox.warning( QDialog(), header, text )
      elif type=="INFO":
        QMessageBox.information( QDialog(), header, text )
      elif type=="CRITICAL":
        QMessageBox.critical( QDialog(), header, text )
  else:
    if type == "WARNING":
      QMessageBox.warning( QDialog(), header, text )
    elif type=="INFO":
      QMessageBox.information( QDialog(), header, text )
    elif type=="CRITICAL":
      QMessageBox.critical( QDialog(), header, text )


  