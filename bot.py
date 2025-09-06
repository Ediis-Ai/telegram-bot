import os
from flask import Flask
from telethon import TelegramClient, events

# گرفتن متغیرهای محیطی
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ساخت کلاینت ربات
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# هندلر ساده: هر پیامی بیاد، جواب میده
@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.reply("سلام 👋 من روی Render ران هستم!")

# --- Flask برای زنده نگه داشتن سرویس ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# اجرای Telethon
if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.create_task(bot.run_until_disconnected())

    # Flask روی پورت Render ران میشه
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
