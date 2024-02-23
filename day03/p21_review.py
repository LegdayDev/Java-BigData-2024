# file: p21_review.py
# desc: 파이썬의 입출력 리뷰
import os

os.system("clear")

# Q7
f = open("./day03/test.txt", mode="r", encoding="utf-8")
body = f.read()
print(body)

f.close()

body = body.replace("java", "python")

f = open("./day03/test.txt", mode="w", encoding="utf-8")
f.write(body)
f.close()


# Q1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False


# Q2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)


avg_numbers(1, 2)
avg_numbers(1, 2, 3, 4, 5)

# Q3
inputData = map(int, input("두 개의 수를 입력하시오(구분값 space) >> ").split(" "))
res = 0
for i in inputData:
    res += i
print(f"두 수의 합은 {res}")

# Q4
print("you", "need", "python")

# Q5
f1 = open("test.txt", mode="w")
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", mode="r")
print(f2.read())

# Q6
user_input = input("저장할 내용을 입력하세요 : ")
f = open("test.txt", "a")
f.write(user_input)
f.write("\n")
f.close()
