import telebot
import requests

import cfg



bot = telebot.TeleBot(cfg.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "ДАРОВА ЕБАТЬ")

@bot.message_handler(content_types=["text"])
def msg_response(message):
    answer = requests.get(cfg.REQUEST_URL, params=cfg.REQUEST_DATA).json()
    bot.send_message(message.chat.id, answer['quoteText'])


bot.polling()

