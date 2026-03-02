import os
from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler

# BotFather থেকে পাওয়া টোকেন এখানে দিন
TOKEN = 'আপনার_বট_টোকেন_এখানে'

async def approve_request(update: Update, context):
    chat_join_request = update.chat_join_request
    try:
        await context.bot.approve_chat_join_request(
            chat_id=chat_join_request.chat.id, 
            user_id=chat_join_request.from_user.id
        )
        print(f"Approved: {chat_join_request.from_user.first_name}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(approve_request))
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
