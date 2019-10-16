from threading import Thread

from validator_collection import checkers

from models import ChatLink
from settings import bot
from pereodic import pereodic_send_links


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Введите ссылку")


@bot.message_handler(func=lambda url: checkers.is_url(url))
def link_save(message):
    chat_id = message.chat.id
    if ChatLink.select().where(chant_id=chat_id).exist():
        ChatLink.delete().where(chat_id=chat_id).execute()
    try:
        ChatLink.create(chat_id=chat_id, link=message.text.strip())
    except:  # отлавливаем все подряд
        bot.reply_to(message, f'Ошибка, ссылка не сохранена')
    else:
        bot.reply_to(message, f'Ссылка "{message.text}" сохранена')


@bot.message_handler(commands=['remove'])
def remove(message):
    obj = ChatLink.get(chat_id=message.chat.id)
    link = obj.link
    obj.delete_instance()
    bot.reply_to(message, f'Ссылка "{link}" удалена')


if __name__ == '__main__':
    thread = Thread(target=pereodic_send_links)
    thread.start()
    bot.polling(none_stop=True, interval=0)
