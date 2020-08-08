#!/usr/bin/python

# Telegram Imports
from telegram.ext import Updater, CommandHandler

# Other Imports
import configparser
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s  %(message)s', level=logging.INFO)

# Read Configuration
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini'))

bot_token = config.get("Bot", "Token", fallback=None)
if bot_token == None:
    print("Error: Token not set.")
    exit()

def start(update, context):
    logging.info("New user: \"{}\"".format(update.message.chat_id))
    update.message.reply_text("Thank you. You should receive birthday updates.")

updater = Updater(bot_token, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start",start))

updater.start_polling()

# Run until CTRL+C
updater.idle()


