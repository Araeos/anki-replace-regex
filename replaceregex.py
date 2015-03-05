# -*- coding: utf-8 -*-
from aqt.qt import *
#from PyQt4.QtGui import QDialog
from PyQt4 import uic
import sys
# TODO: Remove all print statements

def main():
    app = QApplication(sys.argv)
    d = ReplaceRegex(None)
    d.show()
    sys.exit(app.exec_())

# TODO: Remove
isMac = False

class ReplaceRegex(QDialog):
    def __init__(self, mw):
        if isMac:
            # use a separate window on os x so we can a clean menu
            QDialog.__init__(self, None, Qt.Window)
        else:
            QDialog.__init__(self, mw)
        QDialog.__init__(self, None, Qt.Window)
        self.mw = mw
        #self.form = replaceregex.form.UI_Dialog()
        self.ui = uic.loadUi('replace-regex/form.ui', self)
        self.connect(self, SIGNAL("rejected()"), self.onReject)
        self.connect(self.ui.buttonBox, SIGNAL("accepted()"), self.onAccept)
    def onReject(self):
        print("Rejected")
        return True
    def onAccept(self):
        print("Accepted")
        return True


if __name__ == "__main__":
    main()
