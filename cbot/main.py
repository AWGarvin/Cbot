from PyQt4 import QtGui
import sys
import design
from regionaldata import loc_dict
from catadata import searchIndex
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

    def search(self):
        mindate = str(self.dateEdit.date().toPyDate())
        region = self.regionCB.currentText()
        category = self.categoryCB.currentText()
        searchterm = self.lineEdit.text()
        #self.craig = craigList(region, category, searchterm, mindate)


def main():
    app = QtGui.QApplication(sys.argv)
    form = Cbot()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
