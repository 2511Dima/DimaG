from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import gspread
from datetime import datetime
import traceback
import json


t_url = "https://salebot.pro/projects/YOUR_PROJECT_ID/table/YOUR_SALEBOT_TABLE_ID"


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
        
        coo = ['YOUR_CHROME_SALEBOT_COOKIES']
        # Открытие файла с cookies
        for cookie in coo:
            driver.add_cookie(cookie)
        driver.refresh()

        # Закрытие рекламы
        time.sleep(2)
        try:
            driver.find_element(By.CLASS_NAME, 'w-100').find_element(By.XPATH, '//div[@class="svg-light-blue pr-24 cursor-pointer svg-28 close_vip_banner--js"]').click()
        except:
            print('Не получилось закрыть рекламу или окно скрыто\n\n')

        time.sleep(1)

        html = driver.page_source
        parse_info = []

        # Парсим через BeautifulSoup
        soup = bs(html, 'html.parser')
        table = soup.find_all('input', attrs={'class': "cell-content cell-string text-input overflow-text-ellipsis_2"})

        # Сортируем в списки
        temporary = []
        for i in table:
            val = i.get("data-display-value")
            if val == '{}':
                if len(temporary) > 0:
                    parse_info.append(temporary)
                temporary=[]
            else:
                temporary.append(val)
        if len(temporary) > 0:
                    parse_info.append(temporary)

        service_account_info = {
        'YOUR_SERVICE_ACCOUNT_INFO_GOOGLE_SHEETS'
        }

        # Открытие гугл таблицы и выгрузка данных в неё
        gc = gspread.service_account_from_dict(service_account_info)
        wks = gc.open("TABLE_NAME").sheet1
        for i in parse_info:
            if i[0] != 'Тест':
                print(i)
                line = wks.find(i[0]).row
                wks.update_acell('A'+str(line), int(i[5]))
                wks.update_acell('B'+str(line), int(i[6]))
                wks.update_acell('C'+str(line), int(i[7]))
                wks.update_acell('D'+str(line), int(i[8]))
        driver.close()

    except Exception as e:
        now = datetime.now()
        print('Неизвестная ошибка:', now.strftime('%Y-%m-%d %H:%M'))
        print('Подробности ошибки:', str(e))
        traceback.print_exc()

    # time.sleep(900)
