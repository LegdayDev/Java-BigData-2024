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


def run():
    first = Contact("Cristiano", "777-7777", "cr7@nate.com", "Manchester")
    print(first)


if __name__ == "__main__":
    print("프로그램 시작 ")
    run()


print("프로그램 종료")
