import requests
from bs4 import BeautifulSoup
from elice_library.models import AnonymousUser


def init_anonymouse():
    url = 'https://ko.wikipedia.org/wiki/%ED%8F%AC%EC%9C%A0%EB%A5%98%EC%9D%98_%EB%AA%A9%EB%A1%9D'

    response = requests.get(url)
    names = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        head = soup.select('#mw-content-text > div.mw-parser-output > p')

        for i in head:
            for j in i.get_text().split('·'):
                auser = AnonymousUser(name = j.strip())
                names.append(auser.name)
    return names

init_anonymouse()