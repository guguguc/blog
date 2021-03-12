#!/usr/bin/python3
from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine

from blog.route.posts import bp_post
from blog.route.home import bp_home
from blog.route.tags import bp_tag
from blog.route.api import bp_api
from blog.route.admin import CustomIndexlView, CustomModelView, bp_auth

app = Flask(import_name=__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = MongoEngine(app)

app.register_blueprint(bp_post)
app.register_blueprint(bp_home)
app.register_blueprint(bp_tag)
app.register_blueprint(bp_auth)
app.register_blueprint(bp_api)

from blog.utils.db import Post
admin = Admin(app,
              name="blog",
              template_mode='bootstrap3',
              index_view=CustomIndexlView())
admin.add_view(CustomModelView(Post))

if __name__ == '__main__':
    app.run()
