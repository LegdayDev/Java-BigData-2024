# file: p25_usingModule.py
# desc: 모듈 사용하기
import calc

import os
import Math

# import calc as c  # calc.py 파일을 c 라는 별칭 사용
# from calc import mul # calc.py 파일에서 mul 만 사용

os.system("clear")

if __name__ == "__main__":
    print(calc.add(2, 56))

    myMath = Math.Math()
    print(myMath.solv(5))

    print(Math.div(10, 2))


# __name__ 이란? 현재 파이썬 파일을 엔트리 포인트로 설정하는 특별한 변수이다.
"""
처음 실행하는 파이썬 파일이 __name__ 변수에 __main__ 이라는 값이 들어간다.
즉 if __name__ == "__main__" 이라는 뜻은 현재 파이썬파일이 프로그램의 시작점(엔트리 포인트)이 맞는지 판단하는 것
즉 다른 파이썬파일에서 해당 모듈이 불러져도 if __name__ == "__main__" : 밑에 있는 로직은 실행하지 않는다 !!
"""
