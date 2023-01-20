import pytest
from fastapi import HTTPException

from src.posts.controllers import post_controller as controller

pytest_plugins = ('pytest_asyncio',)
POST_URL = "/api/posts/"

@pytest.mark.asyncio
async def test_read_all_posts():
    posts = await controller.get_posts()
    assert len(posts) == 3

@pytest.mark.asyncio
async def test_should_find_a_post_with_correct_id():
    posts = await controller.get_posts()
    a_post = posts[0]
    post = await controller.get_post_by_id(a_post["id"])
    assert post["id"] == a_post["id"]

@pytest.mark.asyncio
async def test_should_create_a_post_with_the_correct_values():
    a_post = {
        "title": "el loco",
        "author": "pepe",
        "content": "peliculon",
    }
    post = await controller.save_posts(a_post)
    assert post["id"] is not None
    assert post["title"] == a_post["title"]
    assert post["author"] == a_post["author"]
    assert post["content"] == a_post["content"]

@pytest.mark.skip
async def test_should_not_create_a_post_if_some_principal_values_are_missing():
    try:
        a_post = {
            "author": "pepe",
            "content": "peliculon",
        }
        await controller.save_posts(a_post)
    except:
        raise ('Should fix this')

@pytest.mark.asyncio
async def test_given_an_existing_post_should_be_able_to_be_updated():
    posts = await controller.get_posts()
    a_post = posts[0]
    assert a_post["title"] == "aTitle"
    a_post["title"] = "el seminario del loco"
    post_updated = await controller.find_and_update(a_post["id"], a_post)
    assert post_updated['title'] == "el seminario del loco"

@pytest.mark.asyncio
async def test_given_a_not_existing_post_should_return_404_error():
    try:
        posts = await controller.get_posts()
        a_post = posts[1]
        a_post["title"] = "el seminario del loco2"
        await controller.update_posts("wrong_uuid_123", a_post)
        raise Exception("should fail")
    except HTTPException as exc:
        assert exc.status_code == 404
