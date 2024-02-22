# file: p11_whileCondition.py
# desc: while 반복문

# 기본구조
"""
while 조건문:
    실행문
    실행문
"""

hit = 0

while hit < 20:  # while 다음에 오는 문장이 True 인 경우에만 실행
    hit += 1
    if hit % 3 == 0:
        continue  ## 아래 실행문을 무시하고 다음 반복
    else:
        print(f"나무를 {hit:02d}번 찍었습니다.")

    if hit == 10:
        print("나무가 넘어갑니다")
        break  # 반복문 탈출

## 무한 루프
hit = 0
# while True:
#     hit += 1
#     print(f"나무를 {hit:02d}번 찍었습니다.")

import os

while True:
    os.system("clear")
    select = input("메뉴입력 1.입력 , 2.수정 , 3.검색 , 4.삭제 , 5.종료 > ")

    if select == "1":
        print("데이터 입력")
        input() 
    elif select == "2":
        print("데이터 수정")
        input()
    elif select == "3":
        print("데이터 검색")
        input()
    elif select == "4":
        print("데이터 삭제")
        input()
    elif select == "5":
        print("데이터 종료")
        break
    else:
        print("입력 오류")
        continue
