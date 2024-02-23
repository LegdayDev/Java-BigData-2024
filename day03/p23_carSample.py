# file: p23_carSample.py
# desc: Car클래스 사용해보기
import os
from p22_carClass import Car

os.system("clear")

myCar = Car("Cristiano")  # 클래스를 사용하여 객체 생성 -> 인스턴스

# myCar.carNum = "54라 9595"   값이 제대로 저장이 안된다(__변수라서)
myCar.company = "Jeep"
myCar.fuelType = "Gas"
myCar.carType = "Rubicon"
myCar.color = "Black"
myCar.releaseYear = 2023

print(myCar)  # 클래스에서 __str__() 이 호출

myCar.start()
myCar.accel()
myCar.stop()
myCar.turnLeft()
myCar.turnRight()
