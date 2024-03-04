# file: p51_keyboardAuto.py
# desc: PyAutoGui 로 키보드 조작하기

import pyautogui as auto
import pyperclip as clip  # 한글 입력을 위한 모듈

# auto.mouseInfo()

## 특정 위치에 클릭 후 문자입력
auto.write('print("Cristiano Ronaldo is Football Master")')

## 키보드 프레스 기능
auto.press("enter")

## 키보드 단축키로 입력
# auto.hotkey("command", "a")
# auto.hotkey("command", "c")

# auto.press("\n")
# auto.press("\n")
# auto.press("\n")
# auto.press("\n")

# auto.hotkey("command", "v")

# auto.hotkey("command", "v")
# auto.hotkey("command", "v")
clip.copy("print('안녕하세요 탁구선수 이강인입니다.')")  # 클립보드에 한글 내용을 저장
auto.hotkey("command", "v")  # 클립보드에 복사된 한글을 붙혀넣기
