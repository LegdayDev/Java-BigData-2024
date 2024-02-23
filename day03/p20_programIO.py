# file: p20_programIO.py
# desc: 프로그램 입출력, 프로그램으로 명령 실행 시 파라미터를 받을 수 있음.
import os
import sys

os.system("clear")

args = sys.argv[1:]

# 터미널로 실행해서 파일명 뒤에 명령어를 줄 수 있음.
for i in args:
    # print(i, end=" / ")
    if i == "--version":
        print("Python 3.9.6")
    elif i == "-h":
        print("도움말 >> ")
    else:
        print("재입력")

    break
