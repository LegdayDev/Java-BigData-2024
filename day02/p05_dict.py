# file: p05_dict.py
# desc: 딕셔너리 자료형 , 집합(잘 사용하지 않는다.)
"""
말 그대로 '사전' 이라는 뜻. Key 와 Value가 한 쌍으로 이루어진 자료형.
Key 값은 중복이 안된다. Key 는 문자로 쓰는게 국룰.
"""


## 딕셔너리 정의 및 출력
spiderMan = {
    "name": "Cristiano Ronaldo",
    "age": 37,
    "weapon": "Body",
    "friends": ["Messi", "Neymar", "Park"],
}

print(spiderMan)  # 전체 출력
print(spiderMan["age"])  # Value 출력은 Key 값으로 접근하면 된다.

## 딕셔너리 값 추가
spiderMan["job"] = "Football Master"

print(spiderMan)

## 딕셔너리 값 삭제
del spiderMan["friends"]
print(spiderMan)

## 딕셔너리 관련 함수
### keys() : 딕셔너리의 Key 들을 `dict_key([key, key, ...])` 형식으로 출력
print(spiderMan.keys())
print(list(spiderMan.keys()))  # 리스트형태로 형변환

### items() : 딕셔너리 모든 아이템 출력
print(spiderMan.items())

### get(key) : 딕셔너리의 Value 가져오기
print(spiderMan.get("job"))

### in : 딕셔너리안에 키가 있는지 확인(반환 값은 True , False)
print("friends" in spiderMan)

### pop() : 마지막 값을 반환 후 삭제
res = spiderMan.pop("job")
print(res)
print(spiderMan)

### clear : 데이터를 모두 삭제
spiderMan.clear()

### del : 객체 자체를 삭제
del spiderMan
print(spiderMan)

## 집합 : 중복허용X , 순서X