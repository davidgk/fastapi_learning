from uuid import uuid4 as uuid
from sqlalchemy.orm import Session
from ..models.post_db import Post as PostModel
def get_post(db: Session, post_id: str):
    return db.query(PostModel).filter(PostModel.id == post_id).first()

def get_post_by_id(db: Session, id: str):
    return db.query(PostModel).filter_by(id=id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PostModel).offset(skip).limit(limit).all()

def create_post(db: Session, post: dict):
    id=uuid().__str__()
    db_post = PostModel(id=id,
                        author=post["author"],
                        title=post["title"],
                        content=post["content"],
                        published_at=None,
                        )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

