# file: p09_ifCondition.py
# desc: if 제어문

money = True

if money == True:
    # indentation(들여쓰기) : 파이썬에서 들여쓰기르 잘 못하면 에러가 뜬다.
    print("택시타고 가")
elif money < 5000 and money >= 2500:  # Python 에서 else 는 elif 로 쓴다.
    print("중간에 내릴게요")
else:
    print("뛰어가")

a, b, c, d = 10, 5, 7, 9

print(a >= b)
print(c > d)

print(a >= b and c > d)  # && 연산
print(a >= b or c > d)  ## || 연산

print(not (a >= b))  ## ! 연산

print(1 in [1, 2, 3, 4])  # 우항 안에 좌항이 있으면 True
print(6 in [1, 3, 5, 7, 9])

## print() 함수 옵션들 : sep , end
print("13579", "1011", sep=",")  # sep 구분자
