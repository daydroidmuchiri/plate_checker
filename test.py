import unittest
import os
import openpyxl
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        # Load the Excel sheet
        file_path = "data.xlsx"
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        # Get a list of all the values in the first column of the sheet
        column = sheet['A']
        self.values = [cell.value for cell in column]

        # Set up the bot and start polling for messages
        TOKEN = "6081894512:AAG9pdS6tARvHZltY4DXha4d0bW9YzOEX1k"
        self.updater = Updater(TOKEN, use_context=True)
        self.dp = self.updater.dispatcher
        self.dp.add_handler(MessageHandler(Filters.text, self.message_handler))
        self.updater.start_polling()

    def tearDown(self):
        self.updater.stop()

    def test_registered_message(self):
        test_message = self.values[0]
        response = self.bot.send_message(chat_id=self.updater.effective_chat.id, text=test_message)
        self.assertEqual(response, "registered")

    def test_unregistered_message(self):
        test_message = "unregistered message"
        response = self.bot.send_message(chat_id=self.updater.effective_chat.id, text=test_message)
        self.assertEqual(response, "not registered")

    def message_handler(self, update, context):
        message = update.message.text
        if message in self.values:
            context.bot.send_message(chat_id=update.effective_chat.id, text="registered")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="not registered")

if __name__ == '__main__':
    unittest.main()
