# file: p44_noThreadApp.py
# desc: PyQt5 스레드 학습용(스레드 사용안함)


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
        uic.loadUi("./day07/testThread.ui", self)
        self.setWindowTitle("No Thread App")
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked)
        self.show()

    def btnStartClicked(self):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, 999_999)  # 프로그레스바 범위설정
        self.btnStart.setDisabled(True)
        for i in range(0, 1_000_000):
            print(f"No Thread Start >> {i}")
            self.pgbTask.setValue(i)
            self.txbLog.append(f"No Thread Start >> {i}")
            # UI(메인)스레드가 화면을 그릴 수 있는 여유가 없음(응답없음 발생)

        self.btnStart.setEnabled(True)

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
