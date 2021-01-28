from flask import Blueprint, render_template, current_app
from blog.database.models import Post


home_blueprint = Blueprint(name="home",
                           import_name=__name__,
                           template_folder='../templates')

@home_blueprint.route('/')
@home_blueprint.route('/home')
def home():
    page_info = Post.objects.paginate(page=1, per_page=10)
    return render_template('home.html', page_info=page_info)
