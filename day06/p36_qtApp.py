# file: p36_qtApp.py
# desc: PyQt5 앱 만들기 - 라벨추가

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

# QMainWindow, QLabel, QPushButton 등은 QWidget 을 상속한 자식 클래스
from PyQt5.QtWidgets import *


class myApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel()  # 라벨위젯(qt, PyQt) == 라벨컨트롤(MFC, C#, Java Fx, Android)
        self.setGeometry(500, 250, 1000, 600)
        self.setWindowTitle("My qtApp - label")
        label.setText("Amazing Football Player = Cristiano")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # 위치
        label.setStyleSheet(
            ("color: red; background: black")
        )  # 라벨의 색상스타일 설정( CSS 와 동일 )

        font = label.font()
        font.setFamily("D2Coding")
        font.setPointSize(20)

        label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
        self.show()

    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        paint.setPen(QColor(102, 204, 102))
        paint.setFont(QFont("D2Coding", 30))
        paint.drawText(275, 300, "Football is Cristiano Ronaldo")

        paint.end()


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./images/windows.png"))
instance = myApp()
app.exec_()
