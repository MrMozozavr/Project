from pyparsing import str_type
import time
import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert
from config import TOKEN
cg = CoinGeckoAPI()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1.add(types.KeyboardButton('Курс крипты'), types.KeyboardButton('Курс фиата'), types.KeyboardButton('Конвертер'), types.KeyboardButton('Ваша крипта'), types.KeyboardButton('❓ИНФО'))
    cr = bot.send_message(message.chat.id, 'Мы на главной\nЕсли бот перестал работать, напишите команду:\n/start', reply_markup=b1)
    bot.register_next_step_handler(cr, step)
    if message.text == '/start':
        return main

def step(message):
    if message.text == 'Курс крипты':
        step2(message)
    elif message.text == 'Курс фиата':
        fiat(message)
    elif message.text == 'Конвертер':
        convert1(message)
    elif message.text == 'Ваша крипта':
        yourcrypto(message)
    elif message.text == '❓ИНФО':
        donate(message)
    else:
        bot.send_message(message.chat.id,'Не понимаю о чём вы 🤨')
        time.sleep(1)
        main(message)

def donate(message):
    bot.send_message(message.chat.id, 'На чай создателю\n(MetaMask): <code>0x136Bb3261BB55a780678e71578BC40dB35E2bb69</code>\nОффициальный канал бота t.me/lazybees\nversion bot 1.3', parse_mode="html")
    main(message)

def yourcrypto(message):
    startKBoard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    id = types.KeyboardButton(text="Курс по id")
    id2 = types.KeyboardButton(text="Узнать id крипты")
    back = types.KeyboardButton(text="Назад")
    startKBoard.add(id, id2, back)
    msg = bot.send_message(message.chat.id, 'Вы можете посмотреть курс криптовалют по "id"', reply_markup=startKBoard)
    bot.register_next_step_handler(msg, yourcrypto1)

def yourcrypto1(message):
    if message.text == 'Узнать id крипты':
        yourcrypto3(message)
    elif message.text == 'Курс по id':
        yourcrypto2(message)
    elif message.text == 'Назад':
        main(message)

def yourcrypto2(message):
    msg = bot.send_message(message.chat.id, 'Введите id желаемой криптовалюты:')
    bot.register_next_step_handler(msg, yourcrypto2_1)

def yourcrypto2_1(message):
    msg = message.text
    try:
        price = cg.get_price(ids=msg, vs_currencies='usd')
        bot.send_message(message.chat.id, f'Цена {msg} == {price[msg]["usd"]} $')
    except KeyError:
        msg = 'bitcoin'
        bot.send_message(message.chat.id,'Вы ввели неправильный id')
        time.sleep(2)
    yourcrypto(message)

def yourcrypto3(message):
    bot.send_document(message.chat.id, 'BQACAgIAAxkBAAIE6GJzvcmgGWvGgT0CzM2QJVZOr4MkAAJ5HAACr9OhS344eYi36-j8JAQ')
    time.sleep(0.2)
    main(message)

def convert1(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1.add(types.KeyboardButton('Bitcoin'),   types.KeyboardButton('Ethereum'),
        types.KeyboardButton('Binance Coin'), types.KeyboardButton('litecoin'),
        types.KeyboardButton('Polygon'),      types.KeyboardButton('XRP'),
        types.KeyboardButton('Solana'),       types.KeyboardButton('Cardano'),
        types.KeyboardButton('Polkadot'),     types.KeyboardButton('Avalanche'),
        types.KeyboardButton('Terra'),        types.KeyboardButton('Cosmos Hub'),
        types.KeyboardButton('Dogecoin'),     types.KeyboardButton('Dai'),
        types.KeyboardButton('Dash'),         types.KeyboardButton('Cronos'),
        types.KeyboardButton('Chainlink'),    types.KeyboardButton('FTX Token'),
        types.KeyboardButton('TRON'),         types.KeyboardButton('The Sandbox'),
        types.KeyboardButton('Uniswap'),      types.KeyboardButton('Назад'))
    msg = bot.send_message(message.chat.id, 'Выберите криптовалюту:', reply_markup=b1)
    bot.register_next_step_handler(msg, convert2)

def convert2(message):
    if message.text == 'Bitcoin':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y1)
    elif message.text == 'Ethereum':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y2)
    elif message.text == 'Binance Coin':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y3)
    elif message.text == 'litecoin':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y4)
    elif message.text == 'Polygon':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y5)
    elif message.text == 'XRP':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y6)
    elif message.text == 'Solana':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y7)
    elif message.text == 'Cardano':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y8)
    elif message.text == 'Polkadot':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y9)
    elif message.text == 'Avalanche':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y10)
    elif message.text == 'Terra':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y11)
    elif message.text == 'Cosmos Hub':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y12)
    elif message.text == 'Dogecoin':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y13)
    elif message.text == 'Dai':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y14)
    elif message.text == 'Dash':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y15)
    elif message.text == 'Cronos':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y16)
    elif message.text == 'Chainlink':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y17)
    elif message.text == 'FTX Token':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y18)
    elif message.text == 'TRON':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y19)
    elif message.text == 'The Sandbox':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y20)
    elif message.text == 'Uniswap':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать?')
        bot.register_next_step_handler(msg, y21)
    elif message.text == 'Назад':
        main(message)
    else:
        bot.send_message(message.chat.id,'Не понимаю о чём вы 🤨')
        time.sleep(0.5)
        main(message)

def fiat(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('USD'), types.KeyboardButton('UAH'), types.KeyboardButton('Главная'))
    q = bot.send_message(message.chat.id, 'Курс фиата', reply_markup=b1)
    bot.register_next_step_handler(q, fiat_step2)

def fiat_step2(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Назад'))
    if message.text == 'USD':
        price = convert(base='USD', amount=1, to=['RUB', 'EUR', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 USD == {price["RUB"]} RUB\n'
                                          f'1 USD == {price["EUR"]} EUR\n'
                         f'1 USD == {price["UAH"]} UAH\n'
                         f'1 USD == {price["KZT"]} KZT')
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    if message.text == 'UAH':
        price = convert(base='UAH', amount=1, to=['USD', 'EUR', 'RUB', 'KZT'])
        bot.send_message(message.chat.id, f'1 UAH == {price["USD"]} USD\n'
                                              f'1 UAH == {price["EUR"]} EUR\n'
                                              f'1 UAH == {price["RUB"]} RUB\n'
                                              f'1 UAH == {price["KZT"]} KZT')
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    if message.text == 'Главная':
        main(message)

def y1(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🌐Bitcoin == {price["bitcoin"]["usd"] * convert2} $')
    main(message)

def y2(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='ethereum', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔹Ethereum == {price["ethereum"]["usd"] * convert2} $')
    main(message)

def y3(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='Binancecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 〽️Binance Coin == {price["Binancecoin"]["usd"] * convert2} $')
    main(message)

def y4(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='litecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔸Litecoin  == {price["litecoin"]["usd"] * convert2} $')
    main(message)

def y5(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='matic-network', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔹Polygon == {price["matic-network"]["usd"] * convert2} $')
    main(message)

def y6(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='ripple', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔹XRP == {price["ripple"]["usd"] * convert2} $')
    main(message)

def y7(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='solana', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔹Solana == {price["solana"]["usd"] * convert2} $')
    main(message)

def y8(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='cardano', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔹Cardano == {price["cardano"]["usd"] * convert2} $')
    main(message)

def y9(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='polkadot', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} • Polkadot == {price["polkadot"]["usd"] * convert2} $')
    main(message)

def y10(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='avalanche-2', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} • Avalanche == {price["avalanche-2"]["usd"] * convert2} $')
    main(message)

def y11(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='terra-luna', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔹Terra == {price["terra-luna"]["usd"] * convert2} $')
    main(message)

def y12(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='cosmos', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} • Cosmos Hub == {price["cosmos"]["usd"] * convert2} $')
    main(message)

def y13(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='dogecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} Dogecoin == {price["dogecoin"]["usd"] * convert2} $')
    main(message)

def y14(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='dai', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔹Dai == {price["dai"]["usd"] * convert2} $')
    main(message)

def y15(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='dash', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔹Dash == {price["Dash"]["usd"] * convert2} $')
    main(message)

def y16(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='crypto-com-chain', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} • Cronos == {price["crypto-com-chain"]["usd"] * convert2} $')
    main(message)

def y17(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='chainlink', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} • Chainlink == {price["chainlink"]["usd"] * convert2} $')
    main(message)

def y18(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='ftx-token', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 〽️FTX Token == {price["ftx-token"]["usd"] * convert2} $')
    main(message)

def y19(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='tron', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} • TRON == {price["tron"]["usd"] * convert2} $')
    main(message)

def y20(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='the-sandbox', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🔸The Sandbox == {price["the-sandbox"]["usd"] * convert2} $')
    main(message)

def y21(message):
    convert2 = message.text
    convert2 = float(convert2)

    price = cg.get_price(ids='uniswap', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} 🦄Uniswap == {price["uniswap"]["usd"] * convert2} $')
    main(message)

def step2(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Курс к USD'), types.KeyboardButton('Курс к UAH'), types.KeyboardButton('Главная'))
    q = bot.send_message(message.chat.id, 'Курс моих токенов', reply_markup=b1)
    bot.register_next_step_handler(q, step3)

def step3(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Назад'))
    if message.text == 'Курс к USD':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, matic-network, uniswap, dogecoin, terra-luna, ripple, solana, cardano, polkadot, avalanche-2, dai, the-sandbox, dash, crypto-com-chain, cosmos, ftx-token, tron, chainlink, binancecoin', vs_currencies='usd')
        bot.send_message(message.chat.id, f'Мои токены:\n\n'
                                          f'🌐Bitcoin == {price["bitcoin"]["usd"]} $\n'
                                          f'🔹Ethereum == {price["ethereum"]["usd"]} $\n\n'
                                          f'〽️Binance Coin == {price["binancecoin"]["usd"]} $\n'
                                          f'🔸Litecoin == {price["litecoin"]["usd"]} $\n'
                                          f'🔹Polygon == {price["matic-network"]["usd"]} $\n'
                                          f'🔹XRP == {price["ripple"]["usd"]} $\n'
                                          f'🔹Solana == {price["solana"]["usd"]} $\n'
                                          f'🔹Cardano == {price["cardano"]["usd"]} $\n'
                                          f'• Polkadot == {price["polkadot"]["usd"]} $\n'
                                          f'• Avalanche == {price["avalanche-2"]["usd"]} $\n'
                                          f'🔹Terra == {price["terra-luna"]["usd"]} $\n\n'
                                          f'• Cosmos Hub == {price["cosmos"]["usd"]} $\n'
                                          f'🦮Dogecoin == {price["dogecoin"]["usd"]} $\n'
                                          f'🔹Dai == {price["dai"]["usd"]} $\n'
                                          f'🔹Dash == {price["dash"]["usd"]} $\n'
                                          f'• Cronos == {price["crypto-com-chain"]["usd"]} $\n'
                                          f'• Chainlink == {price["chainlink"]["usd"]} $\n'
                                          f'〽️FTX Token == {price["ftx-token"]["usd"]} $\n'
                                          f'• TRON == {price["tron"]["usd"]} $\n\n'
                                          f'🔸The Sandbox == {price["the-sandbox"]["usd"]} $\n'
                                          f'🦄Uniswap == {price["uniswap"]["usd"]} $', reply_markup=b1)
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, step2)

    elif message.text == 'Курс к UAH':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, matic-network, uniswap, dogecoin, terra-luna, ripple, solana, cardano, polkadot, avalanche-2, dai, the-sandbox, dash, crypto-com-chain, cosmos, ftx-token, tron, chainlink, binancecoin', vs_currencies='uah')
        bot.send_message(message.chat.id, f'Мои токены:\n\n'
                                              f'🌐Bitcoin == {price["bitcoin"]["uah"]} ₴\n'
                                              f'🔹Ethereum == {price["ethereum"]["uah"]} ₴\n\n'
                                              f'〽️Binance Coin == {price["binancecoin"]["uah"]} ₴\n'
                                              f'🔸Litecoin == {price["litecoin"]["uah"]} ₴\n'
                                              f'🔹Polygon == {price["matic-network"]["uah"]} ₴\n'
                                              f'🔹XRP == {price["ripple"]["uah"]} ₴\n'
                                              f'🔹Solana == {price["solana"]["uah"]} ₴\n'
                                              f'🔹Cardano == {price["cardano"]["uah"]} ₴\n'
                                              f'• Polkadot == {price["polkadot"]["uah"]} ₴\n'
                                              f'• Avalanche == {price["avalanche-2"]["uah"]} ₴\n'
                                              f'🔹Terra == {price["terra-luna"]["uah"]} ₴\n\n'
                                              f'• Cosmos Hub == {price["cosmos"]["uah"]} ₴\n'
                                              f'Dogecoin == {price["dogecoin"]["uah"]} ₴\n'
                                              f'🔹Dai == {price["dai"]["uah"]} ₴\n'
                                              f'🔹Dash == {price["dash"]["uah"]} ₴\n'
                                              f'• Cronos == {price["crypto-com-chain"]["uah"]} ₴\n'
                                              f'• Chainlink == {price["chainlink"]["uah"]} ₴\n'
                                              f'〽️FTX Token == {price["ftx-token"]["uah"]} ₴\n'
                                              f'• TRON == {price["tron"]["uah"]} ₴\n\n'
                                              f'🔸The Sandbox == {price["the-sandbox"]["uah"]} ₴\n'
                                              f'🦄Uniswap == {price["uniswap"]["uah"]} ₴', reply_markup=b1)
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, step2)
    elif message.text == 'Главная':
        main(message)
    else:
        bot.send_message(message.chat.id,'Не понимаю о чём вы 🤨')
        time.sleep(0.5)
        main(message)

if __name__ == '__main__':
    bot.polling(none_stop=True)