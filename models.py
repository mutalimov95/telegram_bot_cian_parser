import peewee

from settings import db


class ChatLink(peewee.Model):
    chat_id = peewee.IntegerField()
    link = peewee.TextField()

    class Meta:
        database = db
        primary_key = peewee.CompositeKey('chat_id', 'link')
