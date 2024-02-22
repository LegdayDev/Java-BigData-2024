# file: p12_gugudan.py
# desc: 구구단 프로그램

print("구구단 프로그램 V99")
for y in range(2, 10):
    for x in range(1, 10):
        print(f"{x} X {y} = {x*y:2d}", end="\t")
    print()
