#! python3

import requests
import json
from pprint import pprint

class TelegramBot:
    def __init__(self):
        self.API_URL = 'https://api.telegram.org/bot'
        with open('/home/andy/Documents/Python/telegram-bot/.telegram-api-token', 'r') as f:
            self.API_ID = f.read()
        self.updates_offset = None
    
    def get_updates(self):
        """
        Use this method to receive incoming updates using long polling.
        Returns an Array of Update objects.
        """
        url = self.API_URL + self.API_ID + '/getUpdates'
        params = {'offset': self.updates_offset, 'timeout': 2}
        response = requests.get(url, offset=self.updates_offset)
        if response.status_code == 200:
            updates = json.loads(response.text)
            if updates['ok']:
                result = updates['result']
                self.updates_offset = result[-1]['update_id'] + 1
                return result
        else:
            print('Failed getting updates')

    def remove_banned_words(self, updates):
        """
        Remove messages with banned words.
        """
        for update in updates:
            # print(f'offset in remove_banned_words: {self.updates_offset}')
            
            message_id = update["message"]["message_id"]
            chat_id = update["message"]["chat"]["id"]
            text = update["message"]["text"]
            if 'test' in text.lower():
                url = self.API_URL + self.API_ID + '/deleteMessage'
                params = {'chat_id': chat_id, 'message_id': message_id}
                # print(params)
                response = requests.post(url, data=params)
                # response.raise_for_status()
                if response.status_code == 200:
                    result = json.loads(response.text)
                    
                else:
                    print(f'Couldn\'t delete the message "{text} {chat_id} {message_id}".')

    def send_message(self, chat_id='969768646', msg='Test message. Telegram API'):
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
    # bot.send_message(-991250963)
    bot.remove_banned_words(bot.get_updates())