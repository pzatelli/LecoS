# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_PolygonPerLandCover.ui'
#
# Created: Sun Oct 20 13:01:21 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BatchDialog(object):
    def setupUi(self, BatchDialog):
        BatchDialog.setObjectName(_fromUtf8("BatchDialog"))
        BatchDialog.setWindowModality(QtCore.Qt.WindowModal)
        BatchDialog.resize(657, 574)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BatchDialog.sizePolicy().hasHeightForWidth())
        BatchDialog.setSizePolicy(sizePolicy)
        BatchDialog.setMinimumSize(QtCore.QSize(657, 574))
        BatchDialog.setMaximumSize(QtCore.QSize(657, 574))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/icon_batchCover.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BatchDialog.setWindowIcon(icon)
        self.line = QtGui.QFrame(BatchDialog)
        self.line.setGeometry(QtCore.QRect(10, 80, 641, 16))
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.SettingsBox = QtGui.QGroupBox(BatchDialog)
        self.SettingsBox.setGeometry(QtCore.QRect(10, 90, 671, 131))
        self.SettingsBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SettingsBox.setFlat(False)
        self.SettingsBox.setCheckable(False)
        self.SettingsBox.setObjectName(_fromUtf8("SettingsBox"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.SettingsBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 291, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.rb_Landscape = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.rb_Landscape.setChecked(True)
        self.rb_Landscape.setObjectName(_fromUtf8("rb_Landscape"))
        self.horizontalLayout_3.addWidget(self.rb_Landscape)
        self.rb_Class = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.rb_Class.setObjectName(_fromUtf8("rb_Class"))
        self.horizontalLayout_3.addWidget(self.rb_Class)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.SettingsBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(330, 0, 311, 31))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.ClassLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.ClassLayout.setMargin(0)
        self.ClassLayout.setObjectName(_fromUtf8("ClassLayout"))
        self.LabelClass = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.LabelClass.setObjectName(_fromUtf8("LabelClass"))
        self.ClassLayout.addWidget(self.LabelClass)
        self.cb_LClass = QtGui.QComboBox(self.horizontalLayoutWidget_4)
        self.cb_LClass.setObjectName(_fromUtf8("cb_LClass"))
        self.ClassLayout.addWidget(self.cb_LClass)
        self.label_3 = QtGui.QLabel(self.SettingsBox)
        self.label_3.setGeometry(QtCore.QRect(0, 50, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.SettingsBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 70, 641, 27))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ch_saveResult = QtGui.QCheckBox(self.horizontalLayoutWidget_5)
        self.ch_saveResult.setChecked(True)
        self.ch_saveResult.setObjectName(_fromUtf8("ch_saveResult"))
        self.horizontalLayout_5.addWidget(self.ch_saveResult)
        spacerItem = QtGui.QSpacerItem(150, 0, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.where2Save = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        font.setItalic(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.where2Save.setFont(font)
        self.where2Save.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.where2Save.setInputMask(_fromUtf8(""))
        self.where2Save.setAlignment(QtCore.Qt.AlignCenter)
        self.where2Save.setObjectName(_fromUtf8("where2Save"))
        self.horizontalLayout_5.addWidget(self.where2Save)
        self.locateDir = QtGui.QToolButton(self.horizontalLayoutWidget_5)
        self.locateDir.setObjectName(_fromUtf8("locateDir"))
        self.horizontalLayout_5.addWidget(self.locateDir)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.SettingsBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 100, 641, 22))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.ch_addToTable = QtGui.QCheckBox(self.horizontalLayoutWidget_6)
        self.ch_addToTable.setObjectName(_fromUtf8("ch_addToTable"))
        self.horizontalLayout_6.addWidget(self.ch_addToTable)
        self.line_4 = QtGui.QFrame(self.SettingsBox)
        self.line_4.setGeometry(QtCore.QRect(300, 10, 20, 41))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.SettingsBox)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(330, 30, 311, 31))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.LabelVector = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.LabelVector.setObjectName(_fromUtf8("LabelVector"))
        self.horizontalLayout_7.addWidget(self.LabelVector)
        self.cb_SelD = QtGui.QComboBox(self.horizontalLayoutWidget_7)
        self.cb_SelD.setObjectName(_fromUtf8("cb_SelD"))
        self.horizontalLayout_7.addWidget(self.cb_SelD)
        self.horizontalLayoutWidget = QtGui.QWidget(BatchDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(312, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cb_Raster = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.cb_Raster.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_Raster.setObjectName(_fromUtf8("cb_Raster"))
        self.horizontalLayout.addWidget(self.cb_Raster)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(BatchDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 641, 34))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cb_Vector = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.cb_Vector.setObjectName(_fromUtf8("cb_Vector"))
        self.horizontalLayout_2.addWidget(self.cb_Vector)
        self.line_2 = QtGui.QFrame(BatchDialog)
        self.line_2.setGeometry(QtCore.QRect(10, 520, 641, 16))
        self.line_2.setFrameShadow(QtGui.QFrame.Raised)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(BatchDialog)
        self.line_3.setGeometry(QtCore.QRect(10, 210, 641, 16))
        self.line_3.setFrameShadow(QtGui.QFrame.Raised)
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayoutWidget = QtGui.QWidget(BatchDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 230, 234, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.lay_ClassMet = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ClassMet.setMargin(0)
        self.lay_ClassMet.setObjectName(_fromUtf8("lay_ClassMet"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lay_ClassMet.addWidget(self.label_4)
        self.Cl_Metrics = QtGui.QListWidget(self.verticalLayoutWidget)
        self.Cl_Metrics.setFrameShape(QtGui.QFrame.WinPanel)
        self.Cl_Metrics.setFrameShadow(QtGui.QFrame.Sunken)
        self.Cl_Metrics.setLineWidth(1)
        self.Cl_Metrics.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Cl_Metrics.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Cl_Metrics.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.Cl_Metrics.setObjectName(_fromUtf8("Cl_Metrics"))
        self.lay_ClassMet.addWidget(self.Cl_Metrics)
        self.ch_selectAll = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.ch_selectAll.setObjectName(_fromUtf8("ch_selectAll"))
        self.lay_ClassMet.addWidget(self.ch_selectAll)
        self.verticalLayoutWidget_2 = QtGui.QWidget(BatchDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 360, 163, 95))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.ch_div1 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.ch_div1.setObjectName(_fromUtf8("ch_div1"))
        self.verticalLayout_2.addWidget(self.ch_div1)
        self.ch_div2 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.ch_div2.setObjectName(_fromUtf8("ch_div2"))
        self.verticalLayout_2.addWidget(self.ch_div2)
        self.ch_div3 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.ch_div3.setObjectName(_fromUtf8("ch_div3"))
        self.verticalLayout_2.addWidget(self.ch_div3)
        self.gridLayoutWidget = QtGui.QWidget(BatchDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 230, 391, 121))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.LandscapeBox = QtGui.QGridLayout(self.gridLayoutWidget)
        self.LandscapeBox.setMargin(0)
        self.LandscapeBox.setObjectName(_fromUtf8("LandscapeBox"))
        self.ch_LC4 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ch_LC4.setObjectName(_fromUtf8("ch_LC4"))
        self.LandscapeBox.addWidget(self.ch_LC4, 4, 0, 1, 1)
        self.ch_LC1 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ch_LC1.setObjectName(_fromUtf8("ch_LC1"))
        self.LandscapeBox.addWidget(self.ch_LC1, 1, 0, 1, 1)
        self.ch_LC2 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ch_LC2.setObjectName(_fromUtf8("ch_LC2"))
        self.LandscapeBox.addWidget(self.ch_LC2, 2, 0, 1, 1)
        self.ch_LC3 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ch_LC3.setObjectName(_fromUtf8("ch_LC3"))
        self.LandscapeBox.addWidget(self.ch_LC3, 3, 0, 1, 1)
        self.ch_LC5 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ch_LC5.setObjectName(_fromUtf8("ch_LC5"))
        self.LandscapeBox.addWidget(self.ch_LC5, 1, 1, 1, 1)
        self.ch_LC7 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ch_LC7.setObjectName(_fromUtf8("ch_LC7"))
        self.LandscapeBox.addWidget(self.ch_LC7, 3, 1, 1, 1)
        self.ch_LC6 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ch_LC6.setObjectName(_fromUtf8("ch_LC6"))
        self.LandscapeBox.addWidget(self.ch_LC6, 2, 1, 1, 1)
        self.ch_LC8 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ch_LC8.setObjectName(_fromUtf8("ch_LC8"))
        self.LandscapeBox.addWidget(self.ch_LC8, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.LandscapeBox.addWidget(self.label_6, 0, 0, 1, 1)
        self.ch_AddQGIS = QtGui.QCheckBox(BatchDialog)
        self.ch_AddQGIS.setGeometry(QtCore.QRect(10, 540, 301, 20))
        self.ch_AddQGIS.setChecked(True)
        self.ch_AddQGIS.setObjectName(_fromUtf8("ch_AddQGIS"))
        self.horizontalLayoutWidget_8 = QtGui.QWidget(BatchDialog)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(380, 530, 271, 41))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.btn_About = QtGui.QPushButton(self.horizontalLayoutWidget_8)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_About.setIcon(icon1)
        self.btn_About.setIconSize(QtCore.QSize(12, 12))
        self.btn_About.setObjectName(_fromUtf8("btn_About"))
        self.horizontalLayout_8.addWidget(self.btn_About)
        self.startButtons = QtGui.QDialogButtonBox(self.horizontalLayoutWidget_8)
        self.startButtons.setOrientation(QtCore.Qt.Horizontal)
        self.startButtons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.startButtons.setCenterButtons(True)
        self.startButtons.setObjectName(_fromUtf8("startButtons"))
        self.horizontalLayout_8.addWidget(self.startButtons)
        self.label_2.setBuddy(self.label_2)

        self.retranslateUi(BatchDialog)
        QtCore.QObject.connect(self.startButtons, QtCore.SIGNAL(_fromUtf8("accepted()")), BatchDialog.accept)
        QtCore.QObject.connect(self.startButtons, QtCore.SIGNAL(_fromUtf8("rejected()")), BatchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BatchDialog)
        BatchDialog.setTabOrder(self.cb_Raster, self.cb_Vector)
        BatchDialog.setTabOrder(self.cb_Vector, self.rb_Class)
        BatchDialog.setTabOrder(self.rb_Class, self.rb_Landscape)
        BatchDialog.setTabOrder(self.rb_Landscape, self.cb_LClass)
        BatchDialog.setTabOrder(self.cb_LClass, self.Cl_Metrics)
        BatchDialog.setTabOrder(self.Cl_Metrics, self.startButtons)

    def retranslateUi(self, BatchDialog):
        BatchDialog.setWindowTitle(_translate("BatchDialog", "Polygon batch overlay", None))
        self.SettingsBox.setTitle(_translate("BatchDialog", "Settings:", None))
        self.rb_Landscape.setText(_translate("BatchDialog", "Landscape", None))
        self.rb_Class.setText(_translate("BatchDialog", "Class", None))
        self.LabelClass.setText(_translate("BatchDialog", "Choose class :", None))
        self.label_3.setText(_translate("BatchDialog", "<html><head/><body><p>Output <span style=\" font-size:8pt; font-weight:400; font-style:italic;\">(unselect for direct output)</span>:</p></body></html>", None))
        self.ch_saveResult.setText(_translate("BatchDialog", "Save in file:", None))
        self.where2Save.setText(_translate("BatchDialog", "Select a destination or leave blank to create a temporary file", None))
        self.locateDir.setText(_translate("BatchDialog", "...", None))
        self.ch_addToTable.setText(_translate("BatchDialog", "Save in attribute table", None))
        self.LabelVector.setText(_translate("BatchDialog", "Vector grid ID :", None))
        self.label.setText(_translate("BatchDialog", "Landscape layer :", None))
        self.label_2.setText(_translate("BatchDialog", "<html><head/><body><p>Overlaying grid :</p></body></html>", None))
        self.label_4.setText(_translate("BatchDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Selected Metrics</span><br/><span style=\" font-size:9pt; font-style:italic;\">(press CTRL for multiple selections)</span></p></body></html>", None))
        self.ch_selectAll.setText(_translate("BatchDialog", "Select all", None))
        self.label_5.setText(_translate("BatchDialog", "Diversity", None))
        self.ch_div1.setText(_translate("BatchDialog", "Shannon Index", None))
        self.ch_div2.setText(_translate("BatchDialog", "Shannon equitability", None))
        self.ch_div3.setText(_translate("BatchDialog", "Simpson Index", None))
        self.ch_LC4.setText(_translate("BatchDialog", "Maximum", None))
        self.ch_LC1.setText(_translate("BatchDialog", "Mean", None))
        self.ch_LC2.setText(_translate("BatchDialog", "Sum", None))
        self.ch_LC3.setText(_translate("BatchDialog", "Minimum", None))
        self.ch_LC5.setText(_translate("BatchDialog", "Standard Deviation", None))
        self.ch_LC7.setText(_translate("BatchDialog", "Median", None))
        self.ch_LC6.setText(_translate("BatchDialog", "Lower Quantile (25%)", None))
        self.ch_LC8.setText(_translate("BatchDialog", "Upper Quantile (25%)", None))
        self.label_6.setText(_translate("BatchDialog", "Zonal statistics", None))
        self.ch_AddQGIS.setText(_translate("BatchDialog", "Add table to QGIS afterwards", None))
        self.btn_About.setText(_translate("BatchDialog", "About", None))

import resources_rc
