# file: p21_review.py
# desc: 파이썬의 입출력 리뷰

# Q7
f = open("./day03/test.txt", mode="r", encoding="utf-8")
body = f.readline()
print(body)
f.close()

body = body.replace("java", "python")
f = open("./day03/test.txt", mode="w", encoding="utf-8")
f.write(body)
f.close()
