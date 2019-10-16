import os

import peewee
import telebot
from expiringdict import ExpiringDict

BASE_DIR = os.path.abspath(os.path.curdir)


db = peewee.SqliteDatabase(os.path.join(BASE_DIR, 'database.db'))
bot = telebot.TeleBot(os.environ['TOKEN'])
CACHE = ExpiringDict(max_len=10000, max_age_seconds=60*60*24)
