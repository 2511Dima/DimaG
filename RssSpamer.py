import urllib3
import g4f
import time
import random
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types


tokenTg = '7521073097:AAEE9CoGtlyN9Cm-ccoWyTMzJKzxO9w1jzk' #the same like parser
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

    while True:
        time.sleep(39600)
        if getItems(urlTech2)[0] != titleTech2:
            await bot.send_message(chat_id=-1002334201246, text=(chat(getItems(urlTech2))))
            titleTech2 = getItems(urlTech2)[0]
        else:
            print('Равны')
        time.sleep(random.randint(3600,7200))


        if getItems(url)[0] != title:
            await bot.send_message(chat_id=-1002334201246, text=(chat(getItems(url))))
            title = getItems(url)[0]
        else:
            print('Равны')
        time.sleep(random.randint(3600,7200))


        if getItems(urlTech)[0] != titleTech:
            await bot.send_message(chat_id=-1002334201246, text=(chat(getItems(urlTech))))
            titleTech = getItems(urlTech)[0]
        else:
            print('Равны')
        time.sleep(random.randint(3600,7200))


        if getItems(urlDee)[0] != titleDee:
            await bot.send_message(chat_id=-1002334201246, text=(chat(getItems(urlDee))))
            titleDee = getItems(urlDee)[0]
        else:
            print('Равны')
        time.sleep(random.randint(3600,7200))


        if getItems(url)[0] != title:
            await bot.send_message(chat_id=-1002334201246, text=(chat(getItems(url))))
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

    # items_list = []

    # for item in items:
    #     item_dict = {}
    #     item_dict['title'] = item.title.text
    #     item_dict['description'] = item.description.text
    #     item_dict['link'] = item.find('link')
    #     soup2 = BeautifulSoup(item_dict['description'], 'html.parser')
    #     item_dict['images'] = [img['src'] for img in soup2.find_all('img')]
    #     item_dict['pubDate'] = item.find('pubDate').text
    #     items_list.append(item_dict)

    item_res = items[0].title.text, items[0].description.text, items[0].find('link').text

    return item_res

def chat(item_res):
    response = g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages=[{'role':'user', 'content':f'Переведи этот текст на русский язык. Учитывай, что это пост в телеграмм канал. Оформи его так, как пост для канала. Ничего больше писать не нужно. Также добавь в конец ссылку, с пометкой источник. Создай пост не от первого лица и не особо большой, постарайся сократить информацию, но чтобы было интересно. {item_res}'}],)

    return response



executor.start_polling(dp)
