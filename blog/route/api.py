from datetime import datetime

from flask import Blueprint, jsonify
from blog.utils.db import Post

bp_api = Blueprint(name="api", import_name=__name__, url_prefix="/api")


def convert(data: list):
    res = [{"label": f"Week {week}", "data": [0] * 12} for week in range(1, 6)]
    total_cnt = 0
    for item in data:
        date = item["date"]
        week, month = date["week"], date["month"]
        cnt = item["count"]
        res[week]["data"][month - 1] = cnt
        total_cnt += cnt
    res = dict(total_count=total_cnt, datasets=res)
    return res


@bp_api.route("/activity")
def get_activity():
    current_time = datetime.now()
    start_time = datetime(year=current_time.year, month=1, day=1)
    pipline = [
        {"$match": {"date": {"$gte": start_time, "$lte": current_time}}},
        {"$project": {"month": {"$month": "$date"}, "week": {"$mod": [{"$week": "$date"}, 5]}}},
        {"$group": {"_id": {"month": "$month", "week": "$week"}, "count": {"$sum": 1}}},
        {"$project": {"date": "$_id", "count": "$count", "_id": 0}},
        {"$sort": {"date": 1}}
    ]
    res = list(Post.objects().aggregate(pipline))
    res = convert(res)
    return jsonify(res)
