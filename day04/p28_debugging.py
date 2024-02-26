# file: p28_debugging.py
# desc: 디버깅 학습, 예외처리 추가


class newCalc:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


while True:
    try:
        select = int(input("메뉴 1.더하기, 2.빼기, 3.곱하기, 4.나누기 >"))
    except:
        print('1~5 까지의 숫자만 입력하세요')
        input('계속하시려면 엔터키를 누르세요')
        continue

    if select == 1:
        try:
            x, y = map(int, input("두 수 입력(정수) >>").split(" "))
        except:
            print('정수만 입력하세요')
            input()
            continue
        calc = newCalc()
        print(f"더하기 결과 : {x} + {y} = {calc.add(x,y)}")
    elif select == 2:
        try:
            x, y = map(int, input("두 수 입력(정수) >>").split(" "))
        except:
            print('정수만 입력하세요')
            input()
            continue
        calc = newCalc()
        print(f"빼기 결과 : {x} - {y} = {calc.minus(x,y)}")
    elif select == 3:
        try:
            x, y = map(int, input("두 수 입력(정수) >>").split(" "))
        except:
            print('정수만 입력하세요')
            input()
            continue
        calc = newCalc()
        print(f"곱하기 결과 : {x} * {y} = {calc.mult(x,y)}")
    elif select == 4:
        try:
            x, y = map(int, input("두 수 입력(정수) >>").split(" "))
        except:
            print('정수만 입력하세요')
            input()
            continue
        if y == 0:
            print("제수에 0을 입력하지 마세요")
            input()
            continue
        calc = newCalc()
        print(f"나누기 결과 : {x} / {y} = {calc.div(x,y)}")
    elif select == 5:
        print("프로그램을 종료합니다.")
        input()  # 임시로 멈춘다.
        break
    else:  # 1~5 이외의 입력값이 들어오면
        continue
