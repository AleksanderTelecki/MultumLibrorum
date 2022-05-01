import json
import requests
from .models import *
import urllib.request


def getListOfItems(data, json_object):
    return [item for item in data[json_object]]


def download_file(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    return filename


def gutenbergDataMigrator():
    response_api = requests.get('https://gutendex.com/books/?copyright=false&page=1')
    raw_data = response_api.text
    parsed_data = json.loads(raw_data)

    next = parsed_data['next']
    results = parsed_data['results']
    # for book in results:
    #     title = book['title']
    #     authors = [item['name'] for item in book['authors']]
    #     genres = getListOfItems(book, 'subjects')
    #     bookshelves = getListOfItems(book, 'bookshelves')
    #     languages = getListOfItems(book, 'languages')
    #     html = download_file(book['formats']['text/html'])
    #     print(html)

    # epub = download_file(results[1]['formats']['application/epub+zip'], f"static/data/{results[1]['title']}{}.epub")

