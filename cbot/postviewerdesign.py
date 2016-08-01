# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui_design/postviewerdesign.ui'
#
# Created: Sun Jul 31 20:17:27 2016
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
        Dialog.resize(411, 278)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 281))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.prevBTN = QtGui.QPushButton(self.verticalLayoutWidget)
        self.prevBTN.setObjectName(_fromUtf8("prevBTN"))
        self.horizontalLayout.addWidget(self.prevBTN)
        self.imgButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.imgButton.setObjectName(_fromUtf8("imgButton"))
        self.horizontalLayout.addWidget(self.imgButton)
        self.nextBTN = QtGui.QPushButton(self.verticalLayoutWidget)
        self.nextBTN.setObjectName(_fromUtf8("nextBTN"))
        self.horizontalLayout.addWidget(self.nextBTN)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.emailBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.emailBtn.setObjectName(_fromUtf8("emailBtn"))
        self.horizontalLayout_2.addWidget(self.emailBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.prevBTN.setText(_translate("Dialog", "Prev", None))
        self.imgButton.setText(_translate("Dialog", "Images", None))
        self.nextBTN.setText(_translate("Dialog", "Next", None))
        self.emailBtn.setText(_translate("Dialog", "Contact Me!", None))

