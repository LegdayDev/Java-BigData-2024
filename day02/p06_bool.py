# file : p06_bool.py
# desc : 불(bool)타입, 특수타입(None) 학습

## bool 타입(True or False) 선언 및 출력
a = True
b = False

print(a)
print(b)

## type() 함수를 사용하면 변수의 타입을 알 수 있다.
print(type(a))
print(type(1))
print(type(1.3))
print(type("Hello"))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 4}))
print(type({"name": "hello", "age": 178}))

print(a == b)
print(a == (not b))

print(bool(1))
print(bool(0))  # 0 은 False 그 이외의 숫자는 True
print(bool(3))

print(bool([]))  # 빈 값은 False
print(bool([1, 3]))

print(bool(None))  # None 값은 False

## None 타입
None

c = None
print(c)
print(a + b)  # True + False 는 True(1)
# print(c + a) None 에 값을 더할 수 없다.
