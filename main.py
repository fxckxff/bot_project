import config
import telebot
import requests
import ccxt

bot = telebot.TeleBot(config.token)
binance_api_key = config.api_key
binance_secret_key = config.secret_key

binance_client = ccxt.binance({
    'apiKey': binance_api_key,
    'secret': binance_secret_key,
})

# Получение данных о RSI для выбранной пары торгов
def get_rsi(symbol='BTC/USDT', timeframe='1h', period=14):
    ohlcv = binance_client.fetch_ohlcv(symbol, timeframe)
    closes = [tick[4] for tick in ohlcv]
    rsi = binance_client.rsi(closes, period)
    return rsi

# Функция для определения сигнала на вход в сделку на основе RSI
def trading_strategy(symbol='BTC/USDT', timeframe='1h', rsi_threshold=60):
    rsi = get_rsi(symbol, timeframe)
    print(f'Current RSI for {symbol} ({timeframe}): {rsi}')

    # Если RSI больше или равно пороговому значению, возвращаем True
    return rsi >= rsi_threshold


# Пример использования
if trading_strategy():
    print("Сигнал на вход в сделку!")
else:
    print("Нет сигнала на вход в сделку.")


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