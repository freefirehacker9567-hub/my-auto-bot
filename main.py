import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler

# Render এর জন্য ছোট একটি ওয়েব সার্ভার
app = Flask(__name__)
@app.route('/')
def health_check():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

# আপনার বটের আসল কাজ
TOKEN = '8722696203:AAHeZZJ9kJjzBBDQSCLepNIHKbb8GtHR9DM'

async def auto_approve(update: Update, context):
    request = update.chat_join_request
    try:
        await context.bot.approve_chat_join_request(chat_id=request.chat.id, user_id=request.from_user.id)
        # ইনবক্সে মেসেজ (ইউজার আগে বট স্টার্ট করলে পাবে)
        await context.bot.send_message(chat_id=request.from_user.id, text="স্বাগতম! আপনাকে চ্যানেলে অ্যাড করা হয়েছে ❤For Buy Premium Knock @lifemeanssex")
    except:
        pass

def main():
    # ওয়েব সার্ভার আলাদা ভাবে চালু করা
    threading.Thread(target=run_flask, daemon=True).start()
    
    # বট চালু করা
    application = Application.builder().token(TOKEN).build()
    application.add_handler(ChatJoinRequestHandler(auto_approve))
    application.run_polling()

if __name__ == '__main__':
    main()
