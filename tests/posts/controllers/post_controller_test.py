import pytest
from tests.commons_test import db_test_session
from fastapi import HTTPException
from src.posts.controllers import post_controller as controller
from tests.posts.factory.post_factory import create_post
from src.posts.models.post_db import Post as PostModel
import pytest_asyncio

pytest_plugins = ('pytest_asyncio',)
POST_URL = "/api/posts/"

class DBContainer:
    def __init__(self):
        self.db = db_test_session
    def clean_posts(self):
        posts = self.db.query(PostModel).all()
        for post in posts:
            self.db.delete(post)


@pytest_asyncio.fixture  # dedicated fixture decorator that will do the right thing
async def fixture_posts():
    global dbContainer
    dbContainer = DBContainer()
    dbContainer.clean_posts()
    yield
    dbContainer.db.close()
    print("test concluded")

@pytest.mark.asyncio
async def test_read_all_posts(fixture_posts):
    await controller.save_posts(create_post(), dbContainer.db)
    posts = await controller.get_posts(dbContainer.db)
    assert len(posts) == 1


@pytest.mark.asyncio
async def test_should_create_a_post_with_the_correct_values(fixture_posts):
    a_post = create_post()
    post = await controller.save_posts(a_post, dbContainer.db)
    assert post.id is not None
    assert post.title == a_post["title"]
    assert post.author == a_post["author"]
    assert post.content == a_post["content"]


@pytest.mark.asyncio
async def test_should_find_a_post_with_correct_id(fixture_posts):
    post = await controller.save_posts(create_post(), dbContainer.db)
    a_post = await controller.get_post_by_id(post.id, dbContainer.db)
    assert post.id == a_post.id


@pytest.mark.skip
async def test_should_not_create_a_post_if_some_principal_values_are_missing(fixture_posts):
    try:
        a_post = {
            "author": "pepe",
            "content": "peliculon",
        }
        await controller.save_posts(a_post)
    except:
        raise ('Should fix this')

@pytest.mark.asyncio
async def test_given_an_existing_post_should_be_able_to_be_updated(fixture_posts):
    a_post = await controller.save_posts(create_post(), dbContainer.db)
    a_post.title = "el seminario del loco"
    post_updated = await controller.update_posts(a_post.id, a_post.__dict__, dbContainer.db)
    assert post_updated.title == "el seminario del loco"

@pytest.mark.asyncio
async def test_given_a_not_existing_post_should_return_404_error(fixture_posts):
    try:
        a_post = await controller.save_posts(create_post(), dbContainer.db)
        a_post.title = "el seminario del loco"
        await controller.update_posts("wrong_uuid_123", a_post)
        raise Exception("should fail")
    except HTTPException as exc:
        assert exc.status_code == 404
