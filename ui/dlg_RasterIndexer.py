# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_RasterIndexer.ui'
#
# Created: Mon Apr 15 19:08:48 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RasterIndexer(object):
    def setupUi(self, RasterIndexer):
        RasterIndexer.setObjectName(_fromUtf8("RasterIndexer"))
        RasterIndexer.resize(550, 406)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RasterIndexer.sizePolicy().hasHeightForWidth())
        RasterIndexer.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(RasterIndexer)
        self.buttonBox.setGeometry(QtCore.QRect(190, 370, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.methodSource = QtGui.QTextEdit(RasterIndexer)
        self.methodSource.setGeometry(QtCore.QRect(240, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.methodSource.setFont(font)
        self.methodSource.setFrameShape(QtGui.QFrame.NoFrame)
        self.methodSource.setFrameShadow(QtGui.QFrame.Plain)
        self.methodSource.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.methodSource.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.methodSource.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.methodSource.setReadOnly(True)
        self.methodSource.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.methodSource.setObjectName(_fromUtf8("methodSource"))
        self.line = QtGui.QFrame(RasterIndexer)
        self.line.setGeometry(QtCore.QRect(10, 50, 531, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.frame = QtGui.QFrame(RasterIndexer)
        self.frame.setGeometry(QtCore.QRect(10, 70, 531, 291))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 511, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 511, 131))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 511, 27))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sb_movWin = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.sb_movWin.setWrapping(False)
        self.sb_movWin.setFrame(True)
        self.sb_movWin.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_movWin.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.sb_movWin.setSpecialValueText(_fromUtf8(""))
        self.sb_movWin.setMinimum(3)
        self.sb_movWin.setSingleStep(2)
        self.sb_movWin.setObjectName(_fromUtf8("sb_movWin"))
        self.horizontalLayout.addWidget(self.sb_movWin)
        self.line_3 = QtGui.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 511, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cb_Raster = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.cb_Raster.setObjectName(_fromUtf8("cb_Raster"))
        self.horizontalLayout_2.addWidget(self.cb_Raster)
        self.line_2 = QtGui.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.line_4 = QtGui.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(10, 160, 511, 16))
        self.line_4.setFrameShadow(QtGui.QFrame.Plain)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 511, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 511, 34))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.le_where2save = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.le_where2save.setReadOnly(True)
        self.le_where2save.setObjectName(_fromUtf8("le_where2save"))
        self.horizontalLayout_3.addWidget(self.le_where2save)
        self.btn_Save = QtGui.QToolButton(self.horizontalLayoutWidget_3)
        self.btn_Save.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn_Save.setArrowType(QtCore.Qt.NoArrow)
        self.btn_Save.setObjectName(_fromUtf8("btn_Save"))
        self.horizontalLayout_3.addWidget(self.btn_Save)
        self.line_5 = QtGui.QFrame(self.horizontalLayoutWidget_3)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_3.addWidget(self.line_5)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(0, 70, 291, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.groupBox_3 = QtGui.QGroupBox(RasterIndexer)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 0, 211, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.cb_method = QtGui.QComboBox(self.groupBox_3)
        self.cb_method.setGeometry(QtCore.QRect(0, 20, 211, 31))
        self.cb_method.setObjectName(_fromUtf8("cb_method"))

        self.retranslateUi(RasterIndexer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RasterIndexer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RasterIndexer.reject)
        QtCore.QMetaObject.connectSlotsByName(RasterIndexer)

    def retranslateUi(self, RasterIndexer):
        RasterIndexer.setWindowTitle(QtGui.QApplication.translate("RasterIndexer", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RasterIndexer", "<html><head/><body><p>Creates a forest fragmentation index map after <a href=\"http://www.consecol.org/vol4/iss2/art3/\"><span style=\" text-decoration: underline; color:#0000ff;\">Riitters et al.</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("RasterIndexer", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("RasterIndexer", "Size of moving Window (odd number)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RasterIndexer", "<html><head/><body><p>Forest raster layer </p><p>(where forest=1, non-forest=0)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("RasterIndexer", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Save.setText(QtGui.QApplication.translate("RasterIndexer", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("RasterIndexer", "<html><head/><body><p>Where to save</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("RasterIndexer", "Append to table of contents afterwards", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("RasterIndexer", "Method:", None, QtGui.QApplication.UnicodeUTF8))

