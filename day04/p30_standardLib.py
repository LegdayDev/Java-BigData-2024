# file: p30_standardLib.py
# desc: 표준 라이브러리(built in) 학습

import datetime  # 날짜
import time
import random

print(datetime.date(2024, 2, 26))  # yyyy-mm-dd 형식으로 출력

# ★많이 사용★
curr = datetime.datetime.now()  # 현재 yyyy-mm-dd h:m:s.ssssss
print(curr)

print(curr.weekday())  # 요일 출력 - 월(0), 화(1), 수(2), 목(3), 금(4), 토(5), 일(6)
print(curr.year)  # 년도만 출력
print(curr.month)  # 월 출력
print(curr.day)  # 일 출력
print(curr.hour)  # 시 출력
print(curr.minute)  # 분 출력
print(curr.second)  # 초 출력

# datetime 활용
print(
    f"오늘은 {curr.year}년 {curr.month:02d}월 {curr.day}일이고 현재 시간은 {curr.hour}시 {curr.minute}분 입니다."
)

curr = time.localtime()  # time 으로 찾는 localtime() 잘 안쓰인다.
print(curr)  # 다양한 변수들이 있다.

# time.sleep(ms) : 정말 많이 쓴다.
# for i in range(0, 5):
#     print(f"{i} 출력")
#     time.sleep(1)  # 1초 멈춤

print(random.random())  # 0 에서 1 사이의 소숫점 난수
print(random.randint(0, 10))  # 0부터 10까지 정수 난수

## 로또
result = []
total = []

for i in range(5):
    while True:
        val = random.randint(1, 45)
        while val not in result:
            result.append(val)
        if len(result) == 6:
            break
    result.sort()
    total.append(result)
    result = []

print(total)
