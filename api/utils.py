import json
import requests
from .models import *
import shortuuid
from faker import Faker
import datetime
import random
from pathlib import Path
import os


def getListOfItems(data, json_object):
    return [item for item in data[json_object]]


def download_file(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    return filename


def check_and_save(model, items):
    for item in items:
        if not model.objects.filter(name=item):
            entity = model(name=item)
            entity.save()

    model_objects = []
    for item in items:
        model_objects += model.objects.filter(name=item)

    return model_objects


def gutenbergDataMigrator():
    counter = 0
    for i in range(105, 150):
        print(i)
        response_api = requests.get(f"https://gutendex.com/books/?copyright=false&page={i}")
        raw_data = response_api.text
        parsed_data = json.loads(raw_data)

        results = parsed_data['results']

        for book in results:
            counter += 1
            print(counter)
            authors = [item['name'] for item in book['authors']]
            authors_object = check_and_save(Author, authors)
            genres = getListOfItems(book, 'subjects')
            genres_object = check_and_save(Genres, genres)
            bookshelves = getListOfItems(book, 'bookshelves')
            bookshelf_object = check_and_save(BookShelf, bookshelves)
            languages = getListOfItems(book, 'languages')
            languages_object = check_and_save(Language, languages)

            title = book['title']

            uuid = shortuuid.uuid()
            fake = Faker()
            isbn = fake.isbn13()

            try:
                txt = download_file(book['formats']['text/plain'],
                                    f"static/storage/txt/{isbn}-{uuid}.txt")
            except:
                continue

            try:
                epub = download_file(book['formats']['application/epub+zip'],
                                     f"static/storage/epub/{isbn}-{uuid}.epub")
            except:
                continue

            try:
                image_url = book['formats']['image/jpeg'].replace('small', 'medium')
                image = download_file(image_url, f"static/storage/jpg/{isbn}-{uuid}.jpg")
            except:
                continue

            start_date = datetime.date(year=1900, month=1, day=1)
            end_date = datetime.date(year=2020, month=1, day=1)
            publication_date = fake.date_between(start_date=start_date, end_date=end_date)

            publisher = random.choice(list(Publisher.objects.all()))

            book = Book.objects.create(title=title,
                                       publicationDate=publication_date,
                                       availableQuantity=fake.pyint(5, 1000, 1),
                                       price=fake.pydecimal(right_digits=2, positive=True, min_value=5, max_value=500))

            book.author.add(*authors_object)
            book.language.add(*languages_object)
            book.bookshelf.add(*bookshelf_object)
            book.genres.add(*genres_object)
            book.publisher = publisher
            book.isbn13 = isbn

            book.image.name = image[14:]
            book.epub.name = epub[14:]
            book.txt.name = txt[14:]

            book.save()


