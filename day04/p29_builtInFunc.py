# file: p29_builtInFunc.py
# desc: 내장함수
from os import system

system("clear")

## abs() : 절댓값
print(abs(-6))

## all() : 컬렉션(반복 가능한 데이터->List, Tuple, Dict)의 요소 중 참인 값이 있으면 True
print(all([1, 2, 3]))  # True
print(all([1, 2, 3, 0]))  # False

## chr() : ASCII 나 유니코드 값을 받아서 문자로 변경
print(chr(65))  # A 반환
print(chr(97))  # a 반환

## ascii() : 영문자,문자를 ASCII 코드와 유니코드 숫자로 변경
print(ascii("가"))

## dir() : 객체가 지닌 변수, 함수를 알려준다.
print(dir(str()))

## divmod() : 나눗셈 연산의 몫과 나머지를 튜플로 리턴해준다.
print(divmod(7, 2))  # 7/2 의 몫 3과 나머지 1을 튜플로 리턴

## ★ enumerate() : 데이터를 열거해준다.(데이터와 인덱스를 같이 묶어준다.)
for i in ["Hello", "I',m", "CR7"]:
    print(i)

for i, data in enumerate(["Hello", "I',m", "CR7"]):
    print(f"{i} 번째 데이터는 {data} 입니다.")

## eval(uate) : 실행함수, 문자열로 된 수식,함수를 실행해주는 역할
print(eval("divmod(10,3)"))

## hex() : 10진수를 16진수로 변환
print(hex(255))  # 0x로 시작하는 데이터출력
print(hex(255).upper)  # 대문자로 바꿔서 출력

## oct() : 10진수를 8진수로 변환
print(oct(34))  # 0o로 시작한다.


## ★ map() : 여러값을 한꺼번에 같은 조건으로 변경할 때
def tTime(x) -> int:
    return x * 2


print(
    list(map(tTime, [1, 3, 5, 7, 9]))
)  # [1,3,5,7,9] 에 tTime()에 넣어 2씩 곱하고 다시 list 로 바꾼다.

## max(), min() : 최댓값,최소값
print(max([3, 5, 10, -99]))
print(min([3, 5, 10, -99]))

## ord() == ascii()
print(ord("A"))
print(ord("가"))

## round() : 반올림 함수
print(round(4.6))

## sum() : 컬렉션 요소의 합을 출력
print(sum([1, 2, 3, 4, 5]))
print(sum((1, 2, 3, 4, 5)))
print(sum(range(1, 101)))

## tuple() : 다른 컬렉션을 tuple 로 변환
print(tuple([1, 1, 2, 2, 3, 3, 4, 4, 5]))

## type() : 데이터의 타입을 리턴
print(type("Hello"))  # <class typea명> 반환
print(type([1, 2, 3, 4]))

## zip() : 동일한 갯로 데이터를 묶어서 리턴(두개의 컬렉션의 길이가 일치하는 것 까지만 묶어준다.)
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
normal = [10, 14, 33, 206, 330]

total = list(zip(odd, even, normal))  # 같은 인덱스를 튜플로 묶어서 list로 형변환
print(total)
