# file: calc.py
# desc: 모듈 만들기

# 모듈을 클래스로 만들 필요는 없다, 함수만 있어도 상관없다.
print(f'calc.py 의 __name__ : {__name__}')

def add(a, b):
    return a + b

def mul(a, b):
    return a * b
