from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import logging
import webbrowser
from emoji import emojize

PROXY = {'proxy_url': 'socks5://185.39.150.15:40498',
    'urllib3_proxy_kwargs': {'username': 'dBjT5Vk9qM', 'password': 'rucd0wfF8S'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = "Привет {} {}! Для начала тебе нужно получить на Facebook access_token, чтобы ты мог размещать рекламу. Для этого перейди по ссылке https://example.ru".format(update.message.chat.first_name, emojize(":wave:", use_aliases=True))
    print(text)
    my_keyboard = ReplyKeyboardMarkup([['Справка', 'Ввести access_token']])
    update.message.reply_text(text, reply_markup=my_keyboard)

def help(bot, update):
    webbrowser.open('https://example.com')

def starting(bot, update):
    text = "Что делаем?"
    print(text)
    keyboard_starting = ReplyKeyboardMarkup([['Создать рекламную кампанию', 'Управление', 'Статистика', 'Пиксель', 'Справка']])
    update.message.reply_text(text, reply_markup=keyboard_starting)

############################# Создание рекламной кампании #########################################

def company1(bot, update):
    query = update.callback_query
    bot.edit_message_text(text=company1_text(),
                          reply_markup=menu_company1())

def company2(bot, update):
    query = update.callback_query
    bot.edit_message_text(text=company2_text(),
                          reply_markup=menu_company2())

def company3(bot, update):
    query = update.callback_query
    bot.edit_message_text(text=company3_text(),
                          reply_markup=menu_company3())

############################# Меню рекламной кампании #########################################

def menu_company1():
    keyboard = [[InlineKeyboardButton('Задать имя кампании', callback_data='CompanyName')],
                 [InlineKeyboardButton('Задать цель кампании', callback_data='CompanyTarget')],
                 [InlineKeyboardButton('Оптимизировать бюджет кампании', callback_data='CompanyBudget')],
                 [InlineKeyboardButton('Перейти к настройкам группы объявлений', callback_data='Adset')],
                 [InlineKeyboardButton('Назад', callback_data='starting')]]
    return InlineKeyboardMarkup(keyboard)
    

def menu_company2():
    keyboard = [[InlineKeyboardButton('Задать имя группы объявлений', callback_data='AdsetName')],
                 [InlineKeyboardButton('Динамические креативы', callback_data='AdsetDynamic')],
                 [InlineKeyboardButton('Пол', callback_data='AdsetGender')],
                 [InlineKeyboardButton('Возраст', callback_data='AdsetAge')],
                 [InlineKeyboardButton('Интересы', callback_data='AdsetInterest')],
                 [InlineKeyboardButton('Места размещения', callback_data='AdsetPlacement')],
                 [InlineKeyboardButton('Бюджет', callback_data='AdsetBudget')],
                 [InlineKeyboardButton('Срок', callback_data='AdsetTime')],
                 [InlineKeyboardButton('Перейти к настройкам объявлений', callback_data='Ad')],
                 [InlineKeyboardButton('Назад', callback_data='starting')]]
    return InlineKeyboardMarkup(keyboard)

def menu_company3():
    keyboard = [[InlineKeyboardButton('Задать имя объявления', callback_data='AdName')],
                 [InlineKeyboardButton('Страница ФБ', callback_data='AdFb')],
                 [InlineKeyboardButton('Страница Instagram', callback_data='AdIg')],
                 [InlineKeyboardButton('Формат', callback_data='AdFormat')],
                 [InlineKeyboardButton('Креатив', callback_data='AdCreative')],
                 [InlineKeyboardButton('Текст', callback_data='AdText')],
                 [InlineKeyboardButton('Заголовок', callback_data='AdHeading')],
                 [InlineKeyboardButton('URL', callback_data='AdURL')],
                 [InlineKeyboardButton('Запустить', callback_data='Go')],
                 [InlineKeyboardButton('Назад', callback_data='starting')]]
    return InlineKeyboardMarkup(keyboard)

############################# Сообщения в Кампании #########################################

def company1_text():
  return 'Настройка кампании:'

def company2_text():
  return 'Настройка группы объявлений:'

def company3_text():
  return 'Настройка объявления:'


def Control(bot, update):
    pass

def Statistic(bot, update):
    pass

def Pixel(bot, update):
    pass

def main():
    mybot = Updater("769544739:AAGpBD1EVf9ZHtzzexX1JyYYDGkvfgWMkBs", request_kwargs=PROXY)
    
    logging.info('Бот запускается')

############################# Хэндлеры #########################################

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(RegexHandler('^(Справка)$', help))
    dp.add_handler(RegexHandler('^(Ввести access_token)$', starting))
    dp.add_handler(RegexHandler('^(Управление)$', Control))
    dp.add_handler(RegexHandler('^(Статистика)$', Statistic))
    dp.add_handler(RegexHandler('^(Пиксель)$', Pixel))
    dp.add_handler(RegexHandler('^(Создать рекламную кампанию)$', company1))
    dp.add_handler(CallbackQueryHandler(company2, pattern='Adset'))
    mybot.start_polling()
    mybot.idle() 

main()
