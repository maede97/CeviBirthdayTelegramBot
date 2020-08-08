# CeviBirthdayTelegramBot
Sends a message to users with birthdays on that day.

## Installation
Create a telegram bot and get the token, login to the CeviDB and get your user_token. Store all this information inside a file named `config.ini` (copy the template!).

Fill in the custom fields for the CeviDB and set up a cronjob to run for example every night or so.

To register users to receive messages, execute the helper script `InitHelper.py` and copy the user id after a `/start` command (inside telegram, from the user to the bot) to the configuration file.
