import pymongo
import urllib


db_client = pymongo.MongoClient("mongodb+srv://svyatS:"+urllib.parse.quote("4L6Bh8GFEb@nbHK")+"@cluster0.w1xg8.mongodb.net/telegaTeacher?retryWrites=true&w=majority")


# подключаемся к БД pyloungedb, если её нет, то будет создана
current_db = db_client["telegaTeacher"]  # dictionary style
# current_db = db_client.pyloungedb - attribute style

# получаем колекцию из нашей БД, если её нет, то будет создана
# Коллекция - это группа документов, которая хранится в БД MongoDB (эквалент таблицы в ркляционных базах)
collection = current_db["teacher "]  # current_db.youtubers

# Коллекции и базы данных в MongoDB created lazily - фактически создаются при вставке в них первого документа
# Данные в MongoDB представляются с помощью JSON-style документов
# можно явно указать желаемый айди, добавив ключ - '_id': n
question = {
    "Как дела?": [
        "Отлично",
        "Плохо"
    ]
}


# ins_result = collection.insert_one(question)  # добавляет одну запись в коллекцию collection
for item in collection.find():
    try:
        print(item["Как делаd?"])
    except KeyError:
        print("XZ")
