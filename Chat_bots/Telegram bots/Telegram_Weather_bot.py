import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Вставьте ваш API-ключ OpenWeatherMap
WEATHER_API_KEY = 'API KEY'

# Логирование для отладки
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Отправь мне название города, и я скажу тебе текущую погоду.')


# Функция для получения погоды
def get_weather(city_name: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)

    # Логирование ответа для отладки
    logger.info(f"Запрос к OpenWeather: {url}")
    logger.info(f"Ответ от OpenWeather: {response.status_code} - {response.text}")

    if response.status_code == 200:
        data = response.json()

        # Проверка, что данные о погоде есть
        if 'main' in data and 'weather' in data:
            main = data['main']
            weather = data['weather'][0]

            temperature = main['temp']
            feels_like = main['feels_like']
            description = weather['description']

            weather_report = (f"Погода в {city_name}:\n"
                              f"Температура: {temperature}°C\n"
                              f"Ощущается как: {feels_like}°C\n"
                              f"Описание: {description.capitalize()}")
            return weather_report
        else:
            return "Извините, не удалось найти данные о погоде для указанного города."
    else:
        # Обработка ошибок от API
        return f"Ошибка: {response.status_code}. Возможно, вы ввели некорректное название города."


# Функция для обработки текстовых сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    city_name = update.message.text
    weather_report = get_weather(city_name)
    await update.message.reply_text(weather_report)


# Функция для обработки ошибок
async def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f'Update {update} вызвал ошибку {context.error}')


# Основная функция
def main():
    # Вставьте токен вашего бота
    application = Application.builder().token("BOT TOKEN").build()

    # Диспетчер для регистрации обработчиков
    application.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Логирование ошибок
    application.add_error_handler(error)

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
