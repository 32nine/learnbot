
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem, datetime, logging

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080','urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
planet_white_list = {
    'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Sun', 'Moon',
    'Phobos', 'Deimos', 'Io', 'Europa', 'Ganymede', 'Callisto', 'Mimas', 'Enceladus', 'Tethys', 
    'Dione', 'Rhea', 'Titan', 'Hyperion', 'Iapetus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda'
}
# вызывает какойто дикий краш с полотенцем из ошибок
# logging.basicConfig(format='%(name)s - %(level)s - %(message)s',
#                     level=logging.INFO,
#                     filename='bot.log'
#                     )
             
def greet_user(bot, update):
    print('Вызван /start')
    update.message.reply_text('Привет')

def planet_to_day(bot, update):
    print('Вызван /planet')
    user_text = update.message.text.lower().split()
    planet = user_text[1].capitalize()
    print(planet)

    if planet in planet_white_list:
        planet_cls = getattr(ephem, planet, None)
        print(planet_cls)
        planet_cord = planet_cls(datetime.date.today())
        const = ephem.constellation(planet_cord)
        update.message.reply_text(f'{planet} in {const[1]} at now')
    else:
        update.message.reply_text('Я не знаю такой планеты')
        

       
'''def talk_to_me(bot, update):
    user_text = update.message.text
    user_date = update.message.date
    print(update.message)
    update.message.reply_text('Я тебя услышал')'''

def main():
        
        mybot = Updater("783780173:AAHsYu60QBClly1j5dRNiBTtiWotq-xgz80", request_kwargs=PROXY)

        dp = mybot.dispatcher
        dp.add_handler(CommandHandler('start', greet_user))
        dp.add_handler(CommandHandler('planet', planet_to_day))
        #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
       

        mybot.start_polling()
        mybot.idle()

main()
