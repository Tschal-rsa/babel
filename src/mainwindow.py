from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QMessageBox, QListWidgetItem, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont, QColor
from gui.Ui_mainwindow import Ui_MainWindow
from babel import Lexicon
from worddialog import WordDialog
from poswindow import POSWindow
import os

class wordItem(QListWidgetItem):
    fntCon = QFont('Georgia', 20)
    def __init__(self, con, rank, idx):
        super().__init__(con)
        self.rank, self.idx = rank, idx
        self.setTextAlignment(Qt.AlignCenter)
        self.setFont(wordItem.fntCon)
    
    def set(self, con, rank, idx):
        self.setText(con)
        self.rank, self.idx = rank, idx

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.path = ''
        self.modified = False
        self.lexicon = Lexicon()
        self.windowPOS = POSWindow(self.lexicon)
        local = os.path.dirname(__file__)
        with open(os.path.join(local, 'template/lexBrowser.html'), 'r', encoding='utf-8') as f:
            self.lexTemplate = f.read()
        self.setupUi(self)
        self.wordlist.currentItemChanged.connect(self.render_word)
    
    @pyqtSlot()
    def on_actionPOSView_triggered(self):
        self.windowPOS = POSWindow(self.lexicon)
        self.windowPOS.show()
    
    def render_word(self, item: wordItem):
        template = self.lexTemplate
        for key, value in self.lexicon.word_at(item.rank).items():
            template = template.replace(f'[{key}]', value)
        self.lexBrowser.setHtml(template)
        self.statusbar.showMessage(f'#{item.idx}')
    
    @pyqtSlot()
    def on_actionAdd_triggered(self):
        dlgAdd = WordDialog()
        dlgAdd.setWindowTitle('Add word')
        while dlgAdd.exec() == QDialog.Accepted:
            item = self.lexicon.add_word(**dlgAdd.pack())
            if item:
                self.wordlist.addItem(wordItem(**item))
                self.modified = True
                break
    
    @pyqtSlot()
    def on_actionRemove_triggered(self):
        # only remove when semete(at least) exists 1 item
        if self.wordlist.count() > 0:
            # select current row
            row = self.wordlist.currentRow()
            # remove word
            self.lexicon.remove_word(self.wordlist.currentItem().rank)
            # reload wordlist
            self.loadWordList()
            # show the next item (if exists)
            self.wordlist.setCurrentRow(row if self.wordlist.count() > row else row - 1)
            # modified
            self.modified = True
    
    @pyqtSlot()
    def on_actionModify_triggered(self):
        if self.wordlist.count() > 0:
            item = self.wordlist.currentItem()
            rank = item.rank
            dlgModify = WordDialog()
            dlgModify.setWindowTitle('Modify current word')
            dlgModify.set(**self.lexicon.word_at(rank, simple=True))
            if dlgModify.exec() == QDialog.Accepted:
                packed_item = self.lexicon.modify_word(rank, **dlgModify.pack())
                item.set(**packed_item)
                self.render_word(item)
                self.modified = True
    
    def setPath(self, path: str) -> None:
        self.path = path
        self.setWindowTitle(f'Babel ~ {os.path.split(path)[1]}')
    
    def loadWordList(self) -> None:
        # avoid "segmentation fault"
        self.wordlist.currentItemChanged.disconnect(self.render_word)
        self.wordlist.clear()
        # self.wordlist.addItems(self.lexicon.wordlist())
        for item in self.lexicon.wordlist():
            self.wordlist.addItem(wordItem(**item))
        # reconnect
        self.wordlist.currentItemChanged.connect(self.render_word)
    
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        self.questionSave()
        path, _ = QFileDialog.getOpenFileName(self, 'Open Babel Project', './project', 'Babel Project Files (*.babel);;All Files (*)')
        if path:
            self.setPath(path)
            self.modified = False
            self.lexicon = Lexicon(self.path)
            self.loadWordList()
    
    @pyqtSlot()
    def on_actionSaveAs_triggered(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save Babel Project', './project', 'Babel Project Files (*.babel);;All Files (*)')
        if path:
            self.setPath(path)
            self.modified = False
            self.lexicon.save(path)
    
    @pyqtSlot()
    def on_actionSave_triggered(self):
        if self.path:
            self.modified = False
            self.lexicon.save(self.path)
        else:
            self.on_actionSaveAs_triggered()
    
    @pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()
    
    def closeEvent(self, a0) -> None:
        super().closeEvent(a0)
        self.questionSave()
        a0.accept()
    
    def questionSave(self) -> None:
        if self.modified and QMessageBox.question(self, 'Wait a sec', 'Save?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.on_actionSave_triggered()
            self.modified = False