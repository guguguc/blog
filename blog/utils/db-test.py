import os
import datetime

import mongoengine as me

conn = me.connect("Blog")


class Post(me.Document):
    title = me.StringField(max_length=200, required=True, unique=True)
    date = me.DateTimeField(default=datetime.datetime.now)
    tags = me.StringField(max_length=100)
    content = me.StringField(required=True)
    meta = {'collection': 'post'}


def gen_article(dirname):
    files = os.listdir(dirname)
    articles = [
        dict(title=filename,
             tag="test",
             content=open(os.path.join(dirname, filename)).read())
        for filename in files
    ]
    return articles


if __name__ == "__main__":
    articles = gen_article("../achieves")

    # Insert
    for article in articles:
        p = Post(title=article["title"],
                 tags=article["tag"],
                 content=article["content"])
        p.save()

    # Query
    for post in Post.objects:
        print(post.title)

    # all posts with tags ['python', 'programming']
    print('[*] all posts has tags [python, programming]')
    p2 = Post.objects(tags='python')
    for post in p2:
        print(post.tags, post.content)

    # all posts containing tag ['python']
    print('[*] all posts containing tag *python*')
    p3 = Post.objects(tags__exists='python')
    for post in p3:
        print(post.tags, post.content)
