from telegram.ext import Updater
from telegram.ext import Updater, CommandHandler
import ephem

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080','urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    print('Вызван /start')
    update.message.reply_text('Привет')

def planet_to_day():
        print('вызван /planet')

        planet = update.massage.reply_text('Введите название планеты')
        print(planet)

def main():
        
        mybot = Updater("783780173:AAHsYu60QBClly1j5dRNiBTtiWotq-xgz80", request_kwargs=PROXY)

        dp = mybot.dispatcher
        dp.add_handler(CommandHandler('start', greet_user))
        dp.add_handler(CommandHandler('planet', planet_to_day))

        mybot.start_polling()
        mybot.idle()

main()
