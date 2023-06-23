#! python3

class Chat:

    def __init__(self, id, type, title=None, username=None, first_name=None):
        """
        This object represents a chat.
        """
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name