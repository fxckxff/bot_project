import config
import telebot

bot = telebot.TeleBot(config.token)

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'Hallo mein Freund')
    print(message.chat.id)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
     bot.infinity_polling()