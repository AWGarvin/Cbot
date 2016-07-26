from PyQt4 import QtGui
import sys
import design
import searchdesign
import clistdesign
import searchlistdesign
from regionaldata import loc_dict
from catadata import searchIndex
from searchitem import *
import collections
#from searchitem import craigList


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
        self.searchBTN.clicked.connect(self.search)
        self.viewBTN.clicked.connect(self.viewitemslist)


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
        # self.items = Items()
        for c in self.craig.cList:
            item = Item()
            item.price = str(c.price)[2:-2]
            item.descr = str(c.descr)[2:-2]
            item.email = str(c.email)[2:-2]
            item.phone = str(c.phone)[2:-2]
            item.date = str(c.date)[2:-2]
            item.title = str(c.title)[2:-2]
            self.items.append(item)

    def viewitemslist(self):
        ilist = ItemList(self)
        if ilist.exec_():
            print ilist.getposttitle()
        
    # def itemtest(self):
    #     print "showing window"
    #     self.items[0].set_vals()
    #     self.items[0].exec_()


class ItemList(QtGui.QDialog, searchlistdesign.Ui_Dialog):
    def __init__(self, parent=None):
        super(ItemList, self).__init__(parent)
        self.setupUi(self)
        try:
            self.postCB.insertItems(0, [p.title for p in parent.items])
        except: pass

    def getposttitle(self):
        return self.postCB.currentText()
        
# class Items(QtGui.QDialog, clistdesign.Ui_Dialog):
#     def __init__(self, parent=None):
#         super(Items, self).__init__(parent)
#         self.setupUi(self)
#         # self.items = []
        

class Item(QtGui.QDialog, searchdesign.Ui_Dialog):
    def __init__(self, parent=None):
        super(Item, self).__init__(parent)
        self.setupUi(self)
        # lines followed by hash will be needed for email
        self.region = None
        self.category = None #
        self.searchterm = None #
        self.title = None
        self.descr = None #
        self.price = None #
        self.email = None #
        self.phone = None #
        self.date = None #
        # need to also send carrier
        # need link to listing
        # post id number possibly

    # def set_vals(self):
    #     self.label.setText(self.date)
    #     # self.label_3.setText(self.region)
    #     # self.label_6.setText(self.category)
    #     # self.label_8.setText(self.searchterm)
    #     # need to change label names
    #     # need more information from parser


def main():
    app = QtGui.QApplication(sys.argv)
    form = Cbot()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
