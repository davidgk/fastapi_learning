from fastapi import FastAPI, HTTPException

from src.configs.start_app import app
from src.posts.controllers.python_controller import PostController
from src.models.post import Post
from uuid import uuid4 as uuid


posts = [{
    "id": "some-uuid",
    "title": "aTitle",
    "author": "anAuthor",
    "content": "aContent",
    "created_at": "2023-01-19T15:56:38.015865",
    "published_at": None,
    "published": False
},
    {
        "id": "7a75a41b-1acb-4a18-8ea6-441f877cb812",
        "title": "el bueno",
        "author": "pepe",
        "content": "peliculon",
        "created_at": "2023-01-19T16:17:38.725225",
        "published_at": None,
        "published": False
    },
    {
        "id": "7a75a41b-1acb-4a18-8ea6-441f877cb992",
        "title": "el loco",
        "author": "pepe",
        "content": "peliculon",
        "created_at": "2023-01-19T16:17:38.725225",
        "published_at": None,
        "published": False
    }
]


@app.get("/")
async def root():
    return {"message": 'Welcome to my Rest API'}

postApi = PostController()


# @app.get("/api/posts")
# async def get_posts():
#     return posts
#
#
# @app.post("/api/posts")
# async def save_posts(post: Post):
#     post_dict = post.dict()
#     post_dict["id"] = uuid()
#     posts.append(post_dict)
#     return post_dict
#
#
# @app.get("/api/posts/{post_id}")
# async def save_posts(post_id: str, title=None):
#     posts_filtered = list(filter(lambda post: evaluate_post(post, post_id, title), posts) or [])
#     if len(posts_filtered) > 0:
#         return posts_filtered[0]
#     else:
#         raise HTTPException(status_code=404)
#
#
# @app.delete("/api/posts/{post_id}")
# async def remove_posts(post_id: str):
#     was_removed = False
#     for idx, post in enumerate(posts):
#         found = evaluate_post(post, post_id)
#         if found:
#             posts.remove(post)
#             was_removed = True
#     if not was_removed:
#         raise HTTPException(status_code=404)
#     return "removed"
#
#
# async def find_and_update(post_id, postData):
#     for post in posts:
#         found = evaluate_post(post, post_id)
#         if found:
#             await update_att(post, postData, "title")
#             await update_att(post, postData, "author")
#             await update_att(post, postData, "content")
#             return post
#     return None
#
#
# @app.put("/api/posts/{post_id}")
# async def update_posts(post_id: str, postData: dict):
#     post_updated = await find_and_update(post_id, postData)
#     if not post_updated:
#         raise HTTPException(status_code=404)
#     return post_updated
#
#
# async def update_att(post, postData, att: str):
#     if postData.keys().__contains__(att):
#         post[att] = postData[att]
#
#
# async def find_and_update(post_id, postData):
#     for post in posts:
#         found = evaluate_post(post, post_id)
#         if found:
#             await update_att(post, postData, "title")
#             await update_att(post, postData, "author")
#             await update_att(post, postData, "content")
#             return post
#     return None
#
# def evaluate_post(post, post_id: str, title=None):
#     exists = post["id"] == post_id
#     if exists and title:
#         exists = post["title"] == title
#     return exists
