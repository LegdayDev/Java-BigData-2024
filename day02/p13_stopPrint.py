# file: p13_starPrint.py
# desc: 별찍기 : 2중 for 문으로 만들기
import os

os.system("clear")
for i in range(1, 6):
    for j in range(i, 6):
        print(" ", end="")
    for j in range(0, i * 2 - 1):
        print("*", end="")
    print()
for i in range(1, 6):
    for j in range(i, 6):
        print(" ", end="")

    for j in range(0, i * 2 - 1):
        print("*", end="")
    print()
for i in range(1, 6):
    for j in range(i, 6):
        print(" ", end="")

    for j in range(0, i * 2 - 1):
        print("*", end="")
    print()
for i in range(1, 4):
    print("     *")
