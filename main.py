from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.error import BadRequest

# Вставьте сюда токен вашего бота
BOT_TOKEN = '7465751678:AAEzEh_TE1uYRjwVr3t6wDoF_k89ZdFwLec'

# ID чата, куда будут пересылаться сообщения (целевой чат)
TARGET_CHAT_ID = -1001587121624  # Замените на реальный ID чата

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message:
            await update.message.forward(chat_id=TARGET_CHAT_ID)
    except BadRequest as e:
        print(f"Ошибка при пересылке сообщения: {e}")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, forward_message))
    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()