from PyQt5.QtWidgets import QDialog
from gui.Ui_worddialog import Ui_Dialog
from utils.orth import Orth

class WordDialog(QDialog, Ui_Dialog):
    """Dialog for adding or modifying a word
    """
    def __init__(self) -> None:
        super().__init__()
        self.orth = Orth()
        self.setupUi(self)
        self.lineEditCon.textChanged.connect(self.displayCon)
        self.lineEditNat.textChanged.connect(self.displayNat)
        self.lineEditPron.textChanged.connect(self.displayPron)
    
    def displayCon(self) -> None:
        raw = self.lineEditCon.text()
        self.lineEditConDisplay.setText(self.orth(raw))
    
    def displayNat(self) -> None:
        raw = self.lineEditNat.text()
        self.lineEditNatDisplay.setText(self.orth(raw))
    
    def displayPron(self) -> None:
        raw = self.lineEditPron.text()
        self.lineEditPronDisplay.setText(self.orth(raw))
    
    # def con(self) -> str:
    #     return self.lineEditConDisplay.text()
    
    # def nat(self) -> str:
    #     return self.lineEditNatDisplay.text()
    
    # def pos(self) -> str:
    #     return self.lineEditPOS.text()
    
    # def ipa(self) -> str:
    #     return self.lineEditPronDisplay.text()
    
    # def info(self) -> str:
    #     return self.textEditInfo.toPlainText()
    
    def pack(self) -> dict:
        return {
            'con': self.lineEditConDisplay.text(),
            'nat': self.lineEditNatDisplay.text(),
            'pos': self.lineEditPOS.text(),
            'ipa': self.lineEditPronDisplay.text(),
            'info': self.textEditInfo.toPlainText()
        }
    
    def set(self, con: str, nat: str, pos: str, ipa: str, info: str) -> None:
        self.lineEditCon.setText(con)
        self.lineEditNat.setText(nat)
        self.lineEditPOS.setText(pos)
        self.lineEditPron.setText(ipa)
        self.textEditInfo.setPlainText(info)