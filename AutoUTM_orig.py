from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import gspread
from datetime import datetime
import traceback
import json


# Настройки.
# s_user = "dimon2511gordienko@gmail.com"
# s_pass = "salebot_dima"
t_url = "https://salebot.pro/projects/586185/table/7"


while True:
    try:
        # Настройки браузера для автоматического скачивания.
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        driver.get(t_url)
        time.sleep(105)
        cookies = driver.get_cookies()
        with open('cookies.json', 'w') as file:
            json.dump(cookies, file)
    #     coo = [{'domain': 'salebot.pro', 'httpOnly': False, 'name': 'paper_scroller_x_', 'path': '/projects/586185', 'sameSite': 'Lax', 'secure': False, 'value': '-2000'}, {'domain': 'salebot.pro', 'expiry': 1762542894, 'httpOnly': True, 'name': '_dialog_session', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'b6c1cb4931b9026c5f4d792c8169c9ef'}, {'domain': '.salebot.pro', 'expiry': 1761405254, 'httpOnly': False, 'name': '_ym_isad', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2'}, {'domain': '.salebot.pro', 'expiry': 1792869254, 'httpOnly': False, 'name': '_ym_uid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1761333255682666334'}, {'domain': '.salebot.pro', 'expiry': 1792869254, 'httpOnly': False, 'name': '_ym_d', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1761333255'}, {'domain': 'salebot.pro', 'httpOnly': False, 'name': 'open_map', 'path': '/projects/586185', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': 'salebot.pro', 'httpOnly': False, 'name': 'paper_scroller_y_', 'path': '/projects/586185', 'sameSite': 'Lax', 'secure': False, 'value': '2700'}, {'domain': 'salebot.pro', 'httpOnly': False, 'name': 'zoom_info_', 'path': '/projects/586185', 'sameSite': 'Lax', 'secure': False, 'value': '0'}]
    #     # Открытие файла с cookies
    #     for cookie in coo:
    #         driver.add_cookie(cookie)
    #     driver.refresh()

    #     # Закрытие рекламы
    #     time.sleep(2)
    #     try:
    #         driver.find_element(By.CLASS_NAME, 'w-100').find_element(By.XPATH, '//div[@class="svg-light-blue pr-24 cursor-pointer svg-28 close_vip_banner--js"]').click()
    #     except:
    #         print('Не получилось закрыть рекламу или окно скрыто\n\n')

    #     time.sleep(1)

    #     html = driver.page_source
    #     parse_info = []

    #     # Парсим через BeautifulSoup
    #     soup = bs(html, 'html.parser')
    #     table = soup.find_all('input', attrs={'class': "cell-content cell-string text-input overflow-text-ellipsis_2"})

    #     # Сортируем в списки
    #     temporary = []
    #     for i in table:
    #         val = i.get("data-display-value")
    #         if val == '{}':
    #             if len(temporary) > 0:
    #                 parse_info.append(temporary)
    #             temporary=[]
    #         else:
    #             temporary.append(val)
    #     if len(temporary) > 0:
    #                 parse_info.append(temporary)

    #     service_account_info = {
    #     "type": "service_account",
    #     "project_id": "ivory-bit-475919-k3",
    #     "private_key_id": "1a70a6eb8c2c8980958ea6074e2727a004592fd0",
    #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCrVFUqH4MIJ/qR\nK3hkTfy8RPXUGsKIsIqLLCk9IhGfMjuyrvGywCcsdHGx0ACJZzJD6HuqKcci4zNP\n8TD8IuEn0/pmlqKQaVLE9JpVk2MgMxh9aTeZPn/ntCxGrEF2RWv2/282GSYT/FWx\nQyPI7yZ9GO0iyImyQRyX7QdPNLVAUB2zrOJ7yP0KsQxow38/MrwoyJOvdvRt72G4\ntj0sNMQp4uyeElJ5KArrBYUpYGUigV5Xi1mc2WUWLTwqgBdF6xD/M3GyHXR6lsG9\nfJRki5heKokeRbdf6CjxHZT2oj9wHA+jX2q7izWSMZawTM7iHZE+/MdS+BlZBL7A\nSuv9Az8XAgMBAAECggEAO41ovOePKDqdQfCWPGdPPjHKMRvMGq8iuRV0kCdTcL6J\nOabNpJBeDXm8O05NoXUZZ7lbot46tcm7gEIaAMou8SUhmJ8rin7RolxTeQNuJTcd\ngBoelUnAM83QxhACARZIXOaUxX0gWzoOnzrzKVjXTAxqAPkrw6YWRkjBjaqIhf3A\nSA/Ca6IRUMoFjkjel5KBpokTE/brMMN/RI/23fZj/fwMOBPoD/KblZtWVzI0KClz\n+3jPgn7FtyAozehUhLLED3IRIj4CSvrpxIlJwDI+wkJVJcL8wdY1KFTX7ZwlUHKH\nbkiOcLCZ6hQE1hMQDuE70M3yZgefwl0+mPsQy920IQKBgQDuNc6T2QK+SZ7Yld7X\nz9LEOSRhpNZ4gqYfyDJJPvUdZTqTHk/8GQ6gYLGk0n7+8B6qSOeSfrOMb7G0EPaB\ndfRFSta4LHkVCoynQQYqK3msGEm+w3UmjpYjU0eGB78Jaaspfp+nPgmXJk/Z6Ald\nvQKljaOR5tulT3XZl7tom2xQPQKBgQC4H9+3vWFc4npIxJI/aW3MxU+rCjMrxhS1\na3eNdcw9CZzzuhrkBRZGWg/GazFJIaU68mazKsDtZY0bybDBfm3/x1pV81V5/jVL\nLNGYpDCi/voa3LlAnVKpnedRHpSaQsSZt205YnTHQJ3T3SrI0us913Kdh95a14+D\nf5GEHMkN4wKBgQCCi6JmjCtgtWAEOj4h75cGSnqRuJCBArif+kr0sTgLoAp1zcrv\n0ZuecN9qAKHwfQ+RKtseAanMcPnmQNWXJVl1EAqUbGr/CQUENDJ4sdLAaZ8gmGV/\nd+z39w/feCdNtUdEOkysjucamrhwJyXa5Vap+/GEaAw/kEh5sxnVvjeh0QKBgD38\n/SSu7YiH9wNoqpQOupimFRxQYsnp9i7d73IAprIl+mFT1pnN3KHy0DzM+drVKPuf\ngFPxoOJLviYM0SVTm1TxmMg3FB/uJaMZg7cQEA/QKAPDK9tFG/9e2fHFieIleGsI\nBg27x/UNHBWn8C+MUwaO8ld21rVevUJYQHVp+4ZhAoGAFqvnKMVoTBBS81YB8nl4\nTivno9QHcXbUDxKnc8su+YoKQsEbXEn7dWQIVDIBnQK0Rq4T6BH0AKfrRoDKoA7/\n/uTErS+FGWsEKZo3f0DzXKFxCw/fM6RAYgxHC7Mor6P8aWk/fd5acq6ml0JQIGdI\na0f5lQbL46+2NrOu4Zyc5ws=\n-----END PRIVATE KEY-----\n",
    #     "client_email": "google-sheets-api@ivory-bit-475919-k3.iam.gserviceaccount.com",
    #     "client_id": "104985431719647946549",
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/google-sheets-api%40ivory-bit-475919-k3.iam.gserviceaccount.com",
    #     "universe_domain": "googleapis.com"
    #     }

    #     # Открытие гугл таблицы и выгрузка данных в неё
    #     # gc = gspread.service_account_from_dict(service_account_info)
    #     # wks = gc.open("Посевы (UTM-Аналитика) | Финанс Плюс").sheet1
    #     for i in parse_info:
    #         if i[0] != 'Тест':
    #             print(i)
    #             # line = wks.find(i[0]).row
    #             # wks.update_acell('K'+str(line), int(i[5]))
    #             # wks.update_acell('L'+str(line), int(i[6]))
    #             # wks.update_acell('M'+str(line), int(i[7]))
    #             # wks.update_acell('N'+str(line), int(i[8]))
    #     driver.close()

    except Exception as e:
        now = datetime.now()
        print('Неизвестная ошибка:', now.strftime('%Y-%m-%d %H:%M'))
        print('Подробности ошибки:', str(e))
        traceback.print_exc()

    # time.sleep(900)