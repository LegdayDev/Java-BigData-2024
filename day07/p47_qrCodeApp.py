# file: p47_qrCodeApp.py
# desc: PyQt5 - QR 코드 앱
## QRcode 라이브러리 설치 : pip3 install qrcode

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qrcode 


class qrApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("./day07/qrApp.ui", self)
        self.setWindowTitle("QR Code Generator")
        self.btnGenerate.clicked.connect(self.btnGenerateClicked)
        self.show()

    def btnGenerateClicked(self):
        data = self.txtQrData.text()

        if len(data.strip()) == 0:
            QMessageBox.about(self, "경고", "뭐함? 데이터 안넣음?")
            return
        else:
            imgPath = "./day07/qr.png"
            qrImage = qrcode.make(data)
            qrImage.save("./day07/qr.png")
            img = QPixmap(imgPath)
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(
            self, "종료", "종료 하시겠습니까?", QMessageBox.Cancel | QMessageBox.Yes
        )
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./images/qrCode.png"))
instance = qrApp()
app.exec_()
