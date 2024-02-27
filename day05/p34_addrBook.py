# file: p34_addrBook.py
# desc: 주소록 앱

import os


class Contact:  # 주소록 클래스
    __name = ""
    __phoneNumber = ""
    __eMail = ""
    __addr = ""

    def __init__(self, name, phoneNumber, eMail, addr) -> None:  # 생성자
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr

    def __str__(self) -> str:
        return f"이  름 = {self.__name}\n핸드폰 = {self.__phoneNumber}\n이메일 = {self.__eMail}\n주  소 = {self.__addr}"


def setContact():  # 사용자 입력으로 주소록 받기 함수
    (name, phoneNumber, eMail, addr) = input("입력(이름/핸드폰/이메일/주소) >> ").split(
        "/"
    )
    name = name.strip()
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    return Contact(name, phoneNumber, eMail, addr)


def displayMenu():
    menu = (
        "주소록 프로그램 V1.3\n"
        "1. 연락처 추가\n"
        "2. 연락처 출력\n"
        "3. 연락처 삭제\n"
        "4. 종료\n"
    )
    print(menu)
    sel = int(input("메뉴 입력 >> "))

    return sel


def clearConsole():
    cmd = "clear"  # macOs, Linux, Unix 명령어
    if os.name in ("nt", "dos"):  # Windows 명령어
        cmd = "cls"
    os.system(cmd)


def getContact(listContact):
    if len(listContact) == 0:
        print("주소록이 비어있습니다.")
    else:
        for contact in listContact:
            print(contact,'\n')


def run():
    # 연락처를 담을 리스트 생성
    listContact = []
    clearConsole()
    while True:
        clearConsole()
        selMenu = displayMenu()

        if selMenu == 1:  # 연락처 추가
            listContact.append(setContact())
            input("계속하시려면 Enter 키를 누르십시오")
        elif selMenu == 2:  # 연락처 출력
            getContact(listContact)
            input("계속하시려면 Enter 키를 누르십시오")
        elif selMenu == 3:  # 연락처 삭제
            pass
        elif selMenu == 4:  # 종료
            break
        else:
            continue


if __name__ == "__main__":
    print("프로그램 시작 ")
    run()


print("프로그램 종료")
