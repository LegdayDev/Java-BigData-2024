# file: p19_fileRead.py
# desc: 텍스트 파일 읽기


f = open("./day03/CHANGELOG.md", mode="r", encoding="utf-8")

while True:
    read = f.readline()
    if not read:
        break
    print(read.replace("\n", ""))

f.close()
