from flask import Blueprint, render_template
from blog.utils.db import Post

home_bp = Blueprint(name="home", import_name=__name__, template_folder='../templates')


@home_bp.route('/')
@home_bp.route('/home')
def home():
    page_info = Post.objects.paginate(page=1, per_page=10)
    return render_template('home.html', page_info=page_info)
