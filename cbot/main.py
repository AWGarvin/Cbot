from PyQt4 import QtGui
from PyQt4 import QtCore
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
import sys
import design
import searchdesign
import clistdesign
import searchlistdesign
import postviewerdesign
from regionaldata import loc_dict
from catadata import searchIndex
from searchitem import *
import collections
from threading import Thread
#from searchitem import craigList


################################################################################
# GIVE THE WINDOWS RELEVANT TITLES 
################################################################################

class Cbot(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Cbot, self).__init__(parent)
        self.setupUi(self)
        self.items = []
        self.regionCB.insertItem(0, 'tallahassee')
        self.regionCB.insertItems(1, [l for l in sorted(loc_dict)
                                      if l != 'tallahassee'])
        self.categoryCB.insertItem(0, 'free')
        self.categoryCB.insertItems(1, [c for c in sorted(searchIndex)
                                        if c != 'free'])
        self.searchBTN.clicked.connect(self.threadsearch)
        self.viewBTN.clicked.connect(self.viewitemslist)

    def threadsearch(self):
        Thread(target=self.search, args=()).start()
        #self.connect(self.search, QtCore.SIGNAL("threadDone(QString)"), self.threadDone, QtCore.Qt.DirectConnection)

    def search(self):
        mindate = str(self.dateEdit.date().toPyDate())
        region = str(loc_dict[str(self.regionCB.currentText())])
        category = str(self.categoryCB.currentText())
        searchterm = str(self.lineEdit.text())
        self.craig = craigList(region, category, searchterm, mindate)
        if self.craig.cList == []:
            print "empty craig!"
            return
        self.buildlist()

    def buildlist(self):
        for c in self.craig.cList:
            # item = Item(self)
            item = Item()
            item.price = str(c.price)[2:-2]
            item.descr = str(c.descr)
            item.email = str(c.email)[2:-2]
            item.phone = str(c.phone)[2:-2]
            item.date = str(c.date)[2:-2]
            item.title = str(c.title)[2:-2]
            self.items.append(item)

    def viewitemslist(self):
        ilist = ItemList(self)
        if ilist.exec_():
            try:
                title = ilist.getposttitle()
                post = [i for i in self.items if title == i.title][0]
                DisplayItem(post).exec_()
            except IndexError: pass

class ItemList(QtGui.QDialog, searchlistdesign.Ui_Dialog):
    def __init__(self, parent=None):
        super(ItemList, self).__init__(parent)
        self.setupUi(self)
        try:
            self.postCB.insertItems(0, [p.title for p in parent.items])
        except: pass

    def getposttitle(self):
        return self.postCB.currentText()
        

class Item():
    def __init__(self):
        # lines followed by hash will be needed for email
        self.region = None
        self.category = None #
        self.searchterm = None #
        self.title = None #
        self.descr = None #
        self.price = None #
        self.email = None #
        self.phone = None #
        self.date = None #
        # need to also send carrier
        # need link to listing
        # post id number possibly

class DisplayItem(QtGui.QDialog, postviewerdesign.Ui_Dialog):
    def __init__(self, item, parent=None):
        super(DisplayItem, self).__init__(parent)
        self.setupUi(self)
        text = """\
        \r Title: %s\
        \r Price: %s\
        \r Date: %s\
        \r Phone: %s\
        \r Email: %s\
        \n%s\
        """%(item.title, item.price, item.date,
             item.phone, item.email, item.descr)
        self.textBrowser.setText(text)


def main():
    app = QtGui.QApplication(sys.argv)
    form = Cbot()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
