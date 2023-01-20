from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.commons.configuration.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=False, nullable= True)
    author = Column(String, index=True, nullable= True)
    content = Column(String, nullable= True)
    published_at = Column(DateTime, nullable= True)
    created_at = Column(DateTime,default= datetime.now())
    published = Column(Boolean, default=False)

