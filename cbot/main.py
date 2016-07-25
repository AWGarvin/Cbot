from PyQt4 import QtGui
import sys
import design
import searchdesign
import clistdesign
from regionaldata import loc_dict
from catadata import searchIndex
from searchitem import *
import collections
#from searchitem import craigList


class Cbot(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Cbot, self).__init__(parent)
        self.setupUi(self)
        self.regionCB.insertItem(0, 'tallahassee')
        self.regionCB.insertItems(1, [l for l in sorted(loc_dict)
                                      if l != 'tallahassee'])
        self.categoryCB.insertItem(0, 'free')
        self.categoryCB.insertItems(1, [c for c in sorted(searchIndex)
                                        if c != 'free'])
        self.searchBTN.clicked.connect(self.search)
        self.viewBTN.clicked.connect(self.itemtest)

    def search(self):
        mindate = str(self.dateEdit.date().toPyDate())
        region = str(loc_dict[str(self.regionCB.currentText())])
        category = str(self.categoryCB.currentText())
        searchterm = str(self.lineEdit.text())
        self.craig = craigList(region, category, searchterm, mindate)
        if self.craig.cList == []:
            print "empty craig!"
            return
        # for c in self.craig.cList: print c
        self.buildlist()
        self.itemtest()

    def buildlist(self):
        # self.items = Items()
        self.items = []
        for c in self.craig.cList:
            print c.price
            item = Item()
            item.price = str(c.price)
            item.descr = str(c.descr)
            item.email = str(c.email)
            item.phone = str(c.phone)
            item.date = str(c.date)
        self.items.append(item)

    def viewlist(self):
        pass

    def itemtest(self):
        print "showing window"
        self.items[0].set_vals()
        self.items[0].exec_()

class Items(QtGui.QDialog, clistdesign.Ui_Dialog):
    def __init__(self, parent=None):
        super(Items, self).__init__(parent)
        self.setupUi(self)
        self.items = []
        

class Item(QtGui.QDialog, searchdesign.Ui_Dialog):
    def __init__(self, parent=None):
        super(Item, self).__init__(parent)
        self.setupUi(self)
        self.region = None
        self.category = None
        self.searchterm = None
        self.title = None
        self.descr = None
        self.price = None
        self.email = None
        self.phone = None
        self.date = None

    def set_vals(self):
        self.label.setText(self.date)
        # self.label_3.setText(self.region)
        # self.label_6.setText(self.category)
        # self.label_8.setText(self.searchterm)
        # need to change label names
        # need more information from parser


def main():
    app = QtGui.QApplication(sys.argv)
    form = Cbot()
    # form = Item()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
