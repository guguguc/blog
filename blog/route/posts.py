from flask import Blueprint, render_template
from markdown import markdown

from blog.utils.db import Post

bp_post = Blueprint(name="post_page",
                    import_name=__name__,
                    template_folder='../templates',
                    url_prefix="/achieves")


@bp_post.route('/', defaults={'page': 1})
@bp_post.route('/page/<int:page>')
def list_posts(page):
    page_info = Post.objects.paginate(page=page, per_page=15)
    return render_template('achieves.html', page_info=page_info)


@bp_post.route('/<post_id>')
def get_post(post_id):
    post = Post.objects(id=post_id).get_or_404()
    post.content = markdown(post.content, extensions=['extra', 'codehilite'])
    return render_template('posts.html', post=post)
