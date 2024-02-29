# file: p39_naverNewsApp.py
# desc: PyQt5, QtDesigner로 Naver API 연동 뉴스 앱 만들기

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import webbrowser  # 기본 웹브라우저 모듈
from naverSearch import NaverSearch
import datetime
import time


class myApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("./day06/naverNews.ui", self)
        self.setWindowTitle("My qtApp - QtDesigner")
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        # 버튼 위젯 시그널처리
        self.tblSearchResult.itemSelectionChanged.connect(self.tblResultSelected)
        # 재검색을 위한 처리
        self.txtSearchWord.returnPressed.connect(self.btnSearchClicked)
        self.show()

    def tblResultSelected(self):  # 테이블 클릭 시
        selectRow = self.tblSearchResult.currentRow()  # 현재 선택된 행
        url = self.tblSearchResult.item(selectRow, 1).text()
        webbrowser.open(url)

    def btnSearchClicked(self):  # 검색버튼 클릭시
        searchWord = self.txtSearchWord.text().strip()
        if len(searchWord) == 0:
            QMessageBox.about(self, "네이버검색", "검색어를 입력해주세요!")
            return
        api = NaverSearch()
        jsonSearch = api.getSearchResult(searchWord)

        self.makeTable(jsonSearch)

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(
            self, "종료", "종료 하시겠습니까?", QMessageBox.Cancel | QMessageBox.Yes
        )
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    # 검색결과를 윈도우창에 띄우는 함수
    def makeTable(self, jsonData):
        result = jsonData["items"]

        self.tblSearchResult.setColumnCount(3)
        self.tblSearchResult.setRowCount(len(result))
        self.tblSearchResult.setHorizontalHeaderLabels(
            ["기사제목", "뉴스링크", "게시일자"]
        )

        n = 0
        for post in result:
            self.tblSearchResult.setItem(n, 0, QTableWidgetItem(post["title"]))
            self.tblSearchResult.setItem(n, 1, QTableWidgetItem(post["link"]))
            tempDates = str(post["pubDate"]).split(" ")  # 내일 설명
            year = tempDates[3]
            month = time.strptime(changeMonthFormat(tempDates[2]), "%m").tm_mon
            month = f"{month:02d}"
            day = tempDates[1]
            date = f"{year}-{month}-{day}"
            self.tblSearchResult.setItem(n, 2, QTableWidgetItem(date))
            n += 1

        self.tblSearchResult.setColumnWidth(0, 430)
        self.tblSearchResult.setColumnWidth(1, 200)
        # 더블클릭해서 값 수정하는것을 막는다.
        self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers)


def changeMonthFormat(month):
    if month == "Jan":
        return "1"
    elif month == "Feb":
        return "2"
    elif month == "Mar":
        return "3"
    elif month == "Apr":
        return "4"
    elif month == "May":
        return "5"
    elif month == "Jun":
        return "6"
    elif month == "Jul":
        return "7"
    elif month == "Aug":
        return "8"
    elif month == "Sep":
        return "9"
    elif month == "Oct":
        return "10"
    elif month == "Nov":
        return "11"
    elif month == "Dec":
        return "12"


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./images/news.png"))
instance = myApp()
app.exec_()
