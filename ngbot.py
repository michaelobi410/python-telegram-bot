import requests
import time

TOKEN = '7945842569:AAHq6gjwPpTJSHCHjclT9ROnv6lPfhFHeQk'  # Replace with your bot's API token
URL = f'https://api.telegram.org/bot{TOKEN}/'

def get_updates(offset=None):
    response = requests.get(URL + 'getUpdates', params={'timeout': 100, 'offset': offset})
    return response.json()

def send_message(chat_id, text):
    requests.post(URL + 'sendMessage', params={'chat_id': chat_id, 'text': text})

def handle_commands(message):
    chat_id = message['chat']['id']
    command = message['text']

    if command == '/start':
        send_message(chat_id, 'Welcome! Use /help to see available commands.')
    elif command == '/help':
        send_message(chat_id, '/start - Start the bot\n/help - Show this help message\n/info - Get information about the bot\n/status - Check the bot status\n/deposit - Deposit funds\n/withdraw - Withdraw funds\n/setwallet - Set your wallet address\n/balance - Check your balance\n/referral - Get your referral link')
    elif command == '/info':
        send_message(chat_id, 'This bot helps manage your funds and wallet.')
    elif command == '/status':
        send_message(chat_id, 'Bot is running smoothly!')
    elif command == '/deposit':
        send_message(chat_id, 'Please send the amount you wish to deposit.')
    elif command == '/withdraw':
        send_message(chat_id, 'Please send the amount you wish to withdraw.')
    elif command.startswith('/setwallet'):
        wallet_address = command.split(' ', 1)[1] if ' ' in command else ''
        if wallet_address:
            send_message(chat_id, f'Wallet address set to: {wallet_address}')
        else:
            send_message(chat_id, 'Please provide a wallet address.')
    elif command == '/balance':
        send_message(chat_id, 'Your current balance is: 0.00 (this is just a placeholder)')
    elif command == '/referral':
        send_message(chat_id, 'Your referral link is: https://t.me/yourbot?start=referral_code')

def main():
    offset = None

    while True:
        updates = get_updates(offset)
        for update in updates['result']:
            offset = update['update_id'] + 1
            handle_commands(update['message'])
        time.sleep(1)

if __name__ == '__main__':
    main()
  
