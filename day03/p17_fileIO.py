# file: p17_fileIO.py
# desc: 파일 입출력 학습

# 컴퓨터에서 열면 무조건 닫아야 하는 것들이 3가지 있다.
"""
1. 파일 : open() -> close() 파이썬에서만 안 닫아도 크게 지장이 없다.
2. 통신 : open() -> close()
3. DateBase : open() -> close()
"""

import os

os.system("clear")

# 파일 객체 생성(언어체계 추가 해야한다 !! 기본값은 ASCII, 유니코드는 utf-8)
# 상대경로, 절대경로 : 절대경로는 / 시작, 상대경로는 ../(부모 디렉터리) ./(현재 디렉터리)로 시작
f = open("./day03/cristiano.txt", mode="w", encoding="utf-8")

# 파일 쓰기 진행
f.write("Football is Ronaldo\n")
f.write("갓두")

# 파일 객체 종료
f.close()
