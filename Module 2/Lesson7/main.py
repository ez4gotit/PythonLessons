#Telegram bot

#1 шаг это TelegramBot Token
#Где взять токен? У бота Bot Father https://t.me/BotFather

import asyncio
from email import message_from_binary_file
import logging
import random
from mailbox import Message
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.utils import keyboard
from aiogram.utils.keyboard import ReplyKeyboardBuilder
logging.basicConfig(level=logging.DEBUG)

file = "token.txt"

_token = ""

with open (file, 'r') as file:
    _token = file.read()

bot = Bot(token = _token)

dispatcher = Dispatcher()

users = {}
selected = 0

@dispatcher.message(F.text.lower() == "/start")
async def cmd_start(message: types.Message):
    buttons = [[types.KeyboardButton(text =  "election")]]

    builder = ReplyKeyboardBuilder()
    builder.add(buttons[0][0])
    users.setdefault(message.from_user.id, message.from_user.full_name)
    print(users)
    await message.answer("ку!",reply_markup=builder.as_markup())

@dispatcher.message( Command("start"))
async def cmd_start(message: types.Message):


    await message.answer("ку!")


@dispatcher.message(F.text.lower().contains("election"))
async def send_election(message: types.Message):
    if message.from_user.id == 1029020700:
        selected = random.choice(list(users.keys()))
        await bot.send_message(selected, "Ты выиграл!")
        for user in list(users.keys()):
            if user == selected:
                continue
            await bot.send_message(int(user), f'Выиграл пользователь: {users[selected]}')
    else:
        await message.answer("Вы не админ!")


async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())