from src.configs.start_app import app
from src.posts.services.post_service import PostService


class PostController:
    def __init__(self):
        self.service = PostService()

    @app.get("/api/posts")
    async def get_posts(self):
        return self.service.get_posts()
