# file: p38_qtApp.py
# desc: PyQt5 앱 만들기 - QtDesigner

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class myApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):  # UI 파일을 로드하여 화면디자인 사용
        uic.loadUi("./day06/firstApp.ui", self)
        self.setWindowTitle("My qtApp - QtDesigner")
        # 버튼 시그널처리
        self.btnMsg.clicked.connect(
            self.btnMsgClicked
        )  # UI 파일 내 위젯은 자동완성이 안된다.
        self.show()

    def btnMsgClicked(self):
        QMessageBox.about(self, "Qt 디자이너", "클릭함 ㅋㅋ")
        self.label.setText("Messi is Dog !!!!")

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(
            self, "종료", "종료 하시겠습니까?", QMessageBox.Cancel | QMessageBox.Yes
        )
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./images/appleCEO.png"))
instance = myApp()
app.exec_()
