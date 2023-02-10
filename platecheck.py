import csv
from telegram.ext import Updater, MessageHandler, Filters

# Load the CSV file
file_path = "data.csv"
values = []
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        values.extend(row)

# Define the bot's behavior when a message is received
def message_handler(update, context):
    message = update.message.text
    if message in values:
        context.bot.send_message(chat_id=update.effective_chat.id, text="registered")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="not registered")

# Set up the bot and start polling for messages
TOKEN = "6081894512:AAG9pdS6tARvHZltY4DXha4d0bW9YzOEX1k"
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()
