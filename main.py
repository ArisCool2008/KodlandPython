import random
import telebot
import os

API_TOKEN = ('7746125940:AAGI75eAmJgPKnaDuarKf30sTaSmk54NUJw')

bot = telebot.TeleBot(API_TOKEN)

chance = (random.randint(0,10))

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hello Im Bot!")

@bot.message_handler(commands=['coder_meme'])
def sendcodermeme(message):
    if chance < 8:
        images = random.choice(os.listdir("coder_memes"))
        with open ('coder_memes/' + images, 'rb') as f:
            bot.send_photo(message.chat.id, f)
    if chance > 8:
        images = random.choice(os.listdir("Coder_meme"))
        with open ('Coder_meme/' + images, 'rb') as f:
            bot.send_photo(message.chat.id, f)


