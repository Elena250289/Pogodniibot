import telebot
import requests
import json

bot = telebot.TeleBot('7299418860:AAFX7wPuKBfXdVQnZxV7aCXNVNgDpzrZF8k')
API = '8172e111ac91e21b583aa3af7253d1f7'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Доброго времени суток!!!Какой город тебя интересует?')

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
    bot.send_photo(message.chat.id, file, caption= phrasa)                

bot.polling(non_stop=True)