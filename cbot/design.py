# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui_design/main_window.ui'
#
# Created: Sat Jul 30 21:25:44 2016
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(353, 349)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.carrierBox = QtGui.QComboBox(self.centralwidget)
        self.carrierBox.setObjectName(_fromUtf8("carrierBox"))
        self.carrierBox.addItem(_fromUtf8(""))
        self.carrierBox.addItem(_fromUtf8(""))
        self.carrierBox.addItem(_fromUtf8(""))
        self.carrierBox.addItem(_fromUtf8(""))
        self.carrierBox.addItem(_fromUtf8(""))
        self.carrierBox.addItem(_fromUtf8(""))
        self.carrierBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.carrierBox)
        self.phoneEdit = QtGui.QLineEdit(self.centralwidget)
        self.phoneEdit.setObjectName(_fromUtf8("phoneEdit"))
        self.horizontalLayout.addWidget(self.phoneEdit)
        self.emailEdit = QtGui.QLineEdit(self.centralwidget)
        self.emailEdit.setObjectName(_fromUtf8("emailEdit"))
        self.horizontalLayout.addWidget(self.emailEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.viewBTN = QtGui.QPushButton(self.centralwidget)
        self.viewBTN.setObjectName(_fromUtf8("viewBTN"))
        self.verticalLayout_3.addWidget(self.viewBTN)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setDate(QtCore.QDate(2016, 1, 1))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.regionCB = QtGui.QComboBox(self.centralwidget)
        self.regionCB.setMinimumSize(QtCore.QSize(176, 29))
        self.regionCB.setMaximumSize(QtCore.QSize(176, 29))
        self.regionCB.setObjectName(_fromUtf8("regionCB"))
        self.horizontalLayout_3.addWidget(self.regionCB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.categoryCB = QtGui.QComboBox(self.centralwidget)
        self.categoryCB.setMinimumSize(QtCore.QSize(176, 29))
        self.categoryCB.setMaximumSize(QtCore.QSize(176, 29))
        self.categoryCB.setObjectName(_fromUtf8("categoryCB"))
        self.horizontalLayout_6.addWidget(self.categoryCB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.searchBTN = QtGui.QPushButton(self.centralwidget)
        self.searchBTN.setObjectName(_fromUtf8("searchBTN"))
        self.verticalLayout_3.addWidget(self.searchBTN)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar(MainWindow)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.carrierBox.setItemText(0, _translate("MainWindow", "Verison", None))
        self.carrierBox.setItemText(1, _translate("MainWindow", "Sprint", None))
        self.carrierBox.setItemText(2, _translate("MainWindow", "AT&T", None))
        self.carrierBox.setItemText(3, _translate("MainWindow", "T-Mobile", None))
        self.carrierBox.setItemText(4, _translate("MainWindow", "Virgin Mobile", None))
        self.carrierBox.setItemText(5, _translate("MainWindow", "Nextel", None))
        self.carrierBox.setItemText(6, _translate("MainWindow", "Alltel", None))
        self.phoneEdit.setText(_translate("MainWindow", "PHONE #", None))
        self.emailEdit.setText(_translate("MainWindow", "EMAIL", None))
        self.viewBTN.setText(_translate("MainWindow", "View All Existing Searches", None))
        self.label_5.setText(_translate("MainWindow", "Date Range:", None))
        self.label_3.setText(_translate("MainWindow", "Region:", None))
        self.label_6.setText(_translate("MainWindow", "Category: ", None))
        self.lineEdit.setText(_translate("MainWindow", "Enter Search Term(s)", None))
        self.searchBTN.setText(_translate("MainWindow", "ADD SEARCH", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3", None))

