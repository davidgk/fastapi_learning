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

def get_posts(db):
    return repository.get_posts(db)

async def find_and_update(post_id, postData):
    for post in posts:
        found = evaluate_post(post, post_id)
        if found:
            await update_att(post, postData, "title")
            await update_att(post, postData, "author")
            await update_att(post, postData, "content")
            return post
    return None


async def update_att(post, postData, att: str):
    if postData.keys().__contains__(att):
        post[att] = postData[att]


def evaluate_post(post, post_id: str, title=None):
    exists = post["id"] == post_id
    if exists and title:
        exists = post["title"] == title
    return exists

