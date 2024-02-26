# file: p27_exceptionHandle.py
# desc: 예외처리 2(try - except)

# while True:
#     try:
#         select = int(input("메뉴입력 1.저장 , 2.검색, 3.종료 >> "))
#     except:
#         print("예외발생 !!")
#         continue

#     if select == 3:
#         break
#     elif select == 1:
#         print("저장")
#     elif select == 2:
#         print("검색")
#     else:
#         continue

class Chicken:
    def fly(self):
        raise NotImplementedError # rasie 키워드는 예외를 강제로 발생하는 키워드
    
koko = Chicken()
koko.fly()