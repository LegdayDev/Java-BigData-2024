# file : p04_list.py
# desc : 리스트 자료형

## Python 에는 배열이 없다. 리스트(List)로 대신한다.
even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

datas = [
    123,
    45.6,
    True,
    "Hello",
    odd,
    None,
]  # 리스트는 원소들의 타입이 달라도 저장이 가능하다.
print(datas)

print("even 리스트 출력 : ", even)
print("odd 리스트 출력 : ", odd)

## 인덱싱 , 슬라이싱
print(even[4])

even[4] = 20  # 리스트는 인덱스의 값을 변경가능

print(odd[2])

cpWords = ["Life", "is", "short"]
print(cpWords[0] + cpWords[1])  # 인덱스 값 끼리 덧셈가능(같은 타입일 때)

print(even[0:4])  # 슬라이싱도 똑같다.

## 2차원 리스트
d2Datas = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(d2Datas)

for i in d2Datas:
    print(i)

dm1col1 = [1, 2, 3, 4]
dm1col2 = [5, 6, 7, 8]
dm1col3 = [9, 10, 11, 12]
print([dm1col1, dm1col2, dm1col3])

print(even + odd)

## 값 삭제
del even[2]
print(even)

## 리스트 함수
list = [1, 2, 3]

list.append(10)  # append() 리스트 맨 뒤에 원소 추가
print(list)

list.insert(2, 10)  # insert() 특정 위치에 값을 추가한다.
print(list)

origin = [3, 6, 1, 10, 2, 100, 50, 300, -30, 0]

origin.sort()  # sort() 기본값은 오름차순(ASC)
print(origin)

origin.sort(reverse=True)  # 파라미터로 reverse 값을 True 로 하면 내림차순(DESC)
print(origin)

aa = ["a", "d", "f", "e"]
aa.reverse()  # reverse() 는 정렬과 다르게 그냥 역순으로 뒤집는다.
print(aa)

print(aa.count("a"))  # coutn : 단어 갯수 반환
print(aa.index("e"))  # index : 단어 위치 반환

bb = [1, 3, 5, 6, 8, 3, 1]
bb.remove(3)  # 딱 한개만 지운다( 만약 여러개면 여러번 호출해야 한다 )
print(bb)

print(even.pop())  # . pop() 함수는 가장 마지막 원소 출력하고 제거한다.

## 튜플(Tuple) : 리스트와 동일하지만, 삭제/편집 불가능하다 !!!!

tVal = (1, 3, 5, 7, 8)
print(tVal)

# tVal[2] = 11 -> 값 수정시 예외 발생
# del tVal[2] -> 값 삭제시 예외 발생