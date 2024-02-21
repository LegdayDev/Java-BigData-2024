# file : p03_string.py
# desc : 문자열 자료형

a = "Hello World"
print(a)
b = "Hello World"  # ' 도 문자열을 담을 수 있다.
print(b)

c = "Hello, 'Ashley'"
print(c)  # ""안에 ' 를 쓸 수 있다.(이스케이프 문자도 가능, 단 추천하지 않는다.)

d = """
안녕 하세요 
만나서 반갑습니다.
"""
print(d)  # ' 3개를 이용하면 문자블럭도 가능하다. \(역슬래쉬)를 쓰면 문장이 붙혀진다.

## 문자열 연산 :  + , *
before = "I wanna go to "
after = "Boracai"

print(before + after)  # 문자열을 + 연산자로 붙혀줄 수 있다.
print(after * 4)  # 문자열을 * 연산자로 반복하여 출력할 수 있다.

## 문자열 길이 구하기 - len()
str = "Cristiano Ronaldo"
print(len(str))

## 문자열 인덱싱과 슬라이싱
cp = "Life is too short, You need Python"

print(cp[8])  # 9번째 문자 출력
# cp[2] = 'd' 와 같이 수정이 안됨. 문자열은 배열이지만 값 변경이 안된다.

# 슬라이싱
print(cp[12:17])  # 12번 인덱스부터 16번 인덱스까지 출력

print(cp[0:7], "long", cp[17:])  # : 뒤를 생략하면 끝까지 출력한다.

print(cp[-11:-8])  # - 를 붙히면 뒤에서부터 카운팅을 한다.

## 문자열 포맷팅(format string) : %d , %s, %c 의 사용빈도가 낮다.
temp = 21
print("현재 온도는 %d도 입니다." % temp)

## format() 함수를 사용한 포매팅
temp = 37.5
print("현재 온도는 {0}도 입니다.".format(temp))

## 날자를 포맷으로 만들 때
month = 2
day = 21
hour = 3
mins = 18
sec = 9
print("오늘은 {0}월 {1}일 {2}시 {3}분입니다.".format(month, day, hour, mins))

print(
    "오늘은 {0:02d}-{1:02d}, {2:02d} : {3:02d}분입니다.".format(
        month, day, hour, mins
    )  # :02d 는 2자리의 정수형으로 맞출 수 있다.
)

## 숫자형 포맷팅
income = 6000000000
print(
    "올해 매출액은 {0:,d} 원입니다".format(income)
)  # 회계에서 사용하는 단위로 3글자씩 , 로 끊는다.

## 소수점 포매팅
PI = 3124.1415926535
print(
    "파이는 {0:0,.2f}".format(PI)
)  # 소수점 앞은 3자리씩 , 구분하고 소수점 뒷자리는 2자리까지만 출력

## f 포맷팅 ( Python 3.6 이상 지원 )
name = "Cristiano"
age = 37

cont = f"나는 {name}이고, 나이는 {age}세 입니다."
print(cont)

name = "Lionel"
age = 35
cont = f"나는 {name}이고, 나이는 {age}세 입니다."
print(cont)

print(f"나는 {name}이고, 나이는 {age:03d}세 입니다")
print(
    f"나는 {name}이고, 나이는 {age:03.1f}세 입니다"
)  # 정수는 f 포맥 가능, 실수는 d 포맷 사용불가

## 문자열 함수
a = "Life is short, You need Python"

print(a.count("Life"))  # 해당 단어의 갯수를 반화
print(a.count("o"))  # 하나의 문자도 찾아서 갯수를 반환

print(a.find("short"))  # 해당 문자의 인덱스 위치를 반환 -> 존재하지 않으면 -1 반환
print(
    a.index("short")
)  # 해당 문자의 인덱스 위치를 반환 -> 존재하지 않으면 ValueError 예외 발생

print(",".join("abcde"))  # 문자열 사이사이에 , 를 넣는다.

print(a.upper())  # 대문자로 변환

b = "LIFE IS SHORT"
print(b.lower())  # 소문자로 변환

print(a.capitalize())  # 문장이 시작되는 첫번째 단어의 첫글자만 대문자

origin = "          Hi         "
print(f"++{origin}++")

## 왼쪽 공백 제거
print(f"++{origin.lstrip()}++")
## 오른쪽 공백 제거
print(f"++{origin.rstrip()}++")
## 공백제거
print(f"++{origin.strip()}++")  # 단, 글자 사이 공백은 못없앤다

## 문자 대체하기
str = "Life is too short, you need Python"
print(str.replace(" too ", " ").replace("Python", "Java"))

## 문자열 자르기
cpWords = str.split(" ") # 기본값은 공백, 문자열을 잘라서 리스트 형태로 반환
print(cpWords)
