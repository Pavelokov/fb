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
                

############################# Меню Создание Рекл Кампании #########################################

def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Создать рекламную кампанию', callback_data='Company1')],
                 [InlineKeyboardButton('Управление', callback_data='Control')],
                 [InlineKeyboardButton('Статистика', callback_data='Statistic')],
                 [InlineKeyboardButton('Пиксель', callback_data='Pixel')],
                 [InlineKeyboardButton('Справка', callback_data='help')]]
    return InlineKeyboardMarkup(keyboard)

def menu_company1():
    keyboard = [[InlineKeyboardButton('Задать имя кампании', callback_data='CompanyName')],
                 [InlineKeyboardButton('Задать цель кампании', callback_data='CompanyTarget')],
                 [InlineKeyboardButton('Оптимизировать бюджет кампании', callback_data='CompanyBudget')],
                 [InlineKeyboardButton('Перейти к настройкам группы объявлений', callback_data='Company2')],
                 [InlineKeyboardButton('В меню', callback_data='main_menu')]]
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
                 [InlineKeyboardButton('Перейти к настройкам объявлений', callback_data='Company3')],
                 [InlineKeyboardButton('Назад', callback_data='Company1')],
                 [InlineKeyboardButton('В меню', callback_data='main_menu')]]
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
                 [InlineKeyboardButton('Назад', callback_data='Company2')],
                 [InlineKeyboardButton('В меню', callback_data='main_menu')]]
    return InlineKeyboardMarkup(keyboard)

############################# Меню Кампания ########################################

def menu_CompanyTarget():
    keyboard = [[InlineKeyboardButton('Охват', callback_data='TargetReach')],
                 [InlineKeyboardButton('Трафик', callback_data='TargetTraffic')],
                 [InlineKeyboardButton('Вовлеченность', callback_data='TargetInvolvement')],
                 [InlineKeyboardButton('Просмотры видео', callback_data='TargetVideo')],
                 [InlineKeyboardButton('Генерация лидов', callback_data='TargetLead')],
                 [InlineKeyboardButton('Сообщения', callback_data='TargetMessages')],
                 [InlineKeyboardButton('Конверсии', callback_data='TargetConversions')],
                 [InlineKeyboardButton('Назад', callback_data='Company1')]]
    return InlineKeyboardMarkup(keyboard)

def menu_CompanyBudget():
    keyboard = [[InlineKeyboardButton('Да', callback_data='CompanyBudgetYes')],
                 [InlineKeyboardButton('Нет', callback_data='CompanyBudgetNo')],
                 [InlineKeyboardButton('Назад', callback_data='Company1')]]
    return InlineKeyboardMarkup(keyboard)

def menu_CompanyName():
    keyboard = [[InlineKeyboardButton('Назад', callback_data='Company1')]]
    return InlineKeyboardMarkup(keyboard)

############################# Меню Группа объявлений ########################################

def menu_AdsetSimple():
    keyboard = [[InlineKeyboardButton('Назад', callback_data='Company2')]]
    return InlineKeyboardMarkup(keyboard)

def menu_AdsetDynamic():
    keyboard = [[InlineKeyboardButton('Да', callback_data='AdsetYes')],
                 [InlineKeyboardButton('Нет', callback_data='AdsetNo')],
                 [InlineKeyboardButton('Назад', callback_data='Company2')]]
    return InlineKeyboardMarkup(keyboard)

def menu_AdsetGender():
    keyboard = [[InlineKeyboardButton('Только мужчины', callback_data='AdsetGenderMale')],
                 [InlineKeyboardButton('Только мужчины', callback_data='AdsetGenderFemale')],
                 [InlineKeyboardButton('Мужчины и Женщины', callback_data='AdsetGenderMaleFemale')],
                 [InlineKeyboardButton('Назад', callback_data='Company2')]]
    return InlineKeyboardMarkup(keyboard)

def menu_AdsetPlacement():
    keyboard = [[InlineKeyboardButton('Автоматические плэйсменты', callback_data='AdsetPlacementAuto')],
                 [InlineKeyboardButton('Выбрать плейсменты вручную', callback_data='AdsetPС')],
                 [InlineKeyboardButton('Назад', callback_data='Company2')]]
    return InlineKeyboardMarkup(keyboard)

def menu_AdsetPС():
    keyboard = [[InlineKeyboardButton('Лента Facebook', callback_data='AdsetPС_FFb')],
                 [InlineKeyboardButton('Лента Instagram', callback_data='AdsetPC_FIg')],
                 [InlineKeyboardButton('Stories Facebook', callback_data='AdsetPC_SFb')],
                 [InlineKeyboardButton('Stories Instagram', callback_data='AdsetPC_Sig')],
                 [InlineKeyboardButton('Назад', callback_data='Company2')]]
    return InlineKeyboardMarkup(keyboard)             


############################# Меню объявления ########################################

def menu_AdSimple():
    keyboard = [[InlineKeyboardButton('Назад', callback_data='Company3')]]
    return InlineKeyboardMarkup(keyboard)

def menu_Go():
    keyboard = [[InlineKeyboardButton('В меню', callback_data='main_menu')]]
    return InlineKeyboardMarkup(keyboard)

############################# Управление ########################################

def menu_Control():
    keyboard = [[InlineKeyboardButton('Отобразить список кампаний', callback_data='ControlShowCompany')],
                 [InlineKeyboardButton('Отобразить список групп объявлений', callback_data='ControlShowAdset')],
                 [InlineKeyboardButton('Отобразить список объявлений', callback_data='ControlShowAd')],
                 [InlineKeyboardButton('Дублировать', callback_data='ControlDuplicate')],
                 [InlineKeyboardButton('ВКЛ/ВЫКЛ', callback_data='ControlOn')],
                 [InlineKeyboardButton('Назад', callback_data='Control')]]

    return InlineKeyboardMarkup(keyboard)  

def menu_ControlSimple():
    keyboard = [[InlineKeyboardButton('Назад', callback_data='Control')]]
    return InlineKeyboardMarkup(keyboard)

############################# Статистика ########################################

def menu_Statistic():
    keyboard = [[InlineKeyboardButton('За вчера', callback_data='StatisticYesterday')],
                 [InlineKeyboardButton('За сегодня', callback_data='StatisticToday')],
                 [InlineKeyboardButton('За неделю', callback_data='StatisticWeek')],
                 [InlineKeyboardButton('За месяц', callback_data='StatisticMonth')],
                 [InlineKeyboardButton('За период', callback_data='StatisticPeriod')],
                 [InlineKeyboardButton('В меню', callback_data='main_menu')]]

    return InlineKeyboardMarkup(keyboard) 

############################# Сообщения в Кампании #########################################

def start_message():
  return '"Привет {} {}! Для начала тебе нужно получить на Facebook access_token, чтобы ты мог размещать рекламу. Для этого перейди по ссылке https://example.ru".format(update.message.chat.first_name, emojize(":wave:", use_aliases=True))'

def main_menu_message():
  return 'Что делаем'

def company1_text():
  return 'Настройка кампании:'

def company2_text():
  return 'Настройка группы объявлений:'

def company3_text():
  return 'Настройка объявления:'

############################# Функции #########################################

############################# Старт / Главное меню #########################################

def greet_user(bot, update):
    update.message.reply_text(start_message(),
                            reply_markup=menu_greet_user())

def menu_greet_user():
    keyboard = [[InlineKeyboardButton('Ввести access_token', callback_data='main_menu')],
                 [InlineKeyboardButton('Справка', callback_data='help')]]
    return InlineKeyboardMarkup(keyboard)

def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def help(bot, update):
    webbrowser.open('https://example.com')

############################# Создание рекламной кампании #########################################

def Company1(bot, update):
    query = update.callback_query
    bot.edit_message_text(text=company1_text(),
                          reply_markup=menu_company1(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def Company2(bot, update):
    query = update.callback_query
    bot.edit_message_text(text=company2_text(),
                          reply_markup=menu_company2(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def Company3(bot, update):
    query = update.callback_query
    bot.edit_message_text(text=company3_text(),
                          reply_markup=menu_company3(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )



############################# Создание / Кампании #########################################

def CompanyName(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Задайте имя рекламной кампании',
                          reply_markup=menu_CompanyName(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def CompanyTarget(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Задайте цель рекламной кампании',
                          reply_markup=menu_CompanyTarget(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def CompanyBudget(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Оптимизировать бюджет рекламной кампании?',
                          reply_markup=menu_CompanyBudget(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

############################# Создание / Группа объявлений #########################################

def AdsetName(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Задайте имя группы объявлений',
                          reply_markup=menu_AdsetSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdsetDynamic(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Включить динамические креативы?',
                          reply_markup=menu_AdsetDynamic(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdsetGender(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Укажите пол (по умолчанию Мужчины и Женщины)',
                          reply_markup=menu_AdsetGender(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdsetAge(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Укажите возраст (по умолчанию 18+ - 65)',
                          reply_markup=menu_AdsetSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdsetInterest(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Интересы',
                          reply_markup=menu_AdsetSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdsetPlacement(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Плэйсменты',
                          reply_markup=menu_AdsetPlacement(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdsetPС(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Какие плейсменты включить?',
                          reply_markup=menu_AdsetPС(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdsetBudget(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Задайте бюджет',
                          reply_markup=menu_AdsetSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdsetTime(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Задайте срок действия (цифрой число дней)',
                          reply_markup=menu_AdsetSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

############################# Создание / Объявления #########################################

def AdName(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Задайте имя объявления',
                          reply_markup=menu_AdSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )
def AdFb(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Укажите страницу ФБ',
                          reply_markup=menu_AdSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )
   
def AdIg(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Укажите страницу IG',
                          reply_markup=menu_AdSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdFormat(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Укажите формат',
                          reply_markup=menu_AdSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdCreative(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Добавьте креатив',
                          reply_markup=menu_AdSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdText(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Напишите текст рекламного объявления',
                          reply_markup=menu_AdSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )

def AdHeading(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Укажите Заголовок',
                          reply_markup=menu_AdSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )    

def AdURL(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Укажите URL',
                          reply_markup=menu_AdSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          ) 

def Go(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Объявление запущено',
                          reply_markup=menu_Go(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )                          

############################# Управление #########################################

def Control(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Управление',
                          reply_markup=menu_Control(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )   

def ControlShowCompany(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Список рекламных кампаний',
                          reply_markup=menu_ControlSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )   

def ControlShowAdset(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Список групп объявлений',
                          reply_markup=menu_ControlSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )                          

def ControlShowAd(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Список объявлений',
                          reply_markup=menu_ControlSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )   

def ControlDuplicate(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Что будем дублировать?',
                          reply_markup=menu_ControlSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )   

def ControlOn(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Что включить/выключить?',
                          reply_markup=menu_ControlSimple(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )                    

############################# Статистика ########################################

def Statistic(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='За какой период отобразить?',
                          reply_markup=menu_Statistic(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )   

def StatisticYesterday(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Статистика за вчера',
                          reply_markup=menu_Statistic(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          ) 

def StatisticToday(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Статистика за сегодня',
                          reply_markup=menu_Statistic(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          ) 

def StatisticWeek(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Статистика за неделю',
                          reply_markup=menu_Statistic(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          ) 

def StatisticMonth(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Статистика за месяц',
                          reply_markup=menu_Statistic(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )    

def StatisticPeriod(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Период',
                          reply_markup=menu_Statistic(),
                          message_id=query.message.message_id,
                          chat_id=query.message.chat_id
                          )                                                    

############################# main ##############################################

def main():
    mybot = Updater("769544739:AAGpBD1EVf9ZHtzzexX1JyYYDGkvfgWMkBs", request_kwargs=PROXY)
    
    logging.info('Бот запускается')   

############################# Хэндлеры старт ####################################

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main_menu'))
    dp.add_handler(CallbackQueryHandler(help, pattern='help'))

############################# Хэндлеры Главное меню ##############################

    dp.add_handler(CallbackQueryHandler(Company1, pattern='Company1'))
    dp.add_handler(CallbackQueryHandler(Control, pattern='Control'))
    dp.add_handler(CallbackQueryHandler(Statistic, pattern='Statistic'))
    dp.add_handler(CallbackQueryHandler(help, pattern='Pixel'))
    dp.add_handler(CallbackQueryHandler(help, pattern='help'))

############################# Хэндлеры Кампания Общие ############################

    dp.add_handler(CallbackQueryHandler(Company1, pattern='Company1'))
    dp.add_handler(CallbackQueryHandler(Company2, pattern='Company2'))
    dp.add_handler(CallbackQueryHandler(Company3, pattern='Company3'))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main_menu'))

############################# Хэндлеры Кампания ################################## 

    dp.add_handler(CallbackQueryHandler(CompanyName, pattern='CompanyName'))
    dp.add_handler(CallbackQueryHandler(CompanyTarget, pattern='CompanyTarget'))
    dp.add_handler(CallbackQueryHandler(CompanyBudget, pattern='CompanyBudget'))

############################# Хэндлеры Группа объявлений #########################

    dp.add_handler(CallbackQueryHandler(AdsetName, pattern='AdsetName'))
    dp.add_handler(CallbackQueryHandler(AdsetDynamic, pattern='AdsetDynamic'))
    dp.add_handler(CallbackQueryHandler(AdsetGender, pattern='AdsetGender'))
    dp.add_handler(CallbackQueryHandler(AdsetAge, pattern='AdsetAge'))
    dp.add_handler(CallbackQueryHandler(AdsetInterest, pattern='AdsetInterest'))
    dp.add_handler(CallbackQueryHandler(AdsetPlacement, pattern='AdsetPlacement'))
    dp.add_handler(CallbackQueryHandler(AdsetPС, pattern='AdsetPС'))
    dp.add_handler(CallbackQueryHandler(AdsetBudget, pattern='AdsetBudget'))
    dp.add_handler(CallbackQueryHandler(AdsetTime, pattern='AdsetTime'))

############################# Хэндлеры Объявления ################################

    dp.add_handler(CallbackQueryHandler(AdName, pattern='AdName'))
    dp.add_handler(CallbackQueryHandler(AdFb, pattern='AdFb'))
    dp.add_handler(CallbackQueryHandler(AdIg, pattern='AdIg'))
    dp.add_handler(CallbackQueryHandler(AdFormat, pattern='AdFormat'))
    dp.add_handler(CallbackQueryHandler(AdCreative, pattern='AdCreative'))
    dp.add_handler(CallbackQueryHandler(AdText, pattern='AdText'))
    dp.add_handler(CallbackQueryHandler(AdHeading, pattern='AdHeading'))
    dp.add_handler(CallbackQueryHandler(AdURL, pattern='AdURL'))
    dp.add_handler(CallbackQueryHandler(Go, pattern='Go'))

############################# Хэндлеры Управление ################################

    dp.add_handler(CallbackQueryHandler(ControlShowCompany, pattern='ControlShowCompany'))
    dp.add_handler(CallbackQueryHandler(ControlShowAdset, pattern='ControlShowAdset'))
    dp.add_handler(CallbackQueryHandler(ControlShowAd, pattern='ControlShowAd'))
    dp.add_handler(CallbackQueryHandler(ControlDuplicate, pattern='ControlDuplicate'))
    dp.add_handler(CallbackQueryHandler(ControlOn, pattern='ControlOn'))

############################# Хэндлеры Статистика ################################

    dp.add_handler(CallbackQueryHandler(StatisticYesterday, pattern='StatisticYesterday'))
    dp.add_handler(CallbackQueryHandler(StatisticToday, pattern='StatisticToday'))
    dp.add_handler(CallbackQueryHandler(StatisticWeek, pattern='StatisticWeek'))
    dp.add_handler(CallbackQueryHandler(StatisticMonth, pattern='StatisticMonth'))
    dp.add_handler(CallbackQueryHandler(StatisticPeriod, pattern='StatisticPeriod'))

    mybot.start_polling()
    mybot.idle() 

main()
