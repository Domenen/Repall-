from email import message
import eel
import telebot

TOKEN = 'TOKEN'

bot = telebot.TeleBot(TOKEN)

@eel.expose
def send_messege(chat_id, message):
    bot.send_message(chat_id, message)
    return 'Сообщение отправленно'


eel.init('web')
eel.start('main.html', size=(400, 600))