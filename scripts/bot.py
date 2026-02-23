import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from social_api import post_to_vk  # Импортируем функцию отправки

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
VK_GROUP_ID = os.getenv('VK_GROUP_ID')  # ID вашего сообщества (положительное число)

async def handle_new_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == 'channel':
        text = update.effective_message.text or ""
        print(f"Новый пост в канале: {text}")
        post_to_vk(text, group_id=VK_GROUP_ID)
    else:
        print("Получено не из канала")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_new_post))
    print("Бот запущен, ждём новые посты в канале!")
    app.run_polling()
