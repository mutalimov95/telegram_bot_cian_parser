import re

import requests
from bs4 import BeautifulSoup


def parse(link):
    card_urls = []
    response = requests.get(link)
    if response.status_code != 200:
        raise requests.ConnectionError
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    main_wrap = soup.find('div', id='frontend-serp').div
    card_wrapper = main_wrap.find_all('div', class_=re.compile(r'\w*--wrapper-\w*'), recursive=False, limit=3)[2]
    cards = card_wrapper.find_all('div', class_=re.compile(r'\w*--card--\w*'))
    for c in cards[:-1]:
        card_a_tag = c.find('a', class_=re.compile(r'\w*--header--\w*'))
        card_urls.append(card_a_tag['href'])
    return card_urls