from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8619357016:AAGp4Olagb-BOuwSNJUwd5o-js2mJauG6iQ"

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # 1) если есть "67" в любом месте текста
    if "67" in text:
        await update.message.reply_text("ААААА СИКС СЕВЕЕЕН 67 ПОКОЙО")
        return

    # 2) если написали просто "6" → отвечаем "7"
    if text == "6":
        await update.message.reply_text("7")
        return

    # 3) если написали просто "7" → отвечаем "6"
    if text == "7":
        await update.message.reply_text("6")
        return


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

app.run_polling()
