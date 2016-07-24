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
        self.regionCB.insertItems(1, [l for l in loc_dict if l != 'tallahassee'])
        self.categoryCB.insertItem(0, 'free')
        self.categoryCB.insertItems(1, [c for c in searchIndex if c != 'free'])
        self.searchBTN.clicked.connect(self.search)
        # self.viewBTN.clicked.connect()

    def search(self):
        mindate = str(self.dateEdit.date().toPyDate())
        region = str(self.regionCB.currentText())
        category = loc_dict[str(self.categoryCB.currentText())]
        searchterm = str(self.lineEdit.text())
        print mindate
        print region
        print category
        print searchterm
        self.craig = craigList(region, category, searchterm, mindate)
        self.buildlist()

    def buildlist(self):
        items = Items()
        # for c in self.craig:
        #     item = Item
        #     item.price = c.price
        #     item.descr = c.descr
        #     item.email = c.email
        #     item.phone = c.phone
        #     item.date = c.date
        # items.items.append(item)

    def viewlist(self):
        pass
        

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


def main():
    app = QtGui.QApplication(sys.argv)
    form = Cbot()
    # form = Item()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
