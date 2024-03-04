# file: p58_ocr.py
# desc: 이미지 내 글자 인식

"""
명령어 
1. brew install tesseract -> 터미널
2. brew install tesseract-lang -> 터미널(한국어다운)
3. pip3 install pytesseract -> VS Code
4. Brew list tesseract -> tesseract 위치기억하고 tesseract_cmd 변수에 저장(권한이 없으면 chmod 로 권한풀기)
5. PermissionError -> chomod 775 tesseract경로
"""

from PIL import Image  # 이미지 가져오는 모듈
import pytesseract as pt

imgPath = "./images/day08Img/originalImage.png"
im = Image.open(imgPath)
im.show()

pt.pytesseract.tesseract_cmd = "/opt/homebrew/Cellar/tesseract/5.3.4_1/bin/tesseract"
text = pt.image_to_string(Image.open(imgPath), lang="kor")

print(text)
