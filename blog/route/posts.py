from flask import Blueprint, render_template, current_app, abort, url_for
from blog.database.models import Post

post_blueprint = Blueprint(name="post_page",
                           import_name=__name__,
                           template_folder='../templates')


@post_blueprint.route('/achieves/', defaults={'page': 1})
@post_blueprint.route('/achieves/page/<int:page>')
def list_posts(page):
    page_info = Post.objects.paginate(page=page, per_page=15)
    return render_template('achieves.html', page_info=page_info)


@post_blueprint.route('/achieves/<post_id>')
def get_post(post_id):
    post = Post.objects(id=post_id).get_or_404()
    return render_template('posts.html', post=post)
