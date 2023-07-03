#! python3

import requests
import json
from pprint import pprint

class TelegramBot:
    def __init__(self):
        self.API_URL = 'https://api.telegram.org/bot'
        with open('/home/andy/.telegram-bot/.telegram-api-token', 'r') as f:
            self.API_ID = f.read().strip('\n')
    
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
            print(f'Failed sending the message. {response}')

if __name__ == '__main__':
    # meandyc 969768646
    # TestGroup -991250963
    # Nilo -1001258742986 
    # Pablo 627140333
    
    bot = TelegramBot()
    bot.send_message(msg="Torrent downloaded.")