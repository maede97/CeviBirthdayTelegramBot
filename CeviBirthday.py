#!/usr/bin/python

# Telegram Imports
import telegram

# Other Imports
import configparser
import logging
import requests
import datetime
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s  %(message)s', level=logging.INFO)

# Read Configuration
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini'))

bot_token = config.get("Bot", "Token", fallback=None)
if bot_token == None:
    print("Error: Token not set.")
    exit()

send_users = config.get("Bot", "AllowedUsers", fallback=None)
if send_users == None:
    print("Error: AllowedUsers not set.")
    exit()

send_users = send_users.split(',')

ceviDB_email = config.get("Cevi", "Email")
ceviDB_token = config.get("Cevi", "Token")
ceviDB_group = config.get("Cevi", "Group")
ceviDB_filter = config.get("Cevi", "Filter")

# Create bot from token
bot = telegram.Bot(token=bot_token)

# Get dates in the right format yyyy-mm-dd
today = datetime.date.today().strftime("%Y-%m-%d")
tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

logging.info("Today:    " + today)
logging.info("Tomorrow: " + tomorrow)

def send_message_to_all_users(message):
    logging.info("Sending birthdays to all users")
    for uid in send_users:
        bot.sendMessage(chat_id=uid, text=message, parse_mode=telegram.ParseMode.MARKDOWN_V2)

def extract_birthdays(json):
    birthday_today = []
    birthday_tomorrow = []
    for person in json['people']:
        href = person['href']
        prename = person['first_name']
        lastname = person['last_name']
        # open this person
        r = requests.get(href + '?user_email={}&user_token={}'.format(ceviDB_email, ceviDB_token))
        if r.status_code == 200:
            # read this persons birthday
            json = r.json()
            birthday = json['people'][0]['birthday']
            age = datetime.date.today().year - int(birthday[:4])
            if birthday == today:
                birthday_today.append('{} {}, {}'.format(prename, lastname, age))
            elif birthday == tomorrow:
                birthday_tomorrow.append('{} {}, {}'.format(prename, lastname, age))
    
    #Build message and send it
    message = ""
    if len(birthday_today) > 0:
        message += "*Today*\n"
        message += "\n* ".join(birthday_today) + "\n"
    if len(birthday_tomorrow) > 0:
        message += "*Tomorrow*\n"
        message += "\n * ".join(birthday_tomorrow)
    if len(message) > 0:
        send_message_to_all_users(message)

def getAllBirthdays():
    # build URL string
    logging.info("Getting json from API")
    url = 'https://db.cevi.ch/groups/{}/people.json?filter_id={}&user_email={}&user_token={}'.format(ceviDB_group, ceviDB_filter, ceviDB_email, ceviDB_token)
    r = requests.get(url)
    if r.status_code == 200:
        extract_birthdays(r.json())
    else:
        logging.error("Could not get people from CeviDB api.")


getAllBirthdays()
