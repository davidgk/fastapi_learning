from fastapi import APIRouter, HTTPException

from src.services.post_service import posts, evaluate_post, find_and_update
from src.models.post import Post
from uuid import uuid4 as uuid

router = APIRouter(
    prefix="/posts",
    tags=["Post"],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
async def get_posts():
    return posts


@router.post('/')
async def save_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = uuid()
    posts.append(post_dict)
    return post_dict


@router.get("/{post_id}")
async def save_posts(post_id: str, title=None):
    posts_filtered = list(filter(lambda post: evaluate_post(post, post_id, title), posts) or [])
    if len(posts_filtered) > 0:
        return posts_filtered[0]
    else:
        raise HTTPException(status_code=404)


@router.delete("/{post_id}")
async def remove_posts(post_id: str):
    was_removed = False
    for idx, post in enumerate(posts):
        found = evaluate_post(post, post_id)
        if found:
            posts.remove(post)
            was_removed = True
    if not was_removed:
        raise HTTPException(status_code=404)
    return "removed"


@router.put("/{post_id}")
async def update_posts(post_id: str, postData: dict):
    post_updated = await find_and_update(post_id, postData)
    if not post_updated:
        raise HTTPException(status_code=404)
    return post_updated


