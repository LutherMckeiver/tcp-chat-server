
import random
import uuid


class ChatClient(object):
    def __init__(self, conn=None, addr=None):
        self.id = str(uuid.uuid4())
        self.nick = 'user_{}'.format(random.random())
        self.conn = conn
        self.addr = addr

    def update_nick(self, new_nick):
        self.nick = new_nick
        return self
