import telebot

from cfg import *
from models import core_question

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = "Я бот-студент-хелп, вы можете узнать ответ на любой вопрос, а если такого вопроса нет, задать и получить ответ. Выберите категории вопросов:"
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_lessons = telebot.types.KeyboardButton(text="Занятия")
    btn_work = telebot.types.KeyboardButton(text="Работа Вуза")
    btn_teachers = telebot.types.KeyboardButton(text="Преподаватели")
    keyboard.add(btn_lessons, btn_work, btn_teachers)
    bot.reply_to(message, text, reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def msg_response(message):
    category = message.text
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if (category == "Занятия" or category == "Работа Вуза" or category == "Преподаватели" or category == "Другой вопрос"):
        results = core_question.select().where(core_question.category == category)

        for question in results:
            btn = telebot.types.KeyboardButton(text=str(question.question))
            keyboard.add(btn)

        answer = "Выбери вопрос который тебя интересует"


    else:
        category = "Другой вопрос"
        # cursor.execute(f"SELECT * FROM Question WHERE question={message.text}")
        answer = core_question.get_or_none(core_question.question == message.text)
        if answer is not None:
            answer.count += 1
            answer.save()
            answer = answer.answer
        else:
            answer = "Такого вопроса нет"
            question = core_question(
                question=message.text,
                category=category
            )
            question.save()

        btn_lessons = telebot.types.KeyboardButton(text="Занятия")
        btn_work = telebot.types.KeyboardButton(text="Работа Вуза")
        btn_teachers = telebot.types.KeyboardButton(text="Преподаватели")
        keyboard.add(btn_lessons, btn_work, btn_teachers)

    bot.send_message(message.chat.id, answer, reply_markup=keyboard)


bot.polling()
