from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8619357016:AAGp4Olagb-BOuwSNJUwd5o-js2mJauG6iQ"

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    # если есть "67" в любом месте текста
    if "67" in text:
        await update.message.reply_text("слава 67")
        return
        
    if "@blaz_shiz" or "блазик помоги" in text:
        await update.message.reply_text("да иди ты нахуй")
        return

    if "42" or "пятёрка" in text:
        await update.message.reply_text("СЛАВА БОССУ 42")
        return

    # если написано ровно "6"
    if text == "6":
        await update.message.reply_text("7")
        return

    # если написано ровно "7"
    if text == "7":
        await update.message.reply_text("6")
        return


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

    app.run_polling()


if __name__ == "__main__":
    main()
