from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN
from telegram import ReplyKeyboardMarkup


def parrot(bot, updater):
	print(bot.message.text)
	bot.message.reply_text(bot.message.text)

def sms(bot, updater):
	print('Команда /start')
	my_keyboard = ReplyKeyboardMarkup([['/start']], [['/input']], [['/output']])
	bot.message.reply_text('{}'.format(bot.message.chat.first_name), reply_markup=get_keyboard())

def get_keyboard():
	my_keyboard = ReplyKeyboardMarkup([['Ввод'], ['Вывод']]), resize_keyboard=True
	return my_keyboard

def main():
	main_bot = Updater(TG_TOKEN, use_context=True)
	main_bot.dispatcher.add_handler(CommandHandler('start', sms))
	main_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

	main_bot.start_polling()
	main_bot.idle()

main()