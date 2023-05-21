from mongoengine import connect, StringField, Document, ReferenceField, ListField, CASCADE


connect(host="mongodb+srv://koss:koss@cluster0.q0ppart.mongodb.net/?retryWrites=true&w=majority")


class Author(Document):
    fullname = StringField(max_length=250)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=250)
    description = StringField()


class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    meta = {'allow_inheritance': True}


