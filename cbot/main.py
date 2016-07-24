from PyQt4 import QtGui
import sys
import design
from regionaldata import loc_dict
import searchitem

class Cbot(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Cbot, self).__init__(parent)
        self.setupUi(self)
        self.setregiondata()
        self.setcategorydata()

    def setregiondata(self):
        self.regionCB.insertItem(0, 'tallahassee')
        self.regionCB.insertItems(1, [l for l in loc_dict if l != 'tallahassee'])

    def setcategorydata(self):
        pass
        

def main():
    app = QtGui.QApplication(sys.argv)
    form = Cbot()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
                    

