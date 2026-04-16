from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8619357016:AAGp4Olagb-BOuwSNJUwd5o-js2mJauG6iQ"

async def reply_67(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "67":
        await update.message.reply_text("слава 67")
    if update.message.text == "6":
        await update.message.reply_text("7")
    if "67" in text:
        await update.message.reply_text("ААААААААА СИКС СЕВЕЕН")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_67))

app.run_polling()
