# file: p45_threadApp.py
# desc: PyQt5 스레드 학습용(스레드 사용)


import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# QThread: PyQt를 쓰기위한 쓰레드(Thread 와 유사함)
class BackgroundWorker(QThread):
    # UI 스레드의 권한을 BackgroundWorker 스레드에게 권한을 주지않는다!!
    # BackgroundWorker 가 UI스레드에게 신호를 보내줘야 한다.

    # 스레드로 진행 시 UI에서 초기화부분 시그널 전달
    initUiSignal = pyqtSignal(int)

    # 스레드 진행 시 변경되는 숫자를 UI로 전달
    setPgbSignal = pyqtSignal(int)

    # 스레드 진행 시 화면에 출력될 문자열을 UI로 전달
    setTxbSignal = pyqtSignal(str)

    def __init__(self, parent) -> None:  # 부모는 qtApp 클래스
        super().__init__(parent)
        self.parent = parent

    def run(self) -> None:
        # maxVal = 524_287 + 2000 # 524287 줄 이상은 pyQt 창에 안뜬다
        maxVal = 10000 # 524287 줄 이상은 pyQt 창에 안뜬다

        # UI쪽(qtApp)으로 값을 전달( emit()함수는 전송함수 )
        self.initUiSignal.emit(maxVal)

        for i in range(maxVal):
            print(f"Thread start >>>>> {i}")
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f"Thread start >>>>> {i}")


class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):  # UI 파일을 로드하여 화면디자인 사용
        uic.loadUi("./day07/testThread.ui", self)
        self.setWindowTitle("Thread App")
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked)
        self.show()

    def btnStartClicked(self):
        self.btnStart.setDisabled(True)
        th = BackgroundWorker(self)
        th.start()
        th.initUiSignal.connect(self.initPgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbTask)
        self.btnStart.setEnabled(True)

    @pyqtSlot(str)
    def setTxbTask(self, msg):
        self.txbLog.append(msg)

    @pyqtSlot(int)
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

    @pyqtSlot(int)  # pyQtSignal 에서 넘어온 값을 처리해주는 함수라고 선언
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal)

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
instance = qtApp()
app.exec_()
