from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import pyautogui



# Укажи путь к скачанному драйверу Chrome (например, C:/path/to/chromedriver.exe)
# driver_path = 'D:/distrib/Python/works/chromedriver.exe'

# Настройка драйвера 
options = webdriver.ChromeOptions()
options.add_extension('D:/distrib/Python/works/pythonProject/My/clicker/AvtoNMO.f0e2edb5360d85c3c7c3c4156edb6917731950e893c4d262e421dce8a8f8f869')
options.add_argument('--start-maximized')  # Открытие окна браузера на полный экран
driver = webdriver.Chrome(options=options)


# Открываем сайт
url = "https://nmfo-vo.edu.rosminzdrav.ru/#/user-account/search?preselectedProgram=0f781540-f945-f956-2b3a-fa175987a869"
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)


login = driver.find_element(By.ID, 'username')
login.clear()
login.send_keys('152-720-548 45')

password = driver.find_element(By.ID, 'password')
password.clear()
password.send_keys('EBY7OkowUt4HuJtl')

time.sleep(1)


try:
    driver.find_element(By.CLASS_NAME, 'login__actions-section').find_element(By.TAG_NAME, 'button').click()
except:
    print('Не получилось ввойти\n\n\n\n')

time.sleep(4)

try:
    driver.find_element(By.CLASS_NAME, 'tab-group__header').find_element(By.XPATH, '//svg-icon[@title="Интерактивные образовательные модули"]').click()
except:
    print('Не получилось найти модули\n\n\n\n')

time.sleep(5)



items = ['Подготовка шейки матки к родам и родовозбуждение (по утвержденным клиническим рекомендациям) - 2024']



for i in items:

    try:
        search_item = driver.find_element(By.XPATH, '//div[@class="search-filters__section search-filters__section_with-input ng-star-inserted"]').find_element(By.TAG_NAME, 'app-text-field').find_element(By.TAG_NAME, 'input')
        search_item.clear()
        search_item.send_keys(i)
    except:
        print('Не получилось ввести тест\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//td[@class="grid__column_hide-in-card text grid__column_name text_small grid__column_less grid__column ng-star-inserted"]').click()
    except:
        print('Не получилось найти тест\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//button[@class="button button_block button_primary button_more-radius edu-element__plan-button ng-star-inserted"]').click()
    except:
        print('Не получилось взять в работу\n\n\n\n')

    time.sleep(3)

    try:
        driver.find_element(By.XPATH, '//button[@class="button button_primary iom-main-info__start-btn"]').click()
    except:
        try:
            driver.find_element(By.XPATH, '//button[@class="button button_primary iom-main-info__start-btn button_stroked"]').click()
        except:
            print('Не получилось перейти к обучению\n\n\n\n')

    time.sleep(3)

    try:
        driver.find_element(By.XPATH, '//span[@class="ng-star-inserted"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[@class="button button_primary"]').click()
    except:
        print('Не получилось подтвердить снилс\n\n\n\n')

    time.sleep(4)

    try:
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.find_elements(By.XPATH, '//div[@class="v-button v-widget icon v-button-icon"]')[-1].click()
    except:
        print('Не получился быстрый переход\n\n\n\n')

    time.sleep(3)

    try:
        
        fake_test = driver.find_elements(By.XPATH, '//div[@class="v-button v-widget link v-button-link"]')
        if fake_test[5].text == '1.3.1 Предварительное тестирование':
            fake_test[5].click()
        elif fake_test[6].text == '1.3.1 Предварительное тестирование':
            fake_test[6].click()
        elif fake_test[7].text == '1.3.1 Предварительное тестирование':
            fake_test[7].click()


    except:
        print('Не получилось перейти по предварительному/итоговому тестированию\n\n\n\n')

    time.sleep(4)

    try:
            driver.find_element(By.XPATH, '//div[@tabindex="0"][@class="v-button v-widget"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//div[@class="c-table-composition v-layout v-widget v-has-width"]').find_element(By.XPATH, '//span[@class="c-table-clickable-cell"]').click()
    except:
        print('Не получилось взять/перейти по тесту\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//button[@class="quiz-buttons-primary mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]').click()
    except:
        print('Не получилось начать проб тестирование\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//button[@class="quiz-buttons-primary mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]').click()
    except:
        print('Не получилось закончить проб тестирование\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//button[@class="mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]').click()
    except:
        print('Не получилось подтвердить окончание проб тестирования\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//button[@class="quiz-buttons-primary mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]').click()
    except:
        print('Не получилось закончить проб тестирование\n\n\n\n')

    time.sleep(4)

    try:
        actions = ActionChains(driver)
        actions.move_by_offset(100, 100).perform()
        time.sleep(3)
        actions.click().perform()
        time.sleep(1)
        
        try:
            for i in range(3):
                driver.find_element(By.XPATH, '//div[@class="v-button v-widget blue-button v-button-blue-button icon-align-right v-button-icon-align-right icon v-button-icon"]').click()
                time.sleep(1)
            driver.find_element(By.XPATH, '//div[@tabindex="0"][@class="v-button v-widget"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//div[@class="c-table-composition v-layout v-widget v-has-width"]').find_element(By.XPATH, '//span[@class="c-table-clickable-cell"]').click()
        except:
            try:
                driver.find_element(By.XPATH, '//div[@class="v-button v-widget blue-button v-button-blue-button icon-align-right v-button-icon-align-right icon v-button-icon"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//div[@tabindex="0"][@class="v-button v-widget"]').click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//div[@class="c-table-composition v-layout v-widget v-has-width"]').find_element(By.XPATH, '//span[@class="c-table-clickable-cell"]').click()
            except:
                print('Не получилось открыть вкладу рил тестирования2\n\n\n\n')
    except:
        print('Не получилось открыть вкладу рил тестирования\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//button[@class="quiz-buttons-primary mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]').click()
    except:
        print('Не получилось начать рил тестирование\n\n\n\n')
    time.sleep(10)

    try:
        time.sleep(5)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.refresh()
        time.sleep(30)
        keyboard.press_and_release('enter')
        time.sleep(5)
        pyautogui.moveTo(1565, 60, duration=1)  # Переместиться за 1 секунду
        pyautogui.click()
        pyautogui.moveTo(1400, 210, duration=1)  # Переместиться за 1 секунду
        pyautogui.click()
        time.sleep(5)
        keyboard.press_and_release('enter')
    except:
        print('Не получилось включить расширение\n\n\n\n')

    time.sleep(330)

    try:
        driver.find_element(By.XPATH, '//button[@class="quiz-buttons-primary mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]').click()
    except:
        print('Не получилось закончить рил тестирование\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//button[@class="mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]').click()
    except:
        print('Не получилось подтвердить окончание рил тестирования\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//button[@class="quiz-buttons-primary mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]').click()
    except:
        print('Не получилось закончить рил тестирование\n\n\n\n')

    time.sleep(4)

    try:
        driver.find_element(By.XPATH, '//div[@class="v-horizontallayout v-layout v-horizontal v-widget"]').find_element(By.XPATH, '//div[@class="v-button v-widget icon v-button-icon"]').click()
    except:
        print('Не получилось закрыть окно с подтверждением\n\n\n\n')

    time.sleep(2)
    driver.close()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    time.sleep(2)

    try:
        driver.find_element(By.CLASS_NAME, "edu-element__go-back").click()
    except:
        print('Не получилось вернуться назад\n\n\n\n')


time.sleep(1000)