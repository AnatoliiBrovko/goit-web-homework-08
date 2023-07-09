import json
from src.models import Quote, Author


def seed_authors(path):
    with open(path, 'r') as file:
        data = json.load(file)
        for item in data:
            document = Author(**item)
            document.save()


def seed_quotes(path):
    with open(path, 'r') as file:
        data = json.load(file)
        for d in data:
            author_name = d['author']
            author = Author.objects(fullname=author_name).first()
            if not author:
                author = Author(fullname=author_name)
                author.save()

            quote = Quote(
                author=author, quote=d['quote'], tags=d['tags'])
            quote.save()


if __name__ == "__main__":
    seed_authors('src/authors.json')
    seed_quotes('src/qoutes.json')