import telebot
import SlotBot
from bottoken import BotToken

API_TOKEN = BotToken()

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hello Im Bot!")



@bot.message_handler(commands=['Slotroll'])
def slot(message):
    bot.reply_to(message, SlotBot.Slotroll())

bot.infinity_polling()
