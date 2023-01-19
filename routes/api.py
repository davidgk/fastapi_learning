from fastapi import APIRouter
from src.endpoints import post

router = APIRouter(prefix='/api')
router.include_router(post.router)