### key : da740db95614eda666e49b3c867a0790

import requests
import time

url = 'https://sms.gabia.com/oauth/token'
payload = 'grant_type=client_credentials'
headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Authorization':'Basic 3eef0591ba8d19d91f5e64731893e7ec'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=1)
print(response.text)


# import requests
# import time

# url = 'https://sms.gabia.com/api/send/sms'
# payload = 'phone=01021764011&callback=010217640110&message=SMS%20TEST%20MESSAGE&refkey=[[RESTAPITEST20201026]]'
# headers = {
#     'Content-Type':'application/x-www-form-urlencoded',
#     'Authorization':'Basic DckviEksLs6ZXlKMGVYQWlPaUpLVhiR2NpT2lKU1V6STFOaUo5LmV5SnBjM01pT2lKb2RIUndjenBjTDF3dmMyMXpMbWRoWW1saExtTnZiVnd2SWl3aVlYVmtJam9pWEM5dllYVjBhRnd2ZEc5clpXNGlMQ0pshWFhnT2pBNG5uVkVuLWtnVEJoRGpPeWc='
# }
# response = requests.post(url, headers=headers, data=payload, allow_redirects=False, timeout='3')
# print(response.text)