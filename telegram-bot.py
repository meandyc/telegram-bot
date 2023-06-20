#! python3

import requests, json
from pprint import pprint
from update import Update
from message import Message
from chat import Chat

class TelegramBot:
    # TestGroup -991250963, meandyc 969768646, Nilo -1001258742986, Jean Claude 6067145739, Pablo 627140333
    
    def __init__(self):
        self.API_URL = 'https://api.telegram.org/bot'
        with open('/home/andy/Documents/Python/telegramBot/.telegram-api-token', 'r') as f:
            self.API_ID = f.read()
    
    def getUpdates(self):
        """
        Use this method to receive incoming updates using long polling.
        Returns an Array of Update objects.
        """
        try:
            url = self.API_URL + self.API_ID + '/getUpdates'
            response = requests.get(url)
            result_dict = json.loads(response.text)
            updates = result_dict['result']
            pprint(updates[-2])
            
            print('--')
            pprint(updates[-2]['update_id'])
            print('--')

            print('--')
            pprint(updates[-2]['message']['chat'])
            chatId = updates[-2]['message']['chat']['id']
            chatTitle = updates[-2]['message']['chat']['title']
            chatType = updates[-2]['message']['chat']['type']
            print(f'id: {chatId}, chatTitle: {chatTitle}, chatType: {chatType}')
            chat = Chat(id=chatId, title=chatTitle, type=chatType)
            print('after Obj')
            print(f'id: {chat.chatId}, chatTitle: {chat.chatTitle}, chatType: {chat.chatType}')
            print('--')
                
            response.raise_for_status()    
        except Exception as e:
            print(e)
    
    def sendMessageToGroup(self, group, msg='Test message to a group'):
        """
        Use this method to send text messages. On success, the sent Message is returned.
        """
        url = self.API_URL + self.API_ID + '/sendMessage'
        data = {'chat_id': group, 'text': msg}
        response = requests.post(url, data=data)
        result_dict = json.loads(response.text)
        pprint(result_dict)
        try:
            response.raise_for_status()    
        except Exception as e:
            print(e)
    
    
    def sendMessageToMyself(self, chatId='969768646', msg='Test message Telegram API'):
        """
        Use this method to send text messages. On success, the sent Message is returned.
        """
        url = self.API_URL + self.API_ID + '/sendMessage'
        data = {'chat_id': chatId, 'text': msg}
        response = requests.post(url, data=data)
        result_dict = json.loads(response.text)
        pprint(result_dict)
        try:
            response.raise_for_status()    
        except Exception as e:
            print(e)    

if __name__ == '__main__':
    print('\n')

    bot = TelegramBot()
    # bot.sendMessageToMyeself()
    bot.sendMessageToGroup('627140333', 'Dos gardenias para ti... Estreno el proximo domingo...')
    # bot.sendMessageToGroup('-991250963', 'Another test')    #pablo
    
    # bot.getUpdates()