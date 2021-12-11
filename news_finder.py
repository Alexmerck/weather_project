from bs4 import BeautifulSoup
import requests


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_python_news():
    html = get_html("https://news.drom.ru/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.findAll('div', class_='b-info-block__info')
        all_news = []
        for news in news_list:
            news_text = news.find(
                'div', class_='b-info-block__title b-link').text
            all_news.append({'title': news_text})
        return all_news
    return False
