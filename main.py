import telebot
from telebot import types
import requests
import sqlalchemy
import sqlalchemy_utils
from flask import Flask
from models import db
from bot_id import get_id
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://tgbot:rpgbot@localhost:5432/tgrpgbotgame'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Ok')
# bot = telebot.TeleBot(get_id())
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, ' Привет! Я бот для просто рпг игры! У тебя уже есть аккаунт или ты хочешь создать новый?')
#     # api request
#     # api.openweathermap.org/data/2.5/weather?q=Moscow,ru&APPID=8713dbc118a9579c4173ac3a72b1bc65
#     weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&APPID=8713dbc118a9579c4173ac3a72b1bc65&units=metric')
#     bot.send_message(message.chat.id, f'А погода у нас {weather.text} ')
#
# @bot.message_handler(commands=["geo"])
# def geo(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
#     keyboard.add(button_geo)
#     bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)
#
# @bot.message_handler(content_types=["location"])
# def location(message):
#     if message.location is not None:
#         print(message.location)
#         print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
#
#
#
if __name__ == '__main__':
    app.run(debug=True)