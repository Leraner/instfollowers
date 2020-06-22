import json
import requests
import time
from bs4 import BeautifulSoup as bs

url = str(input(''))

headers = {
    'authority': 'www.instagram.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'ig_did=3E0F79A6-A1B6-4A7C-B022-85323BF49290; mid=Xo2-OwALAAEwhZcC9tn71161Ws4t; shbid=17090; csrftoken=ysnHbkYV4Iqpv4h7g44Q2J44L45gpEPc; ds_user_id=9302714734; sessionid=9302714734%3Axnuv5160jwU97k%3A23; shbts=1592767797.1201248; rur=FTW; urlgen="{\\"93.185.28.236\\": 12389}:1jnOrL:KmnZueJhjca0NvZGfp2gSd7pNy4"',
}

response = requests.get(url, headers=headers)

word = 'profilePage_'
data = None

with open('html.txt', 'w', encoding='utf-16') as f:
    f.writelines(response.text)
    f.close()

with open('html.txt', 'r', encoding='utf-16') as f:
    for line in f:
        if word in line:
            data = line
            print(data)
    f.close()


data = data[52:-11]
data_json = json.loads(data)

id = data_json['entry_data']['ProfilePage'][0]['logging_page_id'][12::]
username = str(url[26:-1])

print(id)
print(username)

# word = 'profilePage_'
# data = None
#
# with open('html.txt', 'w', encoding='utf-16') as f:
#     f.writelines(response.text)
#     f.close()
#
# with open('html.txt', 'r', encoding='utf-16') as f:
#     for line in f:
#         if word in line:
#             data = line
#             print(data)
#     f.close()
#
#
# data = data[52:-11]
# data_json = json.loads(data)
#
# id = data_json['entry_data']['ProfilePage'][0]['logging_page_id'][12::]
# username = url[26:-1]
#
# print(id)



# headers = {
#     'authority': 'www.instagram.com',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'accept': '*/*',
#     'x-ig-www-claim': 'hmac.AR25C663GaoISsw34AOKajKrq3gSVfpl87zIZ8jP7FTs8Yc1',
#     'x-requested-with': 'XMLHttpRequest',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
#     'x-ig-app-id': '936619743392459',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': f'https://www.instagram.com/{username}/',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cookie': 'ig_did=3E0F79A6-A1B6-4A7C-B022-85323BF49290; mid=Xo2-OwALAAEwhZcC9tn71161Ws4t; shbid=17090; csrftoken=ysnHbkYV4Iqpv4h7g44Q2J44L45gpEPc; ds_user_id=9302714734; sessionid=9302714734^%^3Axnuv5160jwU97k^%^3A23; rur=FTW; shbts=1592767797.1201248; urlgen=^\\^^{^\\^\\^\\^93.185.28.253^\\^\\^\\^:',
# }
#
# params = (
#     ('__a', '1'),
# )
#
# response = requests.get('https://www.instagram.com/jewmarkesh/', headers=headers, params=params)
#
# response = json.loads((response.text).encode("utf-16"))
#
# print(response['data_json']['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow'])
#
# # data_json['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']
# # data_json['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url']
#
# account_data = response
#
#
#

# with open('yaml.json', 'w') as file:
#     json.dump(response, file)
