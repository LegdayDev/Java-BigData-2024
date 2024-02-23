# file: p24_jeep.py
# desc: 클래스 상속

import os
from p22_carClass import Car

os.system("clear")


class Jeep(Car):  # 상속 : Car 클래스를 상속받는다.
    __fuelRate = 0.0  # 연비
    carNum = ""

    def setFuelRate(self, rate):
        self.__fuelRate = rate

    def getFuelRate(self) -> float:
        return self.__fuelRate

    def getCarNum(self) -> str:  # 오버라이딩
        return f"소중한 제 차는 {super().getCarNum()} 에요~"


myCar = Jeep("Rubicon")
print(myCar)

myCar.setFuelRate(12.5)
print(f"내 차의 연비는 {myCar.getFuelRate()} km/l 입니다.")
print(myCar.getCarNum())
