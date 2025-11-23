from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


token = '8159560859:AAF41j2bCaG8NyENWGkg4WxunYVj--O7qR8'

bot = Bot(token)
dp = Dispatcher(bot)
admin_chat_id = '1235798032'


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    button_price = InlineKeyboardMarkup()
    button_price.add(InlineKeyboardButton('Ознакомиться с ценами и городами', callback_data='prices')).add(InlineKeyboardButton('Предложить новость/Поддержка', callback_data='news'))
    await bot.send_message(chat_id=message.from_user.id, text='Привет!\nЕсли хочешь обратиться к администраторам, то напиши мне, я передам.\nВот все мои функции:', reply_markup=button_price)



@dp.callback_query_handler(text='prices')
@dp.callback_query_handler(text='news')
async def user_news(callback: types.CallbackQuery):
    if callback.data == 'prices':
        await callback.message.answer('Цены на рекламу:\nЦена 1\nЦена 2\nЦена 3')
    elif callback.data == 'news':
        await callback.message.answer('Напиши свою новость и её рассмотрят администраторы:')



@dp.message_handler(content_types=['text'])
async def user_message(message: types.message):
    # if message.from_user.username == 'BuyMeKoenigsegg':
        try:
            await bot.send_message(chat_id=message.reply_to_message.forward_from.id, text=('Вам пришёл ответ:\n\n' + message.text))
            await bot.send_message(chat_id=admin_chat_id, text='Ваше сообщение отправлено!')
            
        except:
            # await bot.send_message(chat_id=admin_chat_id, text='Вы не можете писать себе(')
            if message.from_user.username != 'BuyMeKoenigsegg':
                await message.reply("Ваше сообщение отправлено, Вам скоро ответят!")
                await bot.send_message(chat_id=admin_chat_id, text=(f'Тебе пришло новое сообщение!\n\n' + message.text + f'\n\nЧтобы ответить на него сделай "Reply/Ответ"'))
                await message.bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.from_user.id, message_id=message.message_id)




executor.start_polling(dp)