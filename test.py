import unittest
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters

class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.updater = Updater(token='6081894512:AAG9pdS6tARvHZltY4DXha4d0bW9YzOEX1k', use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.bot = Bot(token='6081894512:AAG9pdS6tARvHZltY4DXha4d0bW9YzOEX1k')
        
        def message_handler(update, context):
            """Handler for messages sent to the bot."""
            # Your message handling logic here

        self.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
        
    def test_registered_message(self):
        test_message = 'Test message for registered users'
        chat_id = 123456  # Replace with a valid chat ID
        response = self.bot.send_message(chat_id=chat_id, text=test_message)
        self.assertEqual(response.text, test_message)
        
    def test_unregistered_message(self):
        test_message = 'Test message for unregistered users'
        chat_id = 654321  # Replace with a valid chat ID
        response = self.bot.send_message(chat_id=chat_id, text=test_message)
        self.assertEqual(response.text, test_message)

if __name__ == '__main__':
    unittest.main()
