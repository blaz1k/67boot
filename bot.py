from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = "8619357016:AAGp4Olagb-BOuwSNJUwd5o-js2mJauG6iQ"
ADMIN_ID = 6897181661  # <-- вставь свой ID

current_chat_id = None


# установка чата
async def setchat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_chat_id

    if update.effective_user.id != ADMIN_ID:
        return

    if not context.args:
        await update.message.reply_text("Используй: /setchat CHAT_ID")
        return

    try:
        current_chat_id = int(context.args[0])
        await update.message.reply_text(f"Чат установлен: {current_chat_id}")
    except:
        await update.message.reply_text("Ошибка ID")


# /say команда
async def say(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if current_chat_id is None:
        await update.message.reply_text("Сначала /setchat")
        return

    text = " ".join(context.args)

    if not text:
        await update.message.reply_text("Напиши текст")
        return

    await context.bot.send_message(chat_id=current_chat_id, text=text)


# пересылка всего
async def forward_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if current_chat_id is None:
        return

    if update.message:
        await context.bot.forward_message(
            chat_id=current_chat_id,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )


# твоя логика
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if "67" in text:
        await update.message.reply_text("67 СИКС СЕВЕЕЕЕЕЕН ПОКОЙОООООООООООО")
        return
    if "пинг" in text:
        await update.message.reply_text("ПОНГ, СОСИ ИРИС ЕБАНЫЙ")
        return
    if "навальный" in text:
        await update.message.reply_text("всем привет, с вами навальный!")
        return
    if "ссср" in text:
        await update.message.reply_text("в ссср все сосали мой хуй")
        return
    if "блазик" in text:
        await update.message.reply_text("да иди ты нахуй")
        return
    if "420" in text:
        await update.message.reply_text("пошли упоремся")
        return
    if "42" in text:
        await update.message.reply_text("СЛАВА БОССУ 42")
        return
    if "52" in text:
        await update.message.reply_text("52.")
        return
    if "кира" in text:
        await update.message.reply_text("!бан")
        return
    if "пацански" in text:
        await update.message.reply_text("пульс ровный как у моей матери")
        return
    if "андрей" in text:
        await update.message.reply_text("я андрей андреевич, сучка")
        return
    if "1488" in text:
        await update.message.reply_text("ПАСХАЛКОООООООООООООООООООООООООООООООООООООООООООООООООООООО")
        return
    if "69" in text:
        await update.message.reply_text("ну давай оформим")
        return
    if "фуг" in text:
        await update.message.reply_text("О ВЕЛИКИЙ ФУГ")
        return
    if "сам пошел" in text:
        await update.message.reply_text("завали ебало, ебаное уёбище, ты нахуй никто, а я - бог сучка")
        return
    if "ливолол" in text:
        await update.message.reply_text("ливолол.")
        return
    if "лолкек" in text:
        await update.message.reply_text("иди нахуй")
        return
    if "даша" in text:
        await update.message.reply_text("да я")
        return
    if "228" in text:
        await update.message.reply_text("пошли упоремся")
        return
    if "333" in text:
        await update.message.reply_text("z уже люто ларплю барт")
        return
    if "666" in text:
        await update.message.reply_text("да прибудет с тобой бог, грешный ты олух")
        return
    if "саня" in text:
        await update.message.reply_text("саню пощадите")
        return
    if "рим" in text:
        await update.message.reply_text("римский топ римский газ, кто не верит - тому в глаз")
        return
    if "блять" in text:
        await update.message.reply_text("не матерись хуев ты долбаеб")
        return
    if "пром" in text:
        await update.message.reply_text("ЗАВАЛИ ЕБАЛо")
        return
    if text == "6":
        await update.message.reply_text("7")
        return
    if text == "7":
        await update.message.reply_text("6")
        return
    if text == "ll":
        await update.message.reply_text("LL TEAM - мы не победим")
        return


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("setchat", setchat))
    app.add_handler(CommandHandler("say", say))
    app.add_handler(MessageHandler(filters.ALL, forward_all))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

    app.run_polling()


if __name__ == "__main__":
    main()
