'''
Telegram_Bot
'''

from telebot import TeleBot
from telebot.types import Message


bot = TeleBot('6736783045:AAFdJooWd3hZ5lHdPbMWPNvgVo0euSCfgHo')

@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    print(chat_id)
    bot.send_message(chat_id, f"Assalom alekum BRATIM {full_name}")


@bot.message_handler(content_types=['text', 'photo'])
def get_text(message: Message):
    chat_id = message.chat.id
    text = message.text
    # bot.send_message(chat_id, text)
    bot.copy_message(-4165120968, chat_id, message.message_id)


@bot.message_handler(content_types=['video'])
def get_video(video: Message):
    chat_id = video.chat.id
    bot.send_video(-4165120968, chat_id)




bot.polling()






























