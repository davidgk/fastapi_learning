from fastapi import APIRouter, HTTPException, Depends

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
from ..repository import post_repository as repository

def save_post( db, post_dict):
    try:
        # posts.append(post_dict)
        return repository.create_post(db, post_dict)
    except Exception as ex:
        raise HTTPException(status_code=500,detail=ex)

def find_post_by_id( id, db):
    try:
        return repository.get_post_by_id(db, id)
    except Exception as ex:
        raise HTTPException(status_code=404,detail=ex)

def get_posts(db):
    return repository.get_posts(db)

async def find_and_update(post_id, post_data, db ):
    try:
        post_db = repository.get_post_by_id(db, post_id)
        if not post_db:
            raise HTTPException(status_code=404, detail="Post not found")
        return repository.update(db, post_db, post_data )
    except BaseException as exc:
        print(exc)
        return None

# def update_fields(post, postData):
#     if postData.keys().__contains__('title'):
#         post.title = postData['title']
#     if postData.keys().__contains__('author'):
#         post.title = postData['author']
#     if postData.keys().__contains__('content'):
#         post.title = postData['content']


def evaluate_post(post, post_id: str, title=None):
    exists = post["id"] == post_id
    if exists and title:
        exists = post["title"] == title
    return exists

