import random
import telebot
import os

API_TOKEN = ('7746125940:AAGI75eAmJgPKnaDuarKf30sTaSmk54NUJw')

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, Im Bot! Today i'll help you provide info about pollution and its results. Use /Pollutionresults ")

@bot.message_handler(commands=['Pollutionresults'])
def send(message):
    chance = (random.randint(1,2))
    if chance == 1:
        bot.reply_to(message, "Smoke and heat from factories causes big damage to the nature.")
        smokeimage = random.choice(os.listdir("smoke"))
        with open ('smoke/' + smokeimage, 'rb') as f:
            bot.send_photo(message.chat.id, f)
    if chance == 2:
        waterimage = random.choice(os.listdir("water"))
        bot.reply_to(message, "Trash and toxic waste causes collosal damage to the ocean ecosystem")
        with open ('water/' + waterimage, 'rb') as f:
            bot.send_photo(message.chat.id, f)

bot.infinity_polling()
    




