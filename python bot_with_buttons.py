import requests
import time

TOKEN = '7945842569:AAHq6gjwPpTJSHCHjclT9ROnv6lPfhFHeQk'  # Replace with your bot's API token
URL = f'https://api.telegram.org/bot{TOKEN}/'

def get_updates(offset=None):
    response = requests.get(URL + 'getUpdates', params={'timeout': 100, 'offset': offset})
    return response.json()

def send_message(chat_id, text, reply_markup=None):
    payload = {'chat_id': chat_id, 'text': text}
    if reply_markup:
        payload['reply_markup'] = reply_markup
    requests.post(URL + 'sendMessage', json=payload)

def create_keyboard():
    keyboard = {
        'inline_keyboard': [
            [
                {'text': 'Info', 'callback_data': 'info'},
                {'text': 'Status', 'callback_data': 'status'}
            ],
            [
                {'text': 'Help', 'callback_data': 'help'}
            ]
        ]
    }
    return keyboard

def handle_commands(message):
    chat_id = message['chat']['id']
    command = message['text']

    if command == '/start':
        reply_markup = create_keyboard()
        send_message(chat_id, 'Welcome! Please choose an option:', reply_markup)
    elif command == '/help':
        send_message(chat_id, 'Use the buttons below to interact with the bot.')

def handle_callback_query(callback_query):
    chat_id = callback_query['message']['chat']['id']
    data = callback_query['data']
    
    if data == 'info':
        send_message(chat_id, 'This bot provides information and status updates.')
    elif data == 'status':
        send_message(chat_id, 'The bot is currently running smoothly.')
    elif data == 'help':
        send_message(chat_id, 'You can start over by clicking /start.')

def main():
    offset = None

    while True:
        updates = get_updates(offset)
        for update in updates['result']:
            offset = update['update_id'] + 1
            
            if 'message' in update:
                handle_commands(update['message'])
            elif 'callback_query' in update:
                handle_callback_query(update['callback_query'])
                
        time.sleep(1)

if __name__ == '__main__':
    main()
               
