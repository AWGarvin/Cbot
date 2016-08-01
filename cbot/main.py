from PyQt4 import QtGui
from PyQt4 import QtCore
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
import sys
import design
import urllib
import requests
import searchdesign
import clistdesign
import searchlistdesign
import postviewerdesign
import itemviewerdesign
from regionaldata import loc_dict
from catadata import searchIndex
from searchitem import *
from alerter import *
import collections
from threading import Thread
#from searchitem import craigList


################################################################################
# GIVE THE WINDOWS RELEVANT TITLES
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

        # self.carrier = self.carrierBox.getText()
        # self.email = self.emailEdit.getText()
        # self.phone = self.phoneEdit.getText()
        self.carrier = None
        self.email = None
        self.phone = None

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
            item.pics = c.getImages()
            self.items.append(item)

    def viewitemslist(self):
        # plist = DisplayImage(self, None)
        # plist.exec_()

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
        self.pics = None #
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
        self.imgButton.clicked.connect(self._img)
        self.emailBtn.clicked.connect(self._email)

    def _next(self):
        self.switchwindow(1)
        
    def _prev(self):
        self.switchwindow(-1)

    def _img(self):
        try:
            DisplayImage(self.item.pics, 0, self).exec_()
        except IndexError: pass # will create alert message box
        # saying that no images are available

    def _email(self):
        email = str(self.parent.emailEdit.text())
        item = self.item
        carrier = str(self.parent.carrierBox.currentText())
        phone = str(self.parent.phoneEdit.text())
        # print email
        # print carrier
        # print phone
        # alerter(item, email, phone, carrier)
        Thread(target=alerter, args=(item, email, phone, carrier)).start()


    def switchwindow(self, n):
        for i in range(0,len(self.parent.items)):
            if self.parent.items[i].title == self.item.title:
                post = self.parent.items[(i+n)%len(self.parent.items)]
                break
        self.close()
        DisplayItem(post, self.parent).exec_()



class DisplayImage(QtGui.QDialog, itemviewerdesign.Ui_Dialog):
    def __init__(self, images, imgnum, parent=None):
        super(DisplayImage, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.parent = parent
        self.imgNumber = imgnum
        self.url = images[self.imgNumber]
        self.data = urllib.urlopen(self.url).read()
        self.image = QtGui.QImage()
        self.image.loadFromData(self.data)
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)

        self.pushButton.clicked.connect(self._next)
        self.pushButton_2.clicked.connect(self._prev)

    def _next(self):
        self.switchwindow(1)
        
    def _prev(self):
        self.switchwindow(-1)

    def switchwindow(self, n):
        imgnum = (self.imgNumber + n) % len(self.parent.item.pics)
        nextImg = DisplayImage(self.parent.item.pics, imgnum, self.parent)
        self.close()
        nextImg.exec_()



def main():
    app = QtGui.QApplication(sys.argv)
    form = Cbot()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
