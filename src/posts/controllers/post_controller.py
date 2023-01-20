from fastapi import APIRouter, HTTPException, Depends
from ..services import post_service as service
from src.posts.services.post_service import posts, evaluate_post, find_and_update
from sqlalchemy.orm import Session

from ...commons.dependencies.dependencies import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Post"],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
async def get_posts(db: Session = Depends(get_db)):
    return service.get_posts(db)

@router.get("/{post_id}")
async def get_post_by_id(post_id: str, db: Session = Depends(get_db)):
    posts_filtered = service.find_post_by_id(post_id, db )
    if posts_filtered:
        return posts_filtered
    else:
        raise HTTPException(status_code=404)

@router.post('/')
async def save_posts(post_dict: dict, db: Session = Depends(get_db)):
    return service.save_post(db, post_dict)

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
async def update_posts(post_id: str, postData: dict,  db: Session = Depends(get_db)):
    post_updated = await find_and_update(post_id, postData, db )
    if not post_updated:
        raise HTTPException(status_code=404)
    return post_updated


