from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Функция для обработки команды /start
async def start(update: Update, context):
    await update.message.reply_text("Привет! Я Echo-bot. Напиши мне что-нибудь!")

# Функция для обработки сообщений
async def echo(update: Update, context):
    # Отправляем обратно то же сообщение, которые получил бот
    await update.message.reply_text(update.message.text)

# Основная функция для запуска бота
def main():
    # Токен вашего бота
    app = ApplicationBuilder.token("Your_token").build()

    # Добавляем обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start)) # Обработчик команды /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo)) # Обработчик текстовых сообщений

    # Запускаем бота
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()

