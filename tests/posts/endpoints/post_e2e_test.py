from tests.commons_test import client, async_get_call
import pytest
pytest_plugins = ('pytest_asyncio',)
POST_URL = "/api/posts/"
@pytest.mark.asyncio
async def test_read_all_posts():
    response = await async_get_call(POST_URL)
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_should_find_a_post_with_correct_id():
    all_posts_response = client.get(POST_URL)
    a_post = all_posts_response.json()[0]
    response = get_post_by_id(a_post["id"])
    assert response.status_code == 200
    assert response.json()["id"] == a_post["id"]

def get_post_by_id(id: str):
    return client.get(f'{POST_URL}{id}')

def test_should_create_a_post_with_the_correct_values():
    a_post = {
        "title": "el loco",
        "author": "pepe",
        "content": "peliculon",
    }
    response = client.post(POST_URL, json=a_post)
    assert response.json()["id"] is not None

def test_should_not_create_a_post_if_some_principal_values_are_missing():
    a_post = {
        "author": "pepe",
        "content": "peliculon",
    }
    response = client.post(POST_URL, json=a_post)
    assert response.status_code == 422

def test_given_an_existing_post_should_be_able_to_be_updated():
    all_posts_response = client.get(POST_URL)
    a_post = all_posts_response.json()[0]
    assert a_post["title"] == "aTitle"
    a_post["title"] = "el seminario del loco"
    post_updated = client.put(f'{POST_URL}{a_post["id"]}', json=a_post)
    assert  post_updated.json()['title'] == "el seminario del loco"

def test_given_a_not_existing_post_should_return_404_error():
    all_posts_response = client.get(POST_URL)
    a_post = all_posts_response.json()[1]
    a_post["title"] = "el seminario del loco2"
    response = client.put(f'{POST_URL}wrong_uuid_123', json=a_post)
    assert response.status_code == 404
