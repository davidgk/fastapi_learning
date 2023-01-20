from fastapi import APIRouter
from src.posts.controllers import post_controller

router = APIRouter(prefix='/api')
router.include_router(post_controller.router)