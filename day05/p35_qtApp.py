# file: p35_qtApp.py
# desc: PyQt5 앱 만들기

"""
PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C, C++ 사용할 GUI(WinApp) 프레임워크(멀티 플랫폼)

설치: pip3 install PyQt5
QApplication : 앱을 전체관리하는 클래스
QWidget : 상단 메뉴바가 없는 윈도우 창
QMainWindow : 상단 메뉴바가 있는 윈도우 창
"""
import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class myApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 250, 1000, 600)
        self.setWindowTitle("My First Windows App")
        self.show()  # 필수 메서드

    def paintEvent(self, event) -> None:
        paint = QPainter()  # 윈도우 창 위에 그림을 그리는 객체
        paint.begin(self)  # 그림을 그리기 시작

        paint.setPen(QColor(102, 204, 102))  # 폰트 색상(R,G,B)
        paint.setFont(QFont("D2Coding", 30))  # 폰트 종류와 크기
        paint.drawText(
            275, 300, "Football is Cristiano Ronaldo"
        )  # 윈도우 창에 글자를 그린다.

        paint.end()  # 그림을 닫아야한다.


app = QApplication(sys.argv)  # 실행할 때 파라미터를 받아 처리할 수 있다.
app.setWindowIcon(QIcon("./images/windows.png"))
instance = myApp()  # 객체 생성
app.exec_()  # 실행
