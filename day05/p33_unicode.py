# file: p33_unicode.py
# desc: ASCII 코드 UNICODE 설명

a = "Life is short, you need python"
print(a)
print(type(a))

b = a.encode("utf-8")  # 문자열앞에 b가 생기고 ' 로 감싸진다(바이너리 코드로 변환)
print(b)
# 타입은 bytes(2진수 데이터) : 네트워크로 데이터 전송, DB 저장 등 데이터 전송에 최적화된 타입이다.
print(type(b))

c = a.encode("euc-kr")  # 한글 체계 cp949(=euc-kr)로 변환
print(c)
print(type(c))

print(b.decode("utf-8")) # UNICODE 를 UTF-8로 디코딩
