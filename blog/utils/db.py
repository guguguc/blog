import datetime
from flask_mongoengine import Document
from mongoengine import StringField, DateTimeField


class Post(Document):
    title = StringField(max_length=200, required=True, unique=True)
    date = DateTimeField(default=datetime.datetime.now)
    tags = StringField(max_length=100, required=True)
    content = StringField(required=True)
    meta = {'collection': 'post',
            'ordering': ['-date']}
