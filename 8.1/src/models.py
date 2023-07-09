from mongoengine import *

connect(host="mongodb+srv://userweb11:Qwerty@cluster0.qlztwtl.mongodb.net/?retryWrites=true&w=majority", ssl=True)


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author)
    quote = StringField()

    meta = {'allow_inheritance': True}
