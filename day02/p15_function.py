# file: p15_function.py
# desc: 함수 학습
import os

os.system("clear")


def plus(a, b):  # 매개변수, 리턴값 O
    return a + b


def minus(a, b):  # 매개변수 O , 리턴값 X
    print(a - b)


def multi():  # 매개변수 X , 리턴값 O
    global a, c  # 밖에 있는 전역변수 a, c를 사용
    res = a * c
    return res


def divide():  # 매개변수 X , 리턴값 X
    global a, c
    print(a / c)


def pow(a, b=10):  # 기본인수는 지정할 때 뒤에서부터
    return a**b


a = 10
c = 7

print("더하기")
result = plus(a, c)
print(result)

print("빼기")
minus(a, c)

print("곱하기")
result = multi()
print(result)

print("나누기")
divide()

print(pow(2, 3))
print(pow(2))


def plus_many(*items):  # 동적 매개변수
    result = 0
    for item in items:
        result += item

    return result


print(plus_many(1, 2))
print(plus_many(1, 2, 3, 4, 5, 3, 2))
print(plus_many(1, 2, 3, 5, 13))


def calculator(mode, *args):  # 동적 매개변수를 활용한 계산기 메서드
    if mode == "+":
        result = 0
        for i in args:
            result += i

    elif mode == "-":
        result = args[0]
        for i in args[1:]:
            result -= i

    elif mode == "*":
        result = 1
        for i in args:
            result *= i
    elif mode == "/":
        result = args[0]
        for i in args[1:]:
            result /= i
    return result


print(calculator("+", 4, 6))
print(calculator("-", 10, 40))
print(calculator("*", 4, 25))
print(calculator("/", 10, 3))


def print_kwargs(**items):  # 키워드 매개변수(잘 사용하지 않음), 딕셔너리 생성
    print(items)


print_kwargs(name="Cristiano Ronaldo", age=37, weapon="body")


def calc2(a, b):  ## 리턴값을 여러개 반환
    res1 = a + b
    res2 = a - b
    res3 = a * b
    res4 = a / b

    return res1, res2, res3, res4


print(calc2(10, 4))  # 여러 반환값이 튜플에 담긴다.

pl, mi, mul, di = calc2(1, 2)  # 값을 나눠서 변수에 저장도 가능하다.

print(pl)
print(mi)
print(mul)
print(di)

## 람다함수 ( 함수명 = lambda 매개변수, ... : 실행문)
add = lambda a, b: a + b
print(add(5, 4))

madd = lambda a, *args: [i * 4 for i in args]
print(madd(3, 1, 2, 4))
