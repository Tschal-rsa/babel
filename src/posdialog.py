from PyQt5.QtWidgets import QDialog
from gui.Ui_posdialog import Ui_Dialog
from utils.orth import Orth

class POSDialog(QDialog, Ui_Dialog):
    """Dialog for adding or modifying a POS
    """
    def __init__(self) -> None:
        super().__init__()
        self.orth = Orth()
        self.setupUi(self)
        self.lineEditPOS.textChanged.connect(self.displayPOS)
    
    def displayPOS(self) -> None:
        raw = self.lineEditPOS.text()
        self.lineEditPOSDisplay.setText(self.orth(raw))
    
    def pack(self) -> dict:
        return {
            'nam': self.lineEditPOSDisplay.text(),
            'abbr': self.lineEditAbbr.text(),
            'info': self.textEditInfo.toPlainText()
        }