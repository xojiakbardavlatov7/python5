import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from btns import*


TOKEN = ("8809466266:AAGRfkX8dpRDiu88fqH1zAHmOddJehNcmXA")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=btnss)


@dp.message(Command('menu'))
async def menu_command(message: Message):
    await message.answer("Menuga xush kelibsiz :)", reply_markup=menu_btns)



















































































async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

print("working...")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())