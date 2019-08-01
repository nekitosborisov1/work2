import telebot
from telebot import types

API_TOKEN = '668326815:AAH4Uj_OrxmSv6pHOzEbx0IynVJS7eAaILc'

bot = telebot.TeleBot(API_TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_buy= types.InlineKeyboardButton("Купить биткоины \U0001F4B5")
btn_curs= types.KeyboardButton("Курс валют \U0001F4C8")
btn_rules= types.KeyboardButton("Правила обменника\U00002757")
btn_help= types.KeyboardButton("Поддержка 24/24 (анонимно) \U00002611")
markup_menu.add(btn_buy, btn_curs, btn_rules, btn_help)

markup_inline_url = types.InlineKeyboardMarkup()
btn_in_url = types.InlineKeyboardButton('\U0001F4B1 Конвертер валют', url='https://pokur.su/btc/rub/1/')
markup_inline_url.add(btn_in_url)

markup_inline_url2 = types.InlineKeyboardMarkup()
btn_in_url2 = types.InlineKeyboardButton('\U0001F4C4 Права и обязанности сторон', url='https://note-pad.net/ru/read/fd3d573508e0c70d56cb3490ae25c147?page=1')
markup_inline_url2.add(btn_in_url2)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 print(message)
 bot.send_message(message.chat.id, "Добро пожаловать в *Virtual Exchange*!                                                                                                                                                  "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                         "
                                   "_Обменник создан исключительно для облегчения процесса оплаты заказов магазина Criminal Russia. Работаем по выгодному курсу только для клиентов магазина. Не пытайтесь обмануть и менять валюту для других целей._                                                                           "
                                   "*\U00002757Иные операции обмена запрещены\U00002757*                                                                                                                                      "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                                         "
                                   "Для покупки биткоинов пишите в ЛС необходимую сумму для обмена: @ElectronicSupport", parse_mode="Markdown", reply_markup=markup_menu)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
 print(message)
 if message.text == "Купить биткоины \U0001F4B5":
     bot.send_message(message.chat.id,
                      "Для покупки биткоинов пишите в ЛС необходимую сумму для обмена: @ElectronicSupport",
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(message.chat.id,
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                         "
                      "_Обменник создан исключительно для облегчения процесса оплаты заказов магазина Criminal Russia. Работаем по выгодному курсу только для клиентов магазина. Не пытайтесь обмануть и менять валюту для других целей._                                                                           "
                      "*\U00002757Иные операции обмена запрещены\U00002757*                                                                                                                                      "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                                         "
                      ,
                      parse_mode="Markdown", reply_markup=markup_menu)
 elif message.text == "Курс валют \U0001F4C8":
  bot.send_message(message.chat.id, 'Актуальная стоиомость Bitcoin (BTC) к рублю (RUB) \U00002B07', parse_mode="Markdown", reply_markup=markup_inline_url)
 elif message.text == "Поддержка 24/24 (анонимно) \U00002611":
  bot.send_message(message.chat.id, "Ответим на все вопросы, касательно процесса оплаты и гарантий. Также решаем проблемы, связанные с транзакциями                                                                                "
                                    "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                                    "Свой вопрос можно задать администратору обменника: @ElectronicSupport",
                   reply_markup=markup_menu)
 elif message.text == "Правила обменника\U00002757":
  bot.send_message(message.chat.id,
                   '*Правила обменника обязательны к прочтению перед покупкой!*                                                                                                                                   '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                                            '
                   '_Оплачивая заказ - Вы автоматически соглашаетесь с правилами и условиями, указанными ниже_ \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_url2)
 else:
  bot.reply_to(message, message.text, reply_markup=markup_menu)



bot.polling(none_stop=True, interval=0)