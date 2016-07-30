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
# HANDLE NO RESULTS FOUND IN PARSER
# FIX WEIRD THING AT TOP OF MAIN WINDOW
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
            item = Item()
            item.price = c.getPrice()
            item.descr = c.getDescr()
            item.email = c.getEmail()
            item.phone = c.getPhone()
            item.date = c.getDate()
            item.title = c.getTitle()
            self.items.append(item)

    def viewitemslist(self):
        ilist = ItemList(self)
        if ilist.exec_():
            try:
                title = ilist.getposttitle()
                post = [i for i in self.items if title == i.title][0]
                DisplayItem(post, self).exec_()
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
        # self.region = None
        # self.category = None #
        # self.searchterm = None #
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
        self.parent = parent
        self.item = item
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
        self.nextBTN.clicked.connect(self._next)
        self.prevBTN.clicked.connect(self._prev)

    def _next(self):
        self.switchwindow(1)
        
    def _prev(self):
        self.switchwindow(-1)

    def switchwindow(self, n):
        for i in range(0,len(self.parent.items)):
            if self.parent.items[i].title == self.item.title:
                post = self.parent.items[(i+n)%len(self.parent.items)]
                break
        DisplayItem(post, self.parent).exec_()
        self.close()


def main():
    app = QtGui.QApplication(sys.argv)
    form = Cbot()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
