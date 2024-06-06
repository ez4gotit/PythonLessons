#Telegram bot

#1 шаг это TelegramBot Token
#Где взять токен? У бота Bot Father https://t.me/BotFather

import asyncio
import logging
from mailbox import Message
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder


file = "token.txt"
_token = ""
with open(file, 'r') as file:
    _token = file.read()

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token =_token)

dp = Dispatcher()

@dp.message(Command("ку"))
async def cmd_start(message: types.Message):
    buttons = [
            [types.KeyboardButton(text = "Кууууу!")],
            [types.KeyboardButton(text = "Не ку :(")]
    ]
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text = "Кууууу!"))
    builder.add(types.KeyboardButton(text = "Не ку :("))
    for i in range(0,100):
        builder.add(types.KeyboardButton(text = f"Куууууу"+"у"*i+"!"))
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder="выбекрите ку")
    await message.answer("Q????",reply_markup=builder.as_markup()) 
@dp.message(F.text.lower() == "кууууу!")
async def pure_sus(message: types.Message):
    await message.reply("ХАРОШ!")

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())