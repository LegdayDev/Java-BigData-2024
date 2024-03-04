# file: p55_slackMsg.py
# desc: 슬랙으로 메시지 보내기
'''
순서
1. https://api.slack.com/ 에서 Your apps -> Create your first app 
2. From Search 클릭 -> app name 은 영어로만 !!
'''


import requests
import json

slack_url = "슬랙 API 주소"

headres = {"Content-type": "application/json"}
data = {"text": "Messi!!"}

res = requests.post(slack_url, headers=headres, data=json.dumps(data))

if res.status_code == 200:
    print("메시지 전송 성공 !!")
else:
    print("메시지 전송 실패 !!")
