import ccxt
import os
import time
import asyncio
from asyncio import sleep
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils.executor import start_polling
import logging

api_key = "binance api key"
secret_key = "binance api secret"

API_TOKEN = 'tg bot api token'
channel_id = -100xxxxxx7

crypto_pairs = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOTUSDT", "XRPUSDT", "SOLUSDT", "LUNAUSDT", "LINKUSDT", "MATICUSDT", "ALGOUSDT", "AVAXUSDT", "FILUSDT", "XTZUSDT", "DOGEUSDT", "ATOMUSDT", "VETUSDT", "TRXUSDT", "XLMUSDT", "SUSHIUSDT", "EGLDUSDT", "1INCHUSDT", "ICXUSDT", "FTMUSDT", "ZILUSDT", "HNTUSDT", "CHRUSDT", "ZENUSDT", "CTKUSDT", "DODOUSDT", "GRTUSDT", "MASKUSDT", "OGNUSDT", "OCEANUSDT", "BATUSDT", "CELRUSDT", "DENTUSDT", "STORJUSDT", "REEFUSDT", "TLMUSDT", "LINAUSDT",  "GHSTUSDT", "LITUSDT", "FRONTUSDT", "VTHOUSDT", "PERLUSDT", "MTLUSDT", "DREPUSDT", "CVCUSDT", "ARDRUSDT", "BANDUSDT", "SRMUSDT", "BTSUSDT", "AXSUSDT", "SCUSDT", "STMXUSDT", "WINUSDT", "BLZUSDT", "COTIUSDT", "TWTUSDT", "ZRXUSDT"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def get_binance_prices(crypto_pairs, api_key, secret_key):
    binance = ccxt.binance({
        'apiKey': api_key,
        'secret': secret_key
    })
    prices = {}

    for pair in crypto_pairs:
        ticker = binance.fetch_ticker(pair)
        prices[pair] = ticker['ask']

    return prices

async def send_message(message: str):
    await bot.send_message(chat_id=channel_id, text=message, parse_mode=ParseMode.MARKDOWN)

async def on_startup(dp):
    await send_message("STARTED. v1 (alpha beta)")

async def price_monitor():
    old_prices = get_binance_prices(crypto_pairs, api_key, secret_key)

    while True:
        await sleep(60)
        new_prices = get_binance_prices(crypto_pairs, api_key, secret_key)

        for pair in crypto_pairs:
            token_name = pair.replace("USDT", "")
            old_price = old_prices[pair]
            new_price = new_prices[pair]
            if old_price == 0:
                continue
            price_difference = new_price - old_price
            percentage_difference = (price_difference / old_price) * 100

            if abs(percentage_difference) >= 5:
                if price_difference > 0:
                    direction = "🟢"
                    action = "PUMP"
                else:
                    direction = "🔴"
                    action = "DUMP"

                message = f"{direction} #{token_name} | {action} | {abs(percentage_difference):.2f}% ({abs(price_difference):.2f}$) | Current price ${new_price:.2f}"
                await send_message(message)

        old_prices = new_prices


async def on_startup_and_monitor(dp):
    await on_startup(dp)
    await price_monitor()


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup_and_monitor, skip_updates=True)