import telebot
from config import API

bot = telebot.TeleBot(API)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привествую вас в виртуальной симуляции "Hartswood". Начнем игру.')
