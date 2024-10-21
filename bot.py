import requests
import time

TOKEN = '7945842569:AAFkfHvAB-jqiPqa9ADGNe4RLI09XdGWQRc'  # Replace with your bot's API token
URL = f'https://api.telegram.org/

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Info", callback_data='info'),
            InlineKeyboardButton("Status", callback_data='status')
        ],
        [
            InlineKeyboardButton("Help", callback_data='help')
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome! Please choose an option:', reply_markup=reply_markup)

# Help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Use the buttons below to interact with the bot.')

# Callback query handler
def handle_callback_query(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()  # Acknowledge the callback

    if query.data == 'info':
        query.edit_message_text(text='This bot provides information and status updates.')
    elif query.data == 'status':
        query.edit_message_text(text='The bot is currently running smoothly.')
    elif query.data == 'help':
        query.edit_message_text(text='You can start over by clicking /start.')

def main():
    # Replace 'YOUR_TOKEN' with your bot's API token
    updater = Updater("YOUR_TOKEN")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CallbackQueryHandler(handle_callback_query))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
