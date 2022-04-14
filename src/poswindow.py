from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QDialog
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont
from gui.Ui_poswindow import Ui_MainWindow
from posdialog import POSDialog
from babel import Lexicon

class POSItem(QListWidgetItem):
    fntNam = QFont('Consolas', 20)
    def __init__(self, nam, rank):
        super().__init__(nam)
        self.rank = rank
        self.setTextAlignment(Qt.AlignCenter)
        self.setFont(POSItem.fntNam)

class POSWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, lexicon: Lexicon):
        super().__init__()
        self.lexicon = lexicon
        self.setupUi(self)
        self.loadPOSList()
    
    @pyqtSlot()
    def on_actionAdd_triggered(self):
        dlgAdd = POSDialog()
        dlgAdd.setWindowTitle('Add part of speech')
        while dlgAdd.exec() == QDialog.Accepted:
            item = self.lexicon.add_word(**dlgAdd.pack())
            if item:
                self.POSlist.addItem(POSItem(**item))
                self.modified = True
                break
    
    def loadPOSList(self) -> None:
        self.POSlist.clear()
        for item in self.lexicon.POSlist():
            self.POSlist.addItem(POSItem(**item))