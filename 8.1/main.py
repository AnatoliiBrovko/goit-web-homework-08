from src.models import Quote, Author


def find_author(name):
    auth = Author.objects(fullname=name).first()
    if auth:
        quotes = Quote.objects(author=auth)
        print(f"{name}'s quotes:")
        for quote in quotes:
            print((quote.quote).encode('windows-1251').decode('utf-8'))
    else:
        print(f"'{name}' is not defined.")


def find_tag(tag):
    quotes = Quote.objects(tags=tag)
    print(f"Quotes were found for the tag '{tag}':")
    for quote in quotes:
        print((quote.quote).encode('windows-1251').decode('utf-8'))


def find_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    print(f"Quotes were found for the tags '{tags}':")
    for quote in quotes:
        print((quote.quote).encode('windows-1251').decode('utf-8'))


def parse_inputs():
    while True:
        inputs = input("\nFind a quote by tag (tag:*), author name (name: *), or set of tags (tags:*,*):\n")

        _input = inputs.split(":")

        if _input[0].lower() == "name":
            data = _input[1].strip()
            find_author(data)

        elif _input[0].lower() == "tag":
            data = _input[1].strip()
            find_tag(data)

        elif _input[0].lower() == "tags":
            data = _input[1].strip()
            find_tags(data)

        elif _input[0].lower() == "exit":
            break

        else:
            print(f"\nInput '{inputs}' is not correct. Repeat correct input")


if __name__ == "__main__":
    parse_inputs()