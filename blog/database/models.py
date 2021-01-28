import datetime

from blog.app import db


class Post(db.Document):
    title = db.StringField(max_length=200, required=True, unique=True)
    date = db.DateTimeField(default=datetime.datetime.now)
    tags = db.ListField(db.StringField(max_length=100), max_length=5)
    content = db.StringField(required=True)
    meta = {'collection': 'post',
            'ordering': ['-date']}
