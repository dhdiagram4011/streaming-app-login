# curl -X POST "http://apis.aligo.in/send/" \
# 	--data-urlencode "key=eqsuxrlee16gdfcj3u5j8j4qvq70brkn" \
# 	--data-urlencode "user_id=dhdiagram" \
# 	--data-urlencode "sender=01000000000" \
# 	--data-urlencode "receiver=0100000000,0100000000" \
# 	--data-urlencode "destination=0100000000|홍길동" \
# 	--data-urlencode "msg=%홍길동%님! 안녕하세요. API TEST SEND 입니다" \
# 	--data-urlencode "title=API TEST 입니다" \
# 	--data-urlencode "rdate=20201010" \
# 	--data-urlencode "rtime=1302" \
# 	--data-urlencode "testmode_yn=Y"

from urllib.request import urlopen
import requests
import json

def msg_sender():

    TEST_URL = 'http://www.google.com'
    response = urlopen(TEST_URL)
    print(response.status)
    API_URL = 'http://apis.aligo.in/send/'
    headers = {'Content-type':'text/plain'}
    data = {
        'key' : 'ubkm32s9fllu6ui96cq7uegwdk0oxhnc',
        'user_id' : 'dhdiagram',
        'sender' : '01021764011',
        'receiver' : '01021764011',
        'destination' : '01021764011|김도형',
        'msg' : print(response.status),
        'title' : 'API TEST 입니다',
        'rdate' : '20201010',
        'rtime'  : '1400',
        'testmode_yn'  : 'Y'
    }

    requests.post(API_URL, data=data)

msg_sender()






