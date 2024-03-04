# file: p50_mouseAuto.py
# desc: PyAutoGui 로 마우스 조작하기

## PyAutoGui 설치 명령어 : pip3 install pyautogui
## Python 이미지 라이브러리 명령어 : pip3 install pillow

import pyautogui as auto

print(auto.size())  # 현재 모니터 해상도

print(auto.position())  # 현재 마우스 커서 위치(좌측상단이 0,0)

## PyAutoGui 설정창 : 맥에서는 RGB가 안됨
auto.mouseInfo()

## 마우스 이동(절대 좌표) : moveTo(0,0) 은
## auto.FAILSAFE = False 선언 시 0,0 가능(단, 권장하지 않음)
auto.moveTo(10, 10)
auto.moveTo(474, 77, duration=1.0)

## 마우스 이동(상대 좌표)
auto.move(500, 400, duration=1.5)

## 마우스 클릭
auto.leftClick(x=474, y=77) # 파라미터 값이 없으면 현재 마우스위치에서 클릭
auto.rightClick(x=700, y=300) # 해당 좌표에서 우클릭
auto.click(clicks=3, interval=0.1, button="left")

##  마우스 드래그 378,217 -> 935,762
auto.leftClick(x=378, y=217, duration=1.0)
auto.dragTo(x=935, y=762, duration=2.0, button="left")

auto.dragRel(500, 400, duration=1.0, button="left") # 상대좌표 드래그

## 마우스 휠
auto.scroll(10) # 양수는 위
auto.scroll(-5) # 음수는 아래
