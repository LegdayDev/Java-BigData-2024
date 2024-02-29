# file: p46_tts.py
# desc: Text To Speech

# pip3 install gTTs
# pip3 install pygame

from gtts import gTTS
import pygame

text = input("텍스트 입력 >> ")

speech = gTTS(text=text, lang="en")
speech.save("./lib/tts.mp3")

pygame.mixer.init()
pygame.mixer.music.load("./lib/tts.mp3")
pygame.mixer.music.play()
