import telebot
import urllib
import pymongo

import cfg



bot = telebot.TeleBot(cfg.TOKEN)
db_client = pymongo.MongoClient("mongodb+srv://svyatS:"+urllib.parse.quote("4L6Bh8GFEb@nbHK")+"@cluster0.w1xg8.mongodb.net/telegaTeacher?retryWrites=true&w=majority")
current_db = db_client["telegaTeacher"]
collection = current_db["teacher "]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "шо надо?")

@bot.message_handler(content_types=["text"])
def msg_response(message):
    arr = "gg"
    for item in collection.find():
        try:
            arr = item[message.text]
        except KeyError:
            continue

    if(arr == "gg"):
        ins_result = collection.insert_one({
            message.text: []
        })
        answer = "Я не знаю такого вопроса!"
    else:
        answer = arr[0]
    bot.send_message(message.chat.id, answer)


bot.polling()

