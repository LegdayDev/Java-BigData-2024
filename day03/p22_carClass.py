# file: p22_carClass.py
# desc: 객체지향 클래스 학습


class Car:
    __carNum = ""  # 변수명 앞에 __ 이 오면 private 변수
    company = "JEEP"
    releaseYear = 2022
    color = "red"
    carType = "offload"
    fuelType = "gasoline"

    # __메서드명__ 은 매직매서드이다.
    def __init__(self, carNum) -> None:  # 생성자( -> 은 반환타입)
        self.__carNum = carNum
        print(f"{self.__carNum} 객체를 생성합니다.")

    def __str__(self) -> str:  # Java에 toString() 과 비슷해보인다.
        return f"내 차는 {self.company}, {self.__carNum} 입니다~"
    
    def getCarNum(self) -> str:
        return self.__carNum
    
    def getCarColor(self) -> str: # Getter
        return self.__carNum
    
    def setCarColor(self, carNum) -> None: # Setter
        self.__carNum = carNum

    def start(self):
        print(f"{self.__carNum} 차주가 시동을 겁니다")

    def accel(self):
        print(f"{self.__carNum} 차주가 씨게 밟습니다.")

    def stop(self):
        print(f"{self.__carNum} 차주가 급제동을 합니다.")

    def turnLeft(self):
        print(f"{self.__carNum} 차주가 좌회전(?)을 합니다.")

    def turnRight(self):
        print(f"{self.__carNum} 차주가 우회전(?)을 합니다.")
