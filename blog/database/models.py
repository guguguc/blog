import datetime

from blog.app import db


class Post(db.Document):
    title = db.StringField(max_length=200, required=True, unique=True)
    date = db.DateTimeField(default=datetime.datetime.now)
    # category = db.String(required=True)
    # tags = db.ListField(db.StringField(max_length=100), max_length=5)
    tags = db.StringField(max_length=100, required=True)
    content = db.StringField(required=True)
    meta = {'collection': 'post',
            'ordering': ['-date']}
