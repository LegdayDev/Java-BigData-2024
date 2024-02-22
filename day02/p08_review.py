# file: p08_review.py
# desc: 리뷰 (Q2,Q3,Q5,Q6,Q10)

## Q2번: 홀수, 짝수 판별하기
num = 13
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

## Q3번: 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin.split("-")[0]  # 앞자리
num = pin.split("-")[1]
print(f"19{yyyymmdd}")
print(num)

## Q5번: 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

## Q6번: 리스트 역순 정렬하기
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

## Q10번 : 딕셔너리 값 추출하기
a = {"A": 90, "B": 80, "C": 70}
result = a.pop("B")
print(a)
print(result)
