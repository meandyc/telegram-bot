#! python3

import requests
import json
from pprint import pprint
from update import Update
from message import Message
from chat import Chat
from user import User

class TelegramBot:
        
    def __init__(self):
        self.API_URL = 'https://api.telegram.org/bot'
        with open('/home/andy/Documents/Python/telegram-bot/.telegram-api-token', 'r') as f:
            self.API_ID = f.read()
    
    def get_updates(self):
        """
        Use this method to receive incoming updates using long polling.
        Returns an Array of Update objects.
        """
        url = self.API_URL + self.API_ID + '/getUpdates'
        response = requests.get(url)
        if response.status_code == 200:
            updates = json.loads(response.text)
            if updates['ok']:
                return updates['result']
        else:
            print('Failed getting updates')

    def remove_banned_words(self, updates):
        """
        Remove messages with banned words.
        """
        for update in updates:
            # pprint(update)
            print(f'message_id: {update["message"]["message_id"]}')
            print(f'chat_id: {update["message"]["chat"]["id"]}')
            print(f'text: {update["message"]["text"]}')
            print('---')

            # url = self.API_URL + self.API_ID + '/deleteMessage'
            # params = {'chat_id': '-991250963', 'message_id': '81'}
            # response = requests.post(url, data=params)
            # if response.status_code == 200:
            #     result = json.loads(response.text)
            # else:
            #     print('Couldn\'t delete the message.')

    def send_message(self, chat_id='969768646', msg='Test message Telegram API'):
        """
        Use this method to send text messages. On success, the sent Message is returned.
        """
        url = self.API_URL + self.API_ID + '/sendMessage'
        params = {'chat_id': chat_id, 'text': msg}
        response = requests.post(url, data=params)
        if response.status_code == 200:
            json_response = json.loads(response.text)
            pprint(json_response)    
        else:
            print('Failed sending the message')

if __name__ == '__main__':
    # meandyc 969768646
    # TestGroup -991250963
    # Nilo -1001258742986 
    # Pablo 627140333
    
    bot = TelegramBot()
    # bot.send_message()
    bot.remove_banned_words(bot.get_updates())