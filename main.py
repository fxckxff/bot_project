import config
import telebot
import requests

bot = telebot.TeleBot(config.token)

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'Hallo')
    print(message.chat.id)

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

def get_price():
    url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
    response = requests.get(url)
    data = response.json()
    return data['data']['rates']['USD']+'$'

@bot.message_handler(commands=['btc'])
def send_price(message):
    bot.send_message(message.chat.id, get_price())

print('bot arbeitet')
if __name__ == '__main__':
     bot.infinity_polling()