# file: p16_io.py
# desc: 입출력 학습
import os

os.system("clear")

## input() 함수로 받는 데이터는 모두 문자열이다 !!
res = input("인사말을 적어주세요 >> ")
print(res)

## 숫자를 입력받아서 계산할려면 형변환 필요
age = int(input("나이를 적으세요 >> "))
print(age)

num = int(input("나이를 입력하세요 >>"))
print(f"{num} 살 입니다.")

## 입력을 2개 이상 받을 때
(a1, a2, a3) = input("3 값을 입력하시오(구분자는 space) > ").split(" ")
print(f"a1 = {a1}, a2 = {a2}, a3 = {a3}")  # String 타입으로 담긴다.

## 입력받은 여러 값을 int 형으로 담고 싶을 때
(a1, a2, a3) = map(
    int, input("3개의 값을 입력(구분은 spade) >> ").split(" ")
)  # map() 은 list 나 tuple 형변환을 도와준다.
sum = a1 + a2 + a3
print(f"총 합은 = {sum}")
