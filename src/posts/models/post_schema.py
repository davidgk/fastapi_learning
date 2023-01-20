from datetime import datetime
from typing import Text, Optional

from pydantic import BaseModel


class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

    class Config:
        orm_mode = True


