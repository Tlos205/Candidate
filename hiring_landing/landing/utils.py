import telegram
from django.conf import settings

async def send_to_telegram(candidate_data):
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
    message = (
        f"Новый кандидат:\n"
        f"Имя: {candidate_data['name']}\n"
        f"Email: {candidate_data['email']}\n"
        f"Телефон: {candidate_data['phone']}\n"
        f"Описание: {candidate_data['description']}"
    )
    await bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)