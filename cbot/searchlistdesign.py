# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui_design/searchlistdesign.ui'
#
# Created: Tue Jul 26 17:20:01 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(315, 113)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.postCB = QtGui.QComboBox(Dialog)
        self.postCB.setObjectName(_fromUtf8("postCB"))
        self.verticalLayout.addWidget(self.postCB)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.choiceBTN = QtGui.QDialogButtonBox(Dialog)
        self.choiceBTN.setOrientation(QtCore.Qt.Horizontal)
        self.choiceBTN.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.choiceBTN.setObjectName(_fromUtf8("choiceBTN"))
        self.verticalLayout_2.addWidget(self.choiceBTN)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.choiceBTN, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.choiceBTN, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Select Post to View:", None))

