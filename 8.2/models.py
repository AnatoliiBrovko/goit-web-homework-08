from mongoengine import *

connect(host="mongodb+srv://userweb11:Qwerty@cluster0.qlztwtl.mongodb.net/Module_8_2?retryWrites=true&w=majority", ssl=True)

class Recipient(Document):

    fullname = StringField()
    email = StringField()
    message = BooleanField(default=False)

