import urllib3
import g4f
import time
import random
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types


tokenTg = 'YOUR_TG_TOKEN'
urlTech2 = 'https://www.technologyreview.com/topic/artificial-intelligence/feed/'
url = 'https://www.zdnet.com/news/rss.xml'
urlDee = 'https://www.deepmind.com/blog/rss.xml'
urlTech = 'https://techcrunch.com/feed/'

bot = Bot(tokenTg)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    titleTech2 = "gfdgf"
    title = "How to delete Facebook, Messenger, or Instagram - if you want Meta out of your life"
    titleDee = 'hfhg'
    titleTech = 'fdsf'

    chat_id = 'YOUR_CHAT_ID_TG'
    
    while True:
        time.sleep(39600)
        if getItems(urlTech2)[0] != titleTech2:
            await bot.send_message(chat_id=-chat_id, text=(chat(getItems(urlTech2))))
            titleTech2 = getItems(urlTech2)[0]
        else:
            print('Равны')
        time.sleep(random.randint(3600,7200))


        if getItems(url)[0] != title:
            await bot.send_message(chat_id=-chat_id, text=(chat(getItems(url))))
            title = getItems(url)[0]
        else:
            print('Равны')
        time.sleep(random.randint(3600,7200))


        if getItems(urlTech)[0] != titleTech:
            await bot.send_message(chat_id=-chat_id, text=(chat(getItems(urlTech))))
            titleTech = getItems(urlTech)[0]
        else:
            print('Равны')
        time.sleep(random.randint(3600,7200))


        if getItems(urlDee)[0] != titleDee:
            await bot.send_message(chat_id=-chat_id, text=(chat(getItems(urlDee))))
            titleDee = getItems(urlDee)[0]
        else:
            print('Равны')
        time.sleep(random.randint(3600,7200))


        if getItems(url)[0] != title:
            await bot.send_message(chat_id=-chat_id, text=(chat(getItems(url))))
            title = getItems(url)[0]
        else:
            print('Равны')
        time.sleep(25200)



def getItems(url):
    http = urllib3.PoolManager()
    geturl = http.request('Get', url)  # get link
    fullText = geturl.data.decode('utf-8')  # decode

    soup = BeautifulSoup(fullText, 'xml')  # parsing
    items = soup.find_all('item')  # search item

    item_res = items[0].title.text, items[0].description.text, items[0].find('link').text

    return item_res

def chat(item_res):
    response = g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages=[{'role':'user', 'content':f'Переведи этот текст на русский язык. Учитывай, что это пост в телеграмм канал. Оформи его так, как пост для канала. Ничего больше писать не нужно. Также добавь в конец ссылку, с пометкой источник. Создай пост не от первого лица и не особо большой, постарайся сократить информацию, но чтобы было интересно. {item_res}'}],)

    return response



executor.start_polling(dp)

