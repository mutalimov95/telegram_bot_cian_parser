import time
import random

from models import ChatLink
from utils import format_key_for_cache
from parser import parse
from settings import bot, CACHE


def pereodic_send_links():
    while True:
        try:
            chatlinks = ChatLink.select().dicts()
            for chat in chatlinks:
                chat_id = chat.chat_id
                link = chat.link
                card_urls = parse(link)
                for url in card_urls:
                    if CACHE.get(format_key_for_cache(chat_id, url)) is None:
                        CACHE[format_key_for_cache(chat_id, url)] = url
                        bot.send_message(chat_id, url)
            time.sleep(random.randrange(60*5, 60*20))
        except Exception:  # никогда не прекращаем работу
            continue
