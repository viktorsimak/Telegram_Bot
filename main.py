import telebot
from telebot import types

bot = telebot.TeleBot('5456957774:AAEIMDF_lNd1eBy4fECRDUIK6kQsCRR800Y')

@bot.message_handler(commands=['start'])
def start (message):
    mess1 = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. \n' \
            f'Я телеграмм бот, который поможет тебе узнать кредитные ставки по ипотеке в Сбербанке.\n' \
            f'Для того чтобы узнать ставку и первоначальный взнос нового жилья напишите: <b>"Новостройки"</b>.\n' \
            f'Для того чтобы узнать ставку и первоначальный взнос вторичного жилья напишите: <b>"Вторичка"</b>.\n' \
            f'Для того чтобы узнать ставку и первоначальный взнос семейной ипотеки напишите: <b>"Семейная"</b>.\n' \
            f'Для того чтобы узнать ставку и первоначальный взнос ипотеки с господдержкой напишите: <b>"Господдержка"</b>.\n' \
            f'Если у вас возникли трудности или вы хотите узнать информацию более подробно вы можете перейти на сайт.\n' \
            f'Для этого напишите боту: <b>"Веб сайт"</b>'
    bot.send_message(message.chat.id, mess1, parse_mode='html')


@bot.message_handler(content_types=['text'])
def message (message):
    mess1 = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. \n' \
            f'Я телеграмм бот, который поможет тебе узнать кредитные ставки по ипотеке в Сбербанке.\n' \
            f'Для того чтобы узнать ставку и первоначальный взнос нового жилья напишите: <b>"Новостройки"</b>.\n' \
            f'Для того чтобы узнать ставку и первоначальный взнос вторичного жилья напишите: <b>"Вторичка"</b>.\n' \
            f'Для того чтобы узнать ставку и первоначальный взнос семейной ипотеки напишите: <b>"Семейная"</b>.\n' \
            f'Для того чтобы узнать ставку и первоначальный взнос ипотеки с господдержкой напишите: <b>"Господдержка"</b>.\n' \
            f'Если у вас возникли трудности или вы хотите узнать информацию более подробно вы можете перейти на сайт.\n' \
            f'Для этого напишите боту: <b>"Веб сайт"</b>'
    mess2 = f'Ипотека на новостройку от 9,9%.\n Первый взнос от 0%.\n Срок кредита до 30 лет.\n Макс. сумма кредита 100 млн ₽.'

    mess3 = f'Ипотека на вторичное жильё от 9,9%.\n Первый взнос от 0%.\n Срок кредита до 30 лет.\n Макс. сумма кредита 100 млн ₽.'

    mess4 = f'Семейная ипотека от 5,3%.\n' \
            f'Программа для семей, где хотя бы один ребёнок родился после 2018 года включительно или есть ребёнок с инвалидностью.\n' \
            f'Первоначальный взнос от 15%.\n Срок кредита до 30 лет.\n Сумма кредита до 12 млн ₽.'

    mess5 = f'Господдержка от 6,3%.\n Первый взнос от 15%.\n Срок кредита до 30 лет.\n Макс. сумма кредита 12 млн ₽.'

    if message.text == 'Привет':
        bot.send_message(message.chat.id, mess1, parse_mode='html')
    elif message.text == "Новостройки":
        bot.send_message(message.chat.id, mess2, parse_mode='html')
    elif message.text == "Вторичка":
        bot.send_message(message.chat.id, mess3, parse_mode='html')
    elif message.text == "Семейная":
        bot.send_message(message.chat.id, mess4, parse_mode='html')
    elif message.text == "Господдержка":
        bot.send_message(message.chat.id, mess5, parse_mode='html')
    elif message.text == "Веб сайт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить Веб Сайт", url='https://www.sberbank.ru/ru/person/credits/homenew'))
        bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю...')

bot.polling(none_stop=True)
