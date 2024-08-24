import telebot
import requests
import json

# Создание экземпляр бота.
bot = telebot.TeleBot('##########')
API = '######'


# Функция обрабатывает команду start от пользователя.
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Доброго времени суток!!!'
                     f'Какой город тебя интересует?')


# Функция принимает от пользователя название города, обрабатвает
# и выдает какая погода и соответствующую картинку
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    bot.reply_to(message, f'Сейчас погода: {temp}')

    if temp > 25.0:
        file = open('./' + 'hot.jpg', 'rb')
        phrasa = 'Жаришка!'
    elif 15.0 <= temp <= 25.0:
        file = open('./' + 'cool.jpg', 'rb')
        phrasa = 'Хорошая погода))'
    else:
        file = open('./' + 'cold.png', 'rb')
        phrasa = 'Колотуннн!'
    bot.send_photo(message.chat.id, file, caption=phrasa)          


# Запуск бота
bot.polling(non_stop=True)
