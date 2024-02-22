# file: p10_forCondition.py
# desc: for 반복문

## for 문 형식
"""
for item in 반복할 객체:
    실행문
"""
a = [1, 2, 3]
print(type(a))

for i in [1, 2, 3]:
    print(type(i))

for i in ["one", "two", "three"]:
    print(type(i))

b = [(1, 2), (3, 4), (5, 6)]

for i in b:
    print(type(i))

## 리스트안 튜플이 있을 때 튜플출력할 수 있다.
for first, second in b:
    print(first, second)

## 평균 내기
grade = [90, 80, 50, 70, 10]
sum = 0
for i in grade:
    sum += i

print(sum / len(grade))

## range()
print(range(10))  # range(0,10) 에서 생략된 형태
print(range(0, 10))

for i in range(10):
    print(i, end=", ")
print()

print(list(range(0, 10, 5)))  # 3번째 파라미터는 얼만큼 증감할건지 정하는 수다.
print(list(range(1, 10, 2)))

res = 0
for i in range(1, 11):
    res += i
print(res)

## list comprehension : 여러 조건으로 list 를 대량으로 생성할 때 아주 편리
print([i for i in range(1, 10001)])

print([num * 3 for num in range(1, 1001) if num % 3 == 0])
