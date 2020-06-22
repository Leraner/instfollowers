from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from design import Ui_Dialog
import json
import requests
import time
from termcolor import colored
import logging

# Создание приложения

app = QtWidgets.QApplication(sys.argv)

# Создание приложения

# Создание формы и добавление UI

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


# Создание формы и добавление UI

# Логика приложения

def compare_followers():
    index = 0
    after = ""
    followers1 = []
    followers2 = []
    main_running = True
    url = ''
    url1 = ui.lineEdit.text()
    url2 = ui.lineEdit_2.text()


    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename='error.log'

    )

    while main_running:

        if len(url) > 0:
            url = str(url2)
        else:
            url = str(url1)

        headers = {
            'authority': 'www.instagram.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'ig_did=3E0F79A6-A1B6-4A7C-B022-85323BF49290; mid=Xo2-OwALAAEwhZcC9tn71161Ws4t; shbid=17090; csrftoken=ysnHbkYV4Iqpv4h7g44Q2J44L45gpEPc; ds_user_id=9302714734; sessionid=9302714734^%^3Axnuv5160jwU97k^%^3A23; shbts=1591693838.2975924; urlgen=^\\^^{^\\^\\^\\^93.185.28.27^\\^\\^\\^:',
        }

        response = requests.get(f'{url}', headers=headers)

        word = 'profilePage_'
        data = None

        with open('html.txt', 'w', encoding='utf-16') as f:
            f.writelines(response.text)
            f.close()

        with open('html.txt', 'r', encoding='utf-16') as f:
            for line in f:
                if word in line:
                    data = line
            f.close()

        data = data[52:-11]
        data_json = json.loads(data)

        id = data_json['entry_data']['ProfilePage'][0]['logging_page_id'][12::]
        username = url[26:-1]



        cycles_count = 0

        running = False

        if len(followers1) and len(followers2) > 0:
            main_running = False
            running = False
        elif len(id) and len(username) > 0:
            running = True
        else:
            print(colored('Вы ввели что-то неправильно', 'red'))

        while running:
            headers = {
                'authority': 'www.instagram.com',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'accept': '*/*',
                'x-ig-www-claim': 'hmac.AR25C663GaoISsw34AOKajKrq3gSVfpl87zIZ8jP7FTs8fPe',
                'x-requested-with': 'XMLHttpRequest',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                'x-csrftoken': 'ysnHbkYV4Iqpv4h7g44Q2J44L45gpEPc',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': f'https://www.instagram.com/{username}/followers/',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': 'ig_did=3E0F79A6-A1B6-4A7C-B022-85323BF49290; mid=Xo2-OwALAAEwhZcC9tn71161Ws4t; shbid=17090; csrftoken=ysnHbkYV4Iqpv4h7g44Q2J44L45gpEPc; ds_user_id=9302714734; sessionid=9302714734%3Axnuv5160jwU97k%3A23; shbts=1590581290.3389668; urlgen="{\\"93.185.29.181\\": 12389}:1jey4R:MjigUBFUGiY1PqoDYJR5xUy17Sw"',
            }

            if after:
                after_value = f', "after": "{after}"'
            else:
                after_value = ''

            params = {
                ('query_hash', 'c76146de99bb02f6415203be841dd25a'),
                ('variables', f'{{"id":"{id}","include_reel":true,"fetch_mutual":false,"first":1000{after_value}}}'),
            }

            response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)

            response = response.text

            response = json.loads(response.encode("utf-16"))

            after = response['data']['user']['edge_followed_by']['page_info']['end_cursor']
            # print(str(after))

            data_count = response['data']['user']['edge_followed_by']['count']

            time.sleep(10)

            # if data_count > 190000:
            #     logging.debug('data_count больше 190000, time.sleep(15)')
            #     time.sleep(15)
            # else:
            #     logging.debug('data_count меньше 190000, time.sleep(3)')
            #     time.sleep(3)

            objects = response['data']['user']['edge_followed_by']['edges']

            if len(followers1) == 0:
                data_count_changed = 0
                data_count_changed = data_count

            if len(objects) == 0:
                print(colored('На этом аккаунте нет подписчиков либо Вы ввели что-то неправильно', 'red'))
                logging.debug('На этом аккаунте нет подписчиков либо Вы ввели что-то неправильно')
                main_running = False

            for object in objects:
                index += 1
                print(len(followers1), data_count, data_count_changed)
                if len(followers1) != data_count_changed:
                    value = index * 100 // data_count_changed
                    ui.progressBar.setProperty("value", value)
                    followers1.append(object['node']['username'])
                    logging.debug(len(followers1))
                    if index == data_count_changed:
                        running = False
                        index = 0
                        print(colored('Followers from first account had parsed!', 'cyan'))
                        print(colored('----------------------------------------', 'cyan'))
                        logging.debug('Фоловеры были спрашены с первого аккаунта')
                        break
                else:
                    value = index * 100 // data_count
                    ui.progressBar_2.setProperty("value", value)
                    followers2.append(object['node']['username'])
                    logging.debug(len(followers2))
                    if index == data_count:
                        main_running = False
                        running = False
                        print(colored('Followers from second account had parsed!', 'cyan'))
                        print(colored('----------------------------------------', 'cyan'))
                        logging.debug('Фоловеры были спрашены со второго аккаунта')
                        break

    print(followers1)
    print(followers2)

    results = list(set(followers1) & set(followers2))

    with open('results.txt', 'w', encoding='utf-16') as f:
        f.write("Количество одинаковых подписчиков: " + str(len(results)) + "\n")
        for result in results:
            f.write("%s\n" % result)
        f.close()

    print(colored(
        'Откройте документ result.txt, чтобы посмотреть сколько и какие подписчики общие',
        color='cyan'
    ))
    logging.debug('Все результаты помещены в results.txt')
    logging.debug('Программа завершена')


ui.progressBar.setProperty("value", 0)
ui.progressBar_2.setProperty("value", 0)
ui.pushButton.clicked.connect(compare_followers)

# Логика приложения

# Запус основного цикла

sys.exit(app.exec_())

# Запус основного цикла
