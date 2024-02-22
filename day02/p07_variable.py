# file: p07_variable.py
# desc: 변수에 대하여

from copy import copy

a = [1, 2, 3]
print(id(a))

b = a  # 얕은 복사(같은 주소를 공유)
print(id(b))

# del b[2]
# print(a)

d = copy(a) # 깊은 복사(값만 복사하여 서로 다른 주소를 공유)
print("d의 id 값 : ", id(d))
print("a의 id 값 : ", id(a))
