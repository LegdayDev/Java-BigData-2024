# file: p57_mailReceive.py
# desc: 네이버 메일 알림을 슬랙으로 전송

"""
순서
1. 네이버 메일 -> 환경설정 -> IMAP/SMTP 설정 -> 사용함 
"""

import imaplib
import email
from email import policy
import requests
import json

slack_url = "Slack API 주소"

def sendToSlack(msg):
    headres = {"Content-type": "application/json"}
    data = {"text": msg}
    res = requests.post(slack_url, headers=headres, data=json.dumps(data))
    
    if res.status_code == 200:return "OK"
    else:return "Error"

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode


imap = imaplib.IMAP4_SSL("imap.naver.com")  # IMAP 서버명
id = "chlwodud0327"
pw = "네이버 비밀번호"  # TODO Github 올리기전에 가리기

res = imap.login(id, pw)

if res[0] == "OK":
    imap.select("INBOX")
    resp, data = imap.uid("search", None, "All")
    allEmails = data[0].split()
    lastEmails = allEmails[-5:]

    for mail in lastEmails:
        result, data = imap.uid("fetch", mail, "(RFC822)")
        rawEmail = data[0][1]
        emailMessage = email.message_from_bytes(rawEmail, policy=policy.default)

        eamilFrom = str(emailMessage['From'])
        emailDate = str(emailMessage['Date'])

        subject, encode = find_encoding_info(emailMessage['Subject'])
        subject = str(subject)
        if subject.find('중요') >= 0:
            slackMessage = f'{eamilFrom}\n{emailDate}\n{subject}'
            resCode = sendToSlack(slackMessage)
            if resCode == "OK":
                print(f'{subject} 메일 슬랙 전송 성공!!')
            else:
                print(f'{subject} 메일 슬랙 전송 실패!!')
        else:
            print('중요하지 않은 메일이 왔음')

        '''
        print('='*80)
        print(f'FROM : {emailMessage['From']}')
        print(f'TO : {emailMessage['TO']}')
        print(f'DATE : {emailMessage['DATE']}')

        subject, encode = find_encoding_info(emailMessage['Subject'])
        print(f'Subject : {subject}')
        
        슬랙으로 알림을 보낼땐 내용은 필요없다.
        print(f'내용 : ')
        msg = ''
        if emailMessage.is_multipart(): # multipart 형식까지 포함된 메일인가?
            for part in emailMessage.get_payload():
                if part.get_content_type() in['text/plain','text/html'] :
                    bytes = part.get_payload(decode=True)
                    encode = part.get_content_charset()
                    msg = msg + str(bytes, encode) # 인코딩을 자신의 언어로 변경
        else: # multipart 형식이 아닌경우
            part = emailMessage.get_payload() # HTML 형식으로 가져온다.
            print(part)
        '''
        
imap.close()
imap.logout()
