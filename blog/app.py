#!/usr/bin/python3
import pymongo
from flask import Flask, current_app
from flask_mongoengine import MongoEngine

app = Flask(import_name=__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = MongoEngine(app)

with app.app_context():
    try:
        db.connection.admin.command('ismaster')
    except Exception as e:
        print(e)

from blog.route.posts import post_blueprint
from blog.route.home import home_blueprint
from blog.route.tags import tag_blueprint

app.register_blueprint(post_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(tag_blueprint)

if __name__ == '__main__':
    app.run()
