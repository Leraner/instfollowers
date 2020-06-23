import json
import requests
import time
from bs4 import BeautifulSoup as bs


followers = []
followers_after_function = []
index = -1


def parsing(username):
    time.sleep(3)
    headers = {
        'authority': 'www.instagram.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'x-ig-www-claim': 'hmac.AR25C663GaoISsw34AOKajKrq3gSVfpl87zIZ8jP7FTs8Yc1',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'x-ig-app-id': '936619743392459',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://www.instagram.com/{username}/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'ig_did=3E0F79A6-A1B6-4A7C-B022-85323BF49290; mid=Xo2-OwALAAEwhZcC9tn71161Ws4t; shbid=17090; csrftoken=ysnHbkYV4Iqpv4h7g44Q2J44L45gpEPc; ds_user_id=9302714734; sessionid=9302714734^%^3Axnuv5160jwU97k^%^3A23; rur=FTW; shbts=1592767797.1201248; urlgen=^\\^^{^\\^\\^\\^93.185.28.253^\\^\\^\\^:',
    }

    params = (
        ('__a', '1'),
    )

    response = requests.get(f'https://www.instagram.com/{username}/', headers=headers, params=params)

    print(response.text)

    response = json.loads((response.text).encode("utf-16"))

    if response['graphql']['user']['edge_follow']['count'] > 1000:
        result = username + ': ' + str(response['graphql']['user']['edge_follow']['count']) + ' - BOT'
        followers_after_function.append(result)
    else:
        result = username + ': ' + str(response['graphql']['user']['edge_follow']['count'])
        followers_after_function.append(result)

    print(result)

    return result


with open('results.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        followers.append(line)


followers = [line.rstrip() for line in followers]

followers = followers[1::]

try:
    while index <= len(followers):
        index += 1
        print(len(followers), index)
        parsing(followers[index])
except IndexError:
    with open('results.txt', 'w', encoding='utf-8') as f:
        f.write("Количество одинаковых подписчиков: " + str(len(followers_after_function)) + "\n")
        for follower in followers_after_function:
            f.write("%s\n" % follower)
        f.close()

    print('Программа завершила свои действия')