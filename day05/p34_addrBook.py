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

    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False

    def getInfo(self):
        return self.__name, self.__phoneNumber, self.__eMail, self.__addr


def setContact():  # 사용자 입력으로 주소록 받기 함수
    (name, phoneNumber, eMail, addr) = input("입력(이름/핸드폰/이메일/주소) >> ").split(
        "/"
    )
    name = name.strip()
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    return Contact(name, phoneNumber, eMail, addr)


def getContact(listContact):
    if len(listContact) == 0:
        print("주소록이 비어있습니다.")
    else:
        for i, contact in enumerate(listContact):
            print(f"<<<<<<< {i+1} 번째 데이터 >>>>>>>")
            print(contact, "\n")


def delContact(list, name):
    for i in range(len(list) - 1, -1, -1):  # 리스트를 내림차순으로 뒤에서부터 삭제
        item = list[i]
        if item.isNameExist(name):
            del list[i]


def saveContact(list):  # 연락처 저장 함수
    with open("./contacts.txt", mode="w", encoding="utf-8") as fp:
        for item in list:
            name, phoneNumber, eMail, addr = item.getInfo()
            fp.write(f"{name}/{phoneNumber}/{eMail}/{addr}\n")


def loadContact(list):
    try:
        with open("./contacts.txt", mode="r", encoding="utf-8") as fp:
            while True:
                line = fp.readline()
                if not line:
                    break

                lines = line.replace("\n", "").split("/")  # list
                contact = Contact(
                    name=lines[0], phoneNumber=lines[1], eMail=lines[2], addr=lines[3]
                )
                list.append(contact)
    except:  # 연락처 파일이 없으면 빈 파일을 새로 만든다.
        print("빈 파일 출력")
        f = open("./contacts.txt", mode="w", encoding="utf-8")
        f.close()


def displayMenu():
    menu = (
        "주소록 프로그램 V1.4\n"
        "1. 연락처 추가\n"
        "2. 연락처 출력\n"
        "3. 연락처 삭제\n"
        "4. 종료\n"
    )
    print(menu)
    try:
        sel = int(input("메뉴 입력 >> "))
    except:
        sel = 0

    return sel


def clearConsole():
    cmd = "clear"  # macOs, Linux, Unix 명령어
    if os.name in ("nt", "dos"):  # Windows 명령어
        cmd = "cls"
    os.system(cmd)


def run():
    # 연락처를 담을 리스트 생성
    listContact = []
    loadContact(listContact)  # 저장되어있던 연락처를 로딩한다.
    clearConsole()
    while True:
        clearConsole()
        selMenu = displayMenu()

        if selMenu == 1:  # 연락처 추가
            clearConsole()
            try:
                contact = setContact()
            except:  # 입력을 시킨대로 안하면
                contact = None
            if contact != None:
                listContact.append(contact)
                input("연락처 추가 성공!! Enter키를 누르십시오")
            else:
                input("연락처 입력 실패!! Enter키를 누르십시오")
        elif selMenu == 2:  # 연락처 출력
            clearConsole()
            getContact(listContact)
            input("연락처 출력 성공!! Enter키를 누르십시오")
        elif selMenu == 3:  # 연락처 삭제
            clearConsole()
            name = input("삭제할 이름 입력 >> ")
            delContact(listContact, name)
            input("연락처 삭제 성공!! Enter키를 누르십시오")
        elif selMenu == 4:  # 종료
            print(f"list 길이는 {len(listContact)}")
            saveContact(listContact)
            break
        else:
            continue


if __name__ == "__main__":
    print("프로그램 시작 ")
    run()


print("프로그램 종료")
