# file : p02_number.py
# desc : 숫자형 자료타입 및 연산

# 일반 숫자형
age = 40  # 정수형(int) 변수
taxRate = 8.8  # 실수형(float) 변수
highFloats = 4.24e10  # 지수승(float) 변수

print("나이 : ", age)
print("세금 : ", taxRate)
print("지수값 : ", highFloats)

# 틀수 숫자형
binVal = 0b11111111  # 10진수 : 255
octVal = 0o11  # 8진수 : 001(1)001(1) -> 8
hexVal = 0xFF  # 16진수 : F는 15이다. 1111(F)1111(F) -> 255

print("2진수 : ", binVal)
print("8진수 : ", octVal)
print("16진수 : ", hexVal)

# 정리 : 타입을 따로 선언하지 않아도 값에 따라 타입이 정해진다.

a, b, c = 3, 4, 5
print("a + b = ", (a + b))
print("a - b = ", (a - b))
print("a * b = ", (a * b))

# 단, 나눗셈 연산은 3가지로 분류된다.
print("c / b = ", (c / b))  # 정확하게 연산하여 실수로 반환
print("c // b = ", (c // b))  # // 연산자는 몫만 반환한다.
print("c % b = ", (c % b))  # % 연산자는 나머지만 반환한다.

print("2의 10 승 = ", 2**10)  # ** 연산자는 거듭제곱을 반환한다(pow() 와 동일)

# 연산자 우선순위는 () 를 이용하여 우선순위를 정해주면 된다 !!