# file: p48_transApp.py
# desc: PyQt5 - 구글 번역 앱
## 라이브러리 설치 : pip3 install googletrans==3.1.0a0 (알파버전)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from googletrans import Translator


class qrApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.myTrans = Translator()

    def initUI(self):
        uic.loadUi("./day07/transApp.ui", self)
        self.setWindowTitle("Google Translate App")
        self.btnTrans.clicked.connect(self.btnTransClicked)
        self.txtBaseText.returnPressed.connect(self.btnTransClicked)
        self.show()

    def btnTransClicked(self):
        # QMessageBox.about(self, "번역", "번역시작...")
        text = self.txtBaseText.text().strip()
        if len(text) != 0:
            result = self.myTrans.translate(text, src="auto", dest="en")
            self.txbResult.append(f'{text} -> {result.text}')

        pass

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(
            self, "종료", "종료 하시겠습니까?", QMessageBox.Cancel | QMessageBox.Yes
        )
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./images/QrCodeIcon.png"))
instance = qrApp()
app.exec_()
