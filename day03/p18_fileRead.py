# file: p18_fileRead.py
# desc: 텍스트 파일 읽기

import os

os.system("clear")

f = open("./day03/cristiano.txt", mode="r", encoding="utf-8")
f2 = open("./day03/dest.txt", mode="w", encoding="utf-8")
# read = f.readline() 내용을 한 줄 읽어온다.

read = f.readlines()  # 전체를 읽어온다. 한줄씩 리스트에 담긴다.

for line in read:  # 한 줄 씩 출력
    print(line.replace("\n", ""))  # 줄 마지막에 \n 이 있기 떄문에 지워줘야한다.
    f2.write(line) # 텍스트 파일 카피

f.close()
f2.close()
