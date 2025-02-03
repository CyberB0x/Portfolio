"""
Бот для уведомлений
Этот бот будет отправлять уведомления в определённое время, например, каждый день в 12:00. Для этого можно использовать модуль schedule для расписания задач.

Уведомления через Telegram-бота (с использованием schedule):
"""
import asyncio
import schedule
import time
from aiogram import Bot, Dispatcher, types

bot = Bot(token="YOUR_BOT_TOKEN")  # Заменить на реальный токен
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет! Я бот для уведомлений!")


async def send_notification():
    chat_id = "YOUR_CHAT_ID"  # Заменить на ID чата или пользователя
    await bot.send_message(chat_id, "Это ваше ежедневное уведомление!")


async def on_start():
    # Установим уведомления каждый день в 12:00
    schedule.every().day.at("12:00").do(lambda: asyncio.create_task(send_notification()))

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)  # Пауза для не блокирования asyncio


if __name__ == "__main__":
    asyncio.run(on_start())
