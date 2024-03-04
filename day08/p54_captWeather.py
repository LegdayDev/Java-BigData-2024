# file: p54_captWeather.py
# desc: 네이버 날씨 화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

# auto.mouseInfo()

regions = ["서울", "강원", "대전", "대구", "부산"]
auto.moveTo(391, 246, duration=0.5)  # 검색창 이동

for region in regions:
    auto.moveTo(165, 179, duration=0.5)  # 검색창 이동
    auto.leftClick()
    for i in range(5):  # 검색창 비우기
        auto.press("backspace")
    time.sleep(0.2)

    clip.copy(f"{region} 날씨")
    auto.hotkey("command", "v")
    time.sleep(0.2)

    auto.press("enter")
    time.sleep(1.0)

    startX, startY = 31, 299
    endX, endY = 701, 944

    img = auto.screenshot(region=(startX, startY, endX - startX, endY - startY))
    img.save(f"./images/day08Img/{region}날씨.png")
