import telebot

bot = telebot.TeleBot('1027984232:AAFRmLALJMkySUnLy_N4pM8DdPLG_khGl5Q')


@bot.message_handler(commands=['start'])
def start_message(message):
     bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()