"""
Автоответчик (простое приветствие)
Этот бот будет отвечать на команду /start, отправляя приветственное сообщение:
"""
from aiogram import Bot, Dispatcher, types
import asyncio

bot = Bot(token="YOUR_BOT_TOKEN")  # Заменить на реальный токен
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет! Я ваш бот. Чем могу помочь?")

async def on_start():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(on_start())
