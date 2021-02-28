#!/usr/bin/python3
from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine

from blog.route.posts import post_bp
from blog.route.home import home_bp
from blog.route.tags import tag_bp
from blog.route.api import bp_api
from blog.route.admin import CustomIndexlView, CustomModelView, auth_bp
from blog.utils.db import Post

app = Flask(import_name=__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = MongoEngine(app)

app.register_blueprint(post_bp)
app.register_blueprint(home_bp)
app.register_blueprint(tag_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(bp_api)

admin = Admin(app, name="blog", template_mode='bootstrap3', index_view=CustomIndexlView())
admin.add_view(CustomModelView(Post))

if __name__ == '__main__':
    app.run()
