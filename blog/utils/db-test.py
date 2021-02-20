#!/usr/bin/python3
import mongoengine as me
import datetime

conn = me.connect("Blog")


class Post(me.Document):
    title = me.StringField(max_length=200, required=True, unique=True)
    date = me.DateTimeField(default=datetime.datetime.now)
    tags = me.StringField(max_length=100)
    content = me.StringField(required=True)
    meta = {'collection': 'post'}


if __name__ == "__main__":
    blogs = [tuple(line.strip().split()) for line in open("../database/article.txt").readlines()]
    content = open("../achieves/test2.md").read()

    # Insert
    for title, tag in blogs:
        p = Post(title=title, tags=tag, content=content)
        try:
            p.save()
        except Exception as e:
            print(e)

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
