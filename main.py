import os
from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

# আপনার Bot Token এখানে দিন
TOKEN = '8722696203:AAE4oWJy9zZJs-5dmORunDiZP6aS0QHTBkw'

# আপনার কাস্টম মেসেজ এখানে লিখুন
WELCOME_MESSAGE = "আমাদের চ্যানেলে জয়েন করার জন্য আপনাকে ধন্যবাদ! ❤️\nএখানে আপনি নিয়মিত আপডেট পাবেন।"

async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_join_request = update.chat_join_request
    user_id = chat_join_request.from_user.id
    chat_id = chat_join_request.chat.id
    user_name = chat_join_request.from_user.first_name

    try:
        # ১. জয়েন রিকোয়েস্ট অ্যাপ্রুভ করা
        await context.bot.approve_chat_join_request(
            chat_id=chat_id, 
            user_id=user_id
        )
        print(f"Approved: {user_name}")

        # ২. ইউজারকে ইনবক্সে মেসেজ পাঠানো
        await context.bot.send_message(
            chat_id=user_id, 
            text=f"হ্যালো {user_name}!\n{WELCOME_MESSAGE}"
        )
        print(f"Message sent to: {user_name}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    # জয়েন রিকোয়েস্ট হ্যান্ডেলার
    app.add_handler(ChatJoinRequestHandler(approve_request))
    
    print("Bot is running with Inbox Message feature...")
    app.run_polling()

if __name__ == '__main__':
    main()
