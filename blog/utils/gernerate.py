import os
import time
import markdown

from blog.utils.db import Post


def get_post(post_path):
    with open(post_path, mode="r", encoding='utf8') as fp:
        post_title = fp.readline().replace('- title ', '').strip()
        # post_tag = fp.readline().replacee('-')
        post_time = fp.readline().replace('- time ', '').strip()
        post_content = markdown.markdown(fp.read(), extensions=['extra'])
    return {
        'post_title': post_title,
        'post_time': post_time,
        'post_content': post_content,
    }


def get_post_time(post_path):
    timestamp = os.path.getctime(post_path)
    return timestamp2time(timestamp)


def timestamp2time(timestamp):
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)


def get_single_post(post_path):
    post_info = get_post(post_path)
    post_time = get_post_time(post_path)
    post = Post(post_info['post_title'], post_info['post_content'], post_time)
    return post


def get_posts():
    """ get all post info in dictory md"""
    path = r"/home/gugugu/repo/article"
    posts = []
    for filename in os.listdir(path):
        if filename.endswith('.md'):
            absolute_path = os.path.join(path, filename)
            post = get_single_post(absolute_path)
            posts.append(post)
    return posts
