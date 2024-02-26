# file: p31_externalLib.py
# desc: 외부라이브러리 사용법

from faker import Faker  # Faker : 가짜 객체

fake = Faker("ko-KR")
print(fake.name())
print(fake.address())

dummyDate = [(fake.profile()) for _ in range(10)]
print(dummyDate)


## 내부 라이브러리중 웹사이트 데이터
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.naver.com')

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
