# file: p37_qtApp.py
# desc: PyQt5 앱 만들기 - 버튼 추가

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent

from PyQt5.QtWidgets import *


class myApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry((1920 - 300) // 2, (1080 - 300) // 2, 320, 230)
        self.setWindowTitle("My qtApp - button")
        # 화면 UI에서 추가/변경
        btn1 = QPushButton("매수", self)
        btn1.setGeometry(210, 180, 100, 40)
        btn1.clicked.connect(self.btn1Clicked)
        self.show()

    def btn1Clicked(self):
        QMessageBox.about(self, "매수", "매수하셨습니다.")

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(
            self, "파산", "파산신청 하시겠습니까?", QMessageBox.Cancel | QMessageBox.Yes
        )
        if re == QMessageBox.Yes:
            QCloseEvent.accept()  # 닫기
        else:
            QCloseEvent.ignore()  # 무시


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./images/appleCEO.png"))
instance = myApp()
app.exec_()
