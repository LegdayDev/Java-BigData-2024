# file: p34_addrBook.py
# desc: 주소록 앱


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
    (name, phoneNumber, eMail, addr) = input(
        "주소록 입력(이름, 핸드폰, 이메일, 주소[구분자는 /]) >>"
    ).split("/")
    name = name.strip()
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    print(f'"{name}", "{phoneNumber}", "{eMail}", "{addr}"')


def displayMenu():
    menu = (
        "주소록 프로그램 V1\n"
        "1. 연락처 추가\n"
        "2. 연락처 출력\n"
        "3. 연락처 삭제\n"
        "4. 종료\n"
    )
    print(menu)
    sel = int(input("메뉴 입력 >> "))
    return sel


def run():
    while True:
        selMenu = displayMenu()
        if selMenu == 4:
            break


if __name__ == "__main__":
    print("프로그램 시작 ")
    run()


print("프로그램 종료")
