from flask import Blueprint, render_template
from blog.database.models import Post

tag_blueprint = Blueprint(name="tag_page",
                          import_name=__name__,
                          template_folder='../templates')

@tag_blueprint.route("/tags")
def view_tags():
    pipline = [
            {"$group": {"_id": "$tags",
                "articles": {"$push": {"title": "$title",
                "date": {"$dateToString": { "format": "%Y-%m-%d", "date": "$date"}},
                "id": {"$toString": "$_id"}}},
                "count": {"$sum": 1}}},
    ]
    views = list(Post.objects().aggregate(pipline))
    tag_info = [dict(tag=item["_id"], count=item['count']) for item in views]
    article_info = [dict(tag=item['_id'], articles=item['articles']) for item in views]
    print(article_info, tag_info)
    return render_template("category.html", tag_info=tag_info, article_info=article_info)
