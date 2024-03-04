# file: p52_screenCap.py
# desc: PyAutoGui 로 화면 캡쳐하기

# mac : command + shift + 5

import pyautogui as auto

startX, endX = 0, 1919
startY, endY = 0, 1079

img = auto.screenshot(region=(startX, startY, endX - startY, endY - startY))
img.save("./images/day08Img/scrren.png")
