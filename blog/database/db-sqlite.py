import click
import sqlite3

from flask import g, current_app
from flask.cli import with_appcontext
from pprint import pprint

def get_db():
    pprint(current_app.config)
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
    else:
        print('[*] db is None.')

def init_app(app):
    app.teardown_appcontext(close_db)