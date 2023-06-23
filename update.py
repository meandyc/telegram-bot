#! python3

from message import Message

class Update:

    def __init__(self, update_id, message, edited_message, channel_post, edited_channel_post,
                 inline_query, chosen_inline_result, callback_query, shipping_query, pre_checkout_query,
                 poll, poll_answer, my_chat_member, chat_member, chat_join_request):
        """
        This object represents an incoming update.
        At most one of the optional parameters can be present in any given update.
        """
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request