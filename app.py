from flask import Flask, render_template
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading

# ----------- تنظیمات اولیه -----------
app = Flask(__name__)
TOKEN = "توکن_ربات_خودت_اینجا_بذار"  # ← اینجا توکن رباتت رو بگذار

# ----------- قسمت وب (Mini App) -----------
@app.route('/')
def home():
    return render_template('index.html')

# ----------- قسمت ربات تلگرام -----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 باز کردن Mini App", web_app=WebAppInfo(url="https://your-app.onrender.com/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("سلام 👋 این مینی‌اپ من هست:", reply_markup=reply_markup)

def run_telegram_bot():
    app_telegram = ApplicationBuilder().token(TOKEN).build()
    app_telegram.add_handler(CommandHandler("start", start))
    app_telegram.run_polling()

# ----------- اجرای هم‌زمان وب‌سرور و ربات -----------
if __name__ == '__main__':
    threading.Thread(target=run_telegram_bot).start()
    app.run(host='0.0.0.0', port=5000)
