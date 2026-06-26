from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

TOKEN = "8854074867:AAGQYvrHH5-GiiuT7OxeVVGUcnPbE_mavn8"

LINK = "https://t.me/+a8ShciFJS0w1ZjBl"

async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        request = update.chat_join_request

        await context.bot.send_message(
            chat_id=request.user_chat_id,
            text=f"ধন্যবাদ। নিচের লিংকে ক্লিক করুন:\n\n{LINK}"
        )

    except Exception as e:
        print(e)

app = Application.builder().token(TOKEN).build()

app.add_handler(ChatJoinRequestHandler(join_request))

app.run_polling()
