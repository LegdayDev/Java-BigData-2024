# file: naverSearch.py
# desc: 네이버 검색 API 전용 클래스
import datetime
import json
from urllib.request import Request, urlopen
from urllib.parse import quote # 유니코드로 인코딩
import ssl


class NaverSearch:
    def __init__(self) -> None:
        print("naver API 클래스 생성")

    # URL 로 검색시작함수
    def getRequestUrl(self, url):
        req = Request(url)
        req.add_header("X-Naver-Client-Id", "sCtc4lOTO75xcfkiqW9c")  # Client ID
        req.add_header("X-Naver-Client-Secret", "D0VAxU8YB6")  # Client PW
        ssl._create_default_https_context = ssl._create_unverified_context

        try:
            res = urlopen(req)
            if res.status == 200:
                print(f"[{datetime.datetime.now()}] : URL 요청 성공")
                return res.read().decode("utf-8")
        except Exception as e:
            print(f"[{datetime.datetime.now()}] : URL 요청 오류 !! {e.args}")
            return None

    # 실제 동작함수
    def getSearchResult(self, searchWord):
        baseUrl = "https://openapi.naver.com/v1/search/news.json"
        params = f"?query={quote(searchWord)}&start=1&display=20"

        resultUrl = baseUrl + params

        result = self.getRequestUrl(resultUrl)

        if result != None:
            return json.loads(result)
        else:
            return None
