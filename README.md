# CeviBirthdayTelegramBot
Sends a message to users with all Cevi leaders with a birthday on that (or the next) day.

## Installation
Create a telegram bot and get the token, login to the CeviDB and get your user_token. Store all this information inside a file named `config.ini` (copy the template!).

Fill in the custom fields for the CeviDB and set up a cronjob to run for example every night or so.

To register users to receive messages, execute the helper script `InitHelper.py` and copy the user id after a `/start` command (inside telegram, from the user to the bot) to the configuration file.

## Usage
To periodically run the script, set up a cronjob (using `crontab -e`):
```[bash]
# Run this command every day at 08:00 in the morning
* 8 * * * python <PATH-TO-FOLDER>/CeviBirthday/CeviBirthday.py 1> <PATH-TO-FOLDER>/CeviBirthday/CeviBirthday.log 2>&1
```
