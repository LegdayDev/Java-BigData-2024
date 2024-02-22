# Java BigData 2024
## 1 일차
### 파이썬 개발환경 설정
> - [Git](https://git-scm.com/) 세팅 및 [GitHub](https://github.com/) 가입
> - [Github Desktop](https://desktop.github.com/?ref_cta=download+desktop&ref_loc=installing+github+desktop&ref_page=docs) 설치 및 세팅
> - [Python](https://www.python.org/) 설치
> - [VS code](https://code.visualstudio.com/) 설치
> - [D2coding](https://github.com/naver/d2codingfont) 폰트 세팅
### Python 학습 
> 1.  Python 개요
> 2. Python 기초 문법 : 기본 자료형 , 문자열 자료형 , 리스트 , 튜플

#### 기본 자료형
- <span style="color:olivedrab">_타입을 적지 않아도 값에 따라 타입이 정해진다._</span>
    ```python
    a = 3 # 정수형
    b = 3.14 # 실수형
    ```
#### 문자열 자료형
- `""`(쌍따옴표) or `''`(홀따옴표) 구분없이 문자열을 감쌀 수 있다.
- 인덱싱은 `[위치값]` 으로 접근 가능하지만 문자열 수정은 안된다 !!
    - `list[0]`
- 슬라이싱은 `변수명[시작위치:끝위치]` 를 이용하여 짤라서 출력한다.(-를 붙히면 뒤에서 부터 카운팅)
- `format()` 함수를 사용하면 포맷팅이 가능하다.
    ```python
    temp = 21
    print("현재 온도는 %d도 입니다." % temp)
    ```
- python 3.6 부터는 `f 포맷팅`이 가능하다.
    ```python
    ## f 포맷팅 ( Python 3.6 이상 지원 )
    name = "Cristiano"
    age = 37

    cont = f"나는 {name}이고, 나이는 {age}세 입니다."
    print(cont)
    ```
- 문자열 함수는 `count()` , `find()` , `index()` , `join()` , `lower()` , `upper()` 등등이 있다.
    - <span style="color:indianred">***외우지 말고 한 번 눈으로 훑고 필요할 때마다 찾아쓰면 된다.***</span>
#### 리스트와 튜플
- 리스트는 다른 프로그래밍 언어의 배열과 같다 !!
    - `list = [1,4,5]`
    - `list = [1,"hi",True,None]` : <span style="color:slateblue">_꼭 같은 타입의 원소로 이루어져 있지 않아도 된다 !!_</span>
- 인덱싱과 슬라이싱은 문자열과 똑같이 사용하면 된다.
- *2차원 배열*은 [] 안에 [] 를 넣어주면 된다. 즉, <span style="color:olivedrab">_리스트안에 리스트를 넣는 것이다_</span>
    ```python
    ## 2차원 리스트
    d2Datas = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(d2Datas)
    ```
- 리스트의 함수는 아래와 같다.
    - `append(value)` : 리스트 맨 뒤에 원소 추가
    - `insert(index, value)` : 특정 위치에 값을 추가
    - `sort()` : 오름차순
    - `sort(reverse=True)` : 내림차순
    - `reverse()` : 역순
    - `count()` : 단어 갯수
    - `index()` : 단어 위치 반환
    - `remove(value)` : value 1개만 삭제
    - `pop()` : <span style="color:slateblue">_맨 마지막 원소 출력 후 삭제_</span>
- <span style="color:indianred">***튜플은 리스트와 똑같다. 하지만 수정,삭제가 안된다 !!***</span>

## 2일차
### Python 학습
> 1. 딕셔너리 집합
> 2. 불(bool)형
> 3. None형
> 4. 제어문(if , for , while)
> 5. 제어문 연습
> 6. 함수

#### 딕셔너리
- Key 와 Value 가 한 쌍으로 이루어진 자료형
    ```python
    spiderMan = {
        "name": "Cristiano Ronaldo",
        "age": 37,
        "weapon": "Body",
        "friends": ["Messi", "Neymar", "Park"],
    }
    ```
- `items()` : 모든 아이템 출력
- `get(key)` : 딕셔너리 Value 가져오기
- `clear()` : 데이터 모두 삭제
- `del` : 객체 자체를 삭제
#### 불(bool)형과 특수타입(None)
- Python 에서 bool 타입은 **참/거짓을 판별하는 자료형**이다.
- 다른 프로그래밍 언어와 다르게 `True / False` 로 구분된다.
- `None` 은 `Null` 과 똑같은 의미를 가진다.
#### 제어문
- if문
    ```python
    if money == True:
        # indentation(들여쓰기) : 파이썬에서 들여쓰기르 잘 못하면 에러가 뜬다.
        print("택시타고 가")
    elif money < 5000 and money >= 2500:  # Python 에서 else 는 elif 로 쓴다.
        print("중간에 내릴게요")
    else:
        print("뛰어가")
    ```
- for문 : `range()` 함수를 자주 쓴다.
    - range(시작값, 끝값, 증감값) 이 기본이며 시작값과 증감값을 생략하면 0부터 시작해서 1씩 증가한다.
    ```python
    grade = [90, 80, 50, 70, 10]
    sum = 0
    for i in grade:
        sum += i
    ```
- `list comprehension` : 여러 조건으로 list 를 대량으로 생성할 떄 유용
    ```python
    print([i for i in range(1, 10001)])

    print([num * 3 for num in range(1, 1001) if num % 3 == 0])
    ```
#### function(함수)
- 반환타입 없이 `def` 키워드를 사용하여 선언
- 동적 매개변수
    ```python
    def plus_many(*items):  # 동적 매개변수
        result = 0
        for item in items:
            result += item

        return result
    ```
- `람다(lambda)`함수
    ```python
    add = lambda a, b: a + b
    print(add(5, 4))

    madd = lambda a, *args: [i * 4 for i in args]
    print(madd(3, 1, 2, 4))
    ```