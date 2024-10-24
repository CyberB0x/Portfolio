from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Application

song = "https://youtu.be/fUeUia0cGsE?si=McywhztSJRf6LArp"

async def song_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Song for you: {song}')


application = Application.builder().token("7937451091:AAG2fQ5DGPBnpYl5JHmK5IaB9ntU7EmIjck").build()

application.add_handler(CommandHandler("song", song_link))

application.run_polling()

