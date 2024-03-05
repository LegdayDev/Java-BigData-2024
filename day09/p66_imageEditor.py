# file: p66_imageEditor.py
# desc: PyQt 이미지 에디터

"""
qrc 파일을 py로 변경
qyrcc5 파일명.qrc -o 파일명.py
"""

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import resources_qrc
# openCV 추가
import cv2


class imageEditor(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi("./day09/pyNewPaint.ui", self)
        self.setWindowTitle("Image Editor v0.5")
        ## 이미지 처리작업
        pixmap = (
            QPixmap("./images/day09Img/ronaldo.jpg")
            .scaledToHeight(441)
            .scaledToWidth(801)
        )
        self.lblCanvas.setPixmap(pixmap)

        self.brushColor = Qt.red

        self.show()

    def initSignal(self):
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Exit.triggered.connect(self.actionExitClicked)
        self.action_PenRed.triggered.connect(self.actionPenRedClicked)
        self.action_PenGreen.triggered.connect(self.actionPenGreenClicked)
        self.action_PenBlue.triggered.connect(self.actionPenBlueClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)
        # 변환메뉴 추가
        self.action_Grayscale.triggered.connect(self.actionGrayscaleClicked)

    def actionNewClicked(self):
        canvas = QPixmap(self.lblCanvas.width(), self.lblCanvas.height())
        canvas.fill(QColor("white"))
        self.lblCanvas.setPixmap(canvas)

    def actionOpenClicked(self):
        image = QFileDialog.getOpenFileName(
            self, "Image Open", "", "Image file(*.jpg;*.png;*.gif)"
        )
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(441).scaledToWidth(801)
        self.lblCanvas.setPixmap(pixmap)
        self.lblCanvas.adjustSize()

    def actionSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(
            self, "Image Save", "", "Image file(*.jpg;*.png)"
        )
        if filePath == "":
            return
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(filePath)

    def actionExitClicked(self):
        self.closeEvent(self)

    def actionPenRedClicked(self):
        self.brushColor = Qt.red

    def actionPenGreenClicked(self):
        self.brushColor = Qt.green

    def actionPenBlueClicked(self):
        self.brushColor = Qt.blue

    def actionAboutClicked(self):
        QMessageBox.about(self, "알림", "이미지 에디터 v0.5")

    def actionGrayscaleClicked(self):
        image = cv2.imread() # file 만 읽을 수 있다.

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lblCanvas.pixmap())
        brush.setPen(QPen(self.brushColor, 5.0, style=Qt.SolidLine, cap=Qt.RoundCap))
        brush.drawPoint(e.x(), e.y() - 45)
        brush.end()
        self.update()  # 화면 업데이트

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes :
            QCloseEvent.accept()
        else : 
            QCloseEvent.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./day09/imgs/editor.png"))
    instance = imageEditor()
    sys.exit(app.exec_())
