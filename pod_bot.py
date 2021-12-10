import settings

from loguru import logger
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB", compression="zip")

def start_bot(update: Updater, context: CallbackContext):
    mytext = """Privetuly {}
    
Ya ponimau tol'ko komadu /start =)""".format(update.message.chat.first_name)
    update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
    text = "Privet {}, mne prichlo soobshenie: {}!".format(update.message.chat.first_name, update.message.text)
    logger.debug(update.message.text)
    
    update.message.reply_text(text)

def main():
    updtr = Updater(settings.TOKEN_TELEGRAM)

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    logger.info('Bot started!')
    main()