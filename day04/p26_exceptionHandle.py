# file: p26_exceptionHandle.py
# desc: 예외 처리
# 오류(Error) : 코드에 빨간색(노락색) 밑줄이 그어지는 것
# 예외(Exception) : 프로그램 실행 중에 생기는 오류(비정상적 종료)

try:
    f = open("./sanple.txt", mode="r", encoding="utf-8")  # FileNotFoundError 예외
    res = f.readline()
    print(res)
except:
    print("FileNotFoundError 예외발생 !!")
else: # else : 오류가 없는 경우에만 실행
    f.close() #
# finally: # finally : 반드시 실행
#     try: # try-except 를 많이 쓰면 성능이 안좋아진다.
#         f.close()
#     except NameError as e:
#         print(f"{e.args[0]} 예외 발생 !!")

# else: # 오류가 없는경우만 수행
#     f.close()

try:
    print(6 / 0)  # ZeroDivisionError 예외
except ZeroDivisionError as e:
    print(f"{e.args} 예외발생 !!")

a, b = 5, 3

if a > b:
    print(True)
