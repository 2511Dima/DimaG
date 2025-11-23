import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tokenTg = 'YOUR_TG_TOKEN'
tokenVk = 'YOUR_VK_TOKEN'

bot = Bot(tokenTg)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Привет, я беру информацию из последнего поста в любом сообществе Вк\n\nНапиши домен(id) сообщества из ВК:\n(Узнать домен - /help)')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Узнать домен', url='https://vk.com/faq18062'))
    await bot.send_message(chat_id=message.from_user.id, text='Перейди по ссылке и узнай домен сообщества!', reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def get_domain(message: types.Message):
    domain = message.text
    count = 1

    response = requests.get('https://api.vk.com/method/wall.get', params={'access_token': tokenVk, 'v': 5.199, 'domain': domain, 'count': count, 'offset' : 0})
    if 'response' in response.json():
        data = response.json()['response']['items'][0]
        print(data)

        domain_up = domain[0].upper()

        if data['text'] == '':
            pass
        else:
            await bot.send_message(chat_id=message.from_user.id, text=('Последний пост с сообщества ' + domain_up + domain[1:len(domain)] + ':'))


        for i in range(len(data['attachments'])):

            if data['attachments'][i]['type'] == 'photo':
                await bot.send_photo(chat_id=message.from_user.id, photo=data['attachments'][i]['photo']['sizes'][-1]['url'], caption=data['text'])
                
            elif data['attachments'][i]['type'] == 'video':
                await bot.send_photo(chat_id=message.from_user.id, photo=data['attachments'][i]['video']['image'][-1]['url'], caption=data['text'])
                
            else:
                continue


    else:
        await bot.send_message(chat_id=message.from_user.id, text='Такого сообщества не существует\n\nУзнать домен(id) сообщества Вк - /help')




executor.start_polling(dp)
